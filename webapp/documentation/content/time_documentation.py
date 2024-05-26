from nicegui import ui

from . import doc


@doc.demo('Time', '''This is the demo to show to set the time''')
def main_demo() -> None:
    ui.time(value='12:00', on_change=lambda e: result.set_text(e.value))
    result = ui.label()

