from typing import Callable

from nicegui import ui

from ..style import subheading
from .demo import demo


def create_intro() -> None:
    @_main_page_demo('About Page', '''
    You can also add a radio.
''')
    def content():
        ui.query("body").style("background-color: lightblue")
        ui.query("a").classes("text-white")
        with ui.grid(columns=2).classes("first_section"):
            with ui.column().classes("ml-7"):
                ui.image(source="webapp/static/about.png").classes("img1")
            with ui.column().classes("w-2/3 p-4"):
                ui.label("About Me").classes(
                    "text-center text-white text-4xl font-semibold pt-4"
                )
                ui.label("Welcome to my portfolio!").classes(
                    "text-bold text-white text-lg"
                )
                ui.label(
                    """
                        Every day, I strive to improve so that one day I can combine my passions with my work. 
                        Currently seeking professional opportunities, I am particularly interested in the fields of aeronautics, 
                        finance, and space, while looking to integrate them with the world of computing.
                        """
                ).classes("text-white w-full")

                ui.button(
                    "Download CV",
                    on_click=lambda: ui.run_javascript(
                        """
                        console.log('downloadCV')
                        function downloadCV(){
                            let boutonDownload = document.querySelectorAll('.downloadCV');
                            boutonDownload.forEach((bouton) => {
                                bouton.addEventListener('click', () => {
                                    window.open('webapp/static/CV.pdf'); 
                                });
                            });
                        }
                        downloadCV();
                    """
                    ),
                ).classes(
                    "bg-blue-500 text-white text-md px-8 py-3 rounded-lg hover:bg-blue-600 focus:outline-none focus:bg-blue-600 downloadCV"
                )

        
        

    @_main_page_demo('Navigations', '''
        Comes with a collection of commonly used UI elements.
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



    @_main_page_demo('Input Areas', '''
        Time demo .
    ''')
    def date():
     with ui.input('Date') as date:
        with date.add_slot('append'):
            ui.icon('edit_calendar').on('click', lambda: menu.open()).classes('cursor-pointer')
        with ui.menu() as menu:
            ui.date().bind_value(date)


    @_main_page_demo('Elements', '''
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



        

def _main_page_demo(title: str, explanation: str) -> Callable:
    def decorator(f: Callable) -> Callable:
        subheading(title)
        ui.markdown(explanation).classes('bold-links arrow-links')
        return demo(f)
    return decorator
