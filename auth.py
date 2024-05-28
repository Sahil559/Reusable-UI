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
passwords = {'user': 'password'}

unrestricted_page_routes = {'/login', '/signup'}


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



@ui.page('/login')
def login() -> Optional[RedirectResponse]:
    def try_login() -> None:  # local function to avoid passing username and password as arguments
        if passwords.get(username.value) == password.value:
            app.storage.user.update({'username': username.value, 'authenticated': True})
            ui.navigate.to(app.storage.user.get('referrer_path', '/'))  # go back to where the user wanted to go
        else:
            ui.notify('Wrong username or password', color='negative')

    if app.storage.user.get('authenticated', False):
        return RedirectResponse('/login')
    
    login_page = ui.query("body").style("background: linear-gradient(to left, #0066ff, #00ccff);")
    with ui.card().classes('absolute-center shadow-lg rounded-lg').style('padding: 10px; width: 900px; background-color: lightblue; '):
       with ui.grid(columns=2):
        with ui.column().classes("w-3/3 p-4").style('margin-left: 40px;'):
            ui.label('Login').style('font-size: 44px; margin-bottom: 2px; margin-top: 20px; font-weight: bold; color: #333;')
            username = ui.input('Email Address').style('margin-bottom: 5px; padding: 10px; border-radius: 5px; border: 1px solid #ccc;')
            password = ui.input('Password', password=True, password_toggle_button=True).style('margin-bottom: 10px; padding: 10px; border-radius: 5px; border: 1px solid #ccc;')
            ui.button('Log in', on_click=try_login).style('width: 100%; margin-bottom: 10px; background-color: #007BFF; color: white; padding: 10px; border-radius: 5px; font-size: 18px;')
            ui.link('Forgot Password?', '/reset_password').style('display: block; text-align: center; margin-ottom: 10px; color: #007BFF; text-decoration: none;')
            ui.button('Log in with Facebook').props('icon=facebook').style('background-color: #3b5998; color: white; padding: 10px; border-radius: 5px;')
            with ui.row().classes('center').style('margin-top: 20px;'):
                ui.link('Sign Up', '/signup').style('margin-right: 10px; color: #007BFF; text-decoration: none;')
                ui.link('Skip for Now', '/').style('color: #007BFF; text-decoration: none;')
        with ui.column().style('margin-top: 20px; margin-bottom: 40px;margin-left: 40px '):
            ui.image(source="webapp/static/about.png").style('width: 190%; height:100%;')
    return login_page


@ui.page('/signup')
def signup() -> None:
    def try_signup() -> None:
        if new_password.value == confirm_password.value:
            passwords[new_username.value] = new_password.value
            app.storage.user.update({'username': new_username.value, 'authenticated': True})
            ui.navigate.to('/')
        else:
            ui.notify('Passwords do not match', color='negative')

    signup_page = ui.query("body").style("background: linear-gradient(to right, #0066ff, #00ccff);")
    with ui.card().classes('absolute-center shadow-lg rounded-lg').style('padding: 20px; width: 900px; background-color: lightblue'):
        with ui.grid(columns=2):
            with ui.column().classes("w-3/3 p-4").style('margin-left: 40px;'):
                ui.label('Sign Up').style('font-size: 44px; margin-bottom: 5px; margin-top: 20px; font-weight: bold; color: #333;')
                new_username = ui.input('Email Address').style('margin-bottom: 5px; padding: 10px; border-radius: 5px; border: 1px solid #ccc; width: 100%;')
                new_password = ui.input('Password', password=True, password_toggle_button=True).style('margin-bottom: 5px; padding: 10px; border-radius: 5px; border: 1px solid #ccc; width: 100%;')
                confirm_password = ui.input('Confirm Password', password=True, password_toggle_button=True).style('margin-bottom: 5px; padding: 10px; border-radius: 5px; border: 1px solid #ccc; width: 100%;')
                ui.button('Sign Up', on_click=try_signup).style('width: 100%; margin-bottom: 10px; background-color: #007BFF; color: white; padding: 10px; border-radius: 5px; font-size: 18px;')
                ui.link('Back to Login', '/login').style('display: block; text-align: center; margin-bottom: 10px; color: #007BFF; text-decoration: none;')
            with ui.column().style('margin-top: 20px; margin-bottom: 40px;margin-left: 40px '):
                ui.image(source="webapp/static/about.png").style('width: 190%; height:100%;')
    return signup_page


ui.run(storage_secret='THIS_NEEDS_TO_BE_CHANGED', title="Reusable U!")
