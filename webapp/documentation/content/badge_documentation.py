from nicegui import ui

from . import doc


@doc.demo('Badge','''This is the demo of badge''')
def main_demo() -> None:
    with ui.button('Click me!', on_click=lambda: badge.set_text(int(badge.text) + 1)):
        badge = ui.badge('0', color='red').props('floating')

