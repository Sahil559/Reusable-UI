from nicegui import ui

from . import doc


@doc.demo('Button', '''
    You can also add a button.
''')
def main_demo() -> None:
    ui.button('Click me!', on_click=lambda: ui.notify('You clicked me!'))


@doc.demo('Icons', '''
    You can also add an icon to a button.
''')
def icons() -> None:
    with ui.row():
        ui.button('demo', icon='history')
        ui.button(icon='thumb_up')
        with ui.button():
            ui.label('sub-elements')
            ui.image('https://picsum.photos/id/377/640/360') \
                .classes('rounded-full w-16 h-16 ml-4')


