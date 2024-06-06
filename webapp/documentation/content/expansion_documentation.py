from nicegui import ui

from . import doc


@doc.demo('Expansion', '''
    Provides an expandable container as an expansion component.
''')
def main_demo() -> None:
    with ui.expansion('Expand!', icon='work').classes('w-full'):
        ui.label('inside the expansion')


@doc.demo('Expansion with Custom Caption', '''
    A caption, or sub-label, can be added below the title.
''')
def expansion_with_caption():
    with ui.expansion('Expand!', caption='Expansion Caption').classes('w-full'):
        ui.label('inside the expansion')


@doc.demo('Expansion with Grouping', '''
    An expansion group can be defined to enable coordinated open/close states a.k.a. "accordion mode".
''')
def expansion_with_grouping():
    with ui.expansion(text='Expand One!', group='group'):
        ui.label('inside expansion one')
    with ui.expansion(text='Expand Two!', group='group'):
        ui.label('inside expansion two')
    with ui.expansion(text='Expand Three!', group='group'):
        ui.label('inside expansion three')


