from nicegui import ui

from . import doc


@doc.demo('Checkbox', '''
    You can also add a checkbox.
''')
def main_demo() -> None:
    checkbox = ui.checkbox('check me')
    ui.label('Check!').bind_visibility_from(checkbox, 'value')


