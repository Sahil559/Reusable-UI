from typing import Optional
import os
from pathlib import Path
from typing import Optional

from fastapi import HTTPException, Request
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware

from webapp import  main_page, documentation
from starlette.middleware.base import BaseHTTPMiddleware

from nicegui import Client, app, ui

# in reality users passwords would obviously need to be hashed
passwords = {'user1': 'pass1', 'user2': 'pass2'}

unrestricted_page_routes = {'/login'}


class AuthMiddleware(BaseHTTPMiddleware):
    """This middleware restricts access to all NiceGUI pages.

    It redirects the user to the login page if they are not authenticated.
    """

    async def dispatch(self, request: Request, call_next):
        if not app.storage.user.get('authenticated', False):
            if request.url.path in Client.page_routes.values() and request.url.path not in unrestricted_page_routes:
                app.storage.user['referrer_path'] = request.url.path  # remember where the user wanted to go
                return RedirectResponse('/login')
        return await call_next(request)


app.add_middleware(AuthMiddleware)


@ui.page('/')
def _main_page() -> None:
    main_page.create()


@ui.page('/documentation')
def _documentation_page() -> None:
    documentation.render_page(documentation.registry[''], with_menu=False)


@ui.page('/documentation/{name}')
def _documentation_detail_page(name: str) -> Optional[RedirectResponse]:
    if name in documentation.registry:
        documentation.render_page(documentation.registry[name])
        return None
    if name in documentation.redirects:
        return RedirectResponse(documentation.redirects[name])
    raise HTTPException(404, f'documentation for "{name}" could not be found')    

@ui.page('/subpage')
def test_page() -> None:
    ui.label('This is a sub page.')


@ui.page('/login')
def login() -> Optional[RedirectResponse]:
    def try_login() -> None:  # local function to avoid passing username and password as arguments
        if passwords.get(username.value) == password.value:
            app.storage.user.update({'username': username.value, 'authenticated': True})
            ui.navigate.to(app.storage.user.get('referrer_path', '/'))  # go back to where the user wanted to go
        else:
            ui.notify('Wrong username or password', color='negative')

    if app.storage.user.get('authenticated', False):
        return RedirectResponse('/')
    with ui.card().classes('absolute-center'):
        username = ui.input('Username').on('keydown.enter', try_login)
        password = ui.input('Password', password=True, password_toggle_button=True).on('keydown.enter', try_login)
        ui.button('Log in', on_click=try_login)
    return None


ui.run(storage_secret='THIS_NEEDS_TO_BE_CHANGED')
