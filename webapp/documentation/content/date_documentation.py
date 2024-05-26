from nicegui import ui

from . import doc



@doc.demo('Date picker', '''
    This demo shows how to implement a date picker with an input element.
''')
def date():
    with ui.input('Date') as date:
        with date.add_slot('append'):
            ui.icon('edit_calendar').on('click', lambda: menu.open()).classes('cursor-pointer')
        with ui.menu() as menu:
            ui.date().bind_value(date)


@doc.demo('Date filter', '''
    This demo shows how to filter the dates in a date picker.
''')
def date_filter():
    ui.date().props('''default-year-month=2023/01 :options="date => date <= '2023/01/15'"''')


