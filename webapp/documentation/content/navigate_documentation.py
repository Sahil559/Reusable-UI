from nicegui import ui

from . import doc


@doc.demo('Navigation functions', '''
         These functions allow you to navigate within the browser history and to external URLs.
    ''')
def main_demo() -> None:
    with ui.row():
        ui.button('Back', on_click=ui.navigate.back)
        ui.button('Forward', on_click=ui.navigate.forward)
        ui.button(icon='savings',
                  on_click=lambda: ui.navigate.to('https://github.com/sponsors/zauberzeug'))


@doc.demo('Navigation functions 2nd', '''Can be used to programmatically open a different page or URL.''')
def open_github() -> None:
    url = 'https://github.com/zauberzeug/nicegui/'
    ui.button('Open GitHub', on_click=lambda: ui.navigate.to(url, new_tab=True))
