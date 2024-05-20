from nicegui import ui
from . import doc


@doc.demo('Footer', '''
    Use the `auto-close` prop to automatically close the menu on any click event directly without a server round-trip.
''')
def navbar():
    with ui.footer().classes(
        "flex justify-center items-center w-full h-16 bg-gray-800 text-white fixed bottom-0"
    ) as footer:
        footerLabel = ui.label("© 2024 All rights reserved")
        logo = ui.image(source="assets/logo.jpg").classes("w-6 h-6")
    with ui.row().classes("flex justify-center items-center w-full"):
            separator2 = ui.separator().classes("w-1/3 bg-white")
    yield