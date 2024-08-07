from nicegui import ui

from . import doc


@doc.demo('Dropdown button', '''
    You can put any elements inside a dropdown button.
''')
def main_demo() -> None:
    with ui.dropdown_button('Open me!', auto_close=True):
        ui.item('Item 1', on_click=lambda: ui.notify('You clicked item 1'))
        ui.item('Item 2', on_click=lambda: ui.notify('You clicked item 2'))


@doc.demo('Dropdown button', '''
    You can put any elements inside a dropdown button.
    Here is a demo with a few switches.
''')
def custom_dropdown_button() -> None:
    with ui.dropdown_button('Settings', icon='settings', split=True):
        with ui.row().classes('p-4 items-center'):
            ui.icon('volume_up', size='sm')
            ui.switch().props('color=negative')
            ui.separator().props('vertical')
            ui.icon('mic', size='sm')
            ui.switch().props('color=negative')


