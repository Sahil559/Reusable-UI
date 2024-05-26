from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from starlette.responses import RedirectResponse
from fastapi import HTTPException, Request
from starlette.middleware.sessions import SessionMiddleware
from authlib.integrations.starlette_client import OAuth, OAuthError
from webapp.auth.config import CLIENT_ID, CLIENT_SECRET
from fastapi.staticfiles import StaticFiles
from nicegui import app, ui
from typing import Optional
from webapp import  main_page, documentation
import os


app.add_middleware(SessionMiddleware, secret_key=os.environ.get('NICEGUI_SECRET_KEY', ''))

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="add any string...")
app.mount("/static", StaticFiles(directory="webapp/auth/static"), name="static")




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


ui.run(title="Reusable U!")



oauth = OAuth()
oauth.register(
    name='google',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    client_kwargs={
        'scope': 'email openid profile',
        'redirect_url': 'http://localhost:8080/auth'
    }
)


templates = Jinja2Templates(directory="webapp/auth/templates")


@app.get("/")
def index(request: Request):
    user = request.session.get('user')
    if user:
        return RedirectResponse('welcome')

    return templates.TemplateResponse(
        name="home.html",
        context={"request": request}
    )


@app.get('/welcome')
def welcome(request: Request):
    user = request.session.get('user')
    if not user:
        return RedirectResponse('/documentation')
    return templates.TemplateResponse(
        name='welcome.html',
        context={'request': request, 'user': user}
    )


@app.get("/login")
async def login(request: Request):
    url = request.url_for('auth')
    return await oauth.google.authorize_redirect(request, url)


@app.get('/auth')
async def auth(request: Request):
    try:
        token = await oauth.google.authorize_access_token(request)
    except OAuthError as e:
        return templates.TemplateResponse(
            name='error.html',
            context={'request': request, 'error': e.error}
        )
    user = token.get('userinfo')
    if user:
        request.session['user'] = dict(user)
    return RedirectResponse('documentation')


@app.get('/logout')
def logout(request: Request):
    request.session.pop('user')
    request.session.clear()
    return RedirectResponse('/')

