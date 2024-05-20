from nicegui import ui
from . import doc


@doc.demo('Header', '''
    Use the `auto-close` prop to automatically close the menu on any click event directly without a server round-trip.
''')
def navbar() -> None:
    header = ui.header().classes(
        "flex justify-between items-center transparent no-shadow navbar"
    )
    
    
    with ui.row().classes("flex justify-center items-center w-full"):
            home = ui.link("Home", "/").classes(
                "text-lg font-bold no-underline hover:underline text-yellow"
            )
            about = ui.link("About").classes(
                "text-lg font-bold no-underline hover:underline text-yellow"
            )
            contact = ui.link("Contact").classes(
                "text-lg font-bold no-underline hover:underline text-yellow"
            )
            dark_button1 = ui.button("Dark")
    
    # Create another top-level element for the separator
    with ui.row().classes("flex justify-center items-center w-full"):
        separator1 = ui.separator().classes("w-1/3 bg-white navbar_hr")

     
     