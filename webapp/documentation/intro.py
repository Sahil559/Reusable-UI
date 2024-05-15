from typing import Callable

from nicegui import ui

from ..style import subheading
from .demo import demo


def create_intro() -> None:
    @_main_page_demo('Page Section', '''
        While having reasonable defaults, you can still modify the look of your app with CSS as well as Tailwind and Quasar classes.
    ''')
    def formatting_demo():
        ui.label('Hello')
        
        

    @_main_page_demo('Navigations', '''
        Comes with a collection of commonly used UI elements.
    ''')
    def common_elements_demo():
        ui.label('Hello')


    @_main_page_demo('Input Areas', '''
        Binding values between UI elements .
    ''')
    def binding_demo():
        ui.label('Hello')


    @_main_page_demo('Elements', '''
        Binding values between UI elements .
    ''')
    def binding_demo():
        ui.label('Hello')

        

def _main_page_demo(title: str, explanation: str) -> Callable:
    def decorator(f: Callable) -> Callable:
        subheading(title)
        ui.markdown(explanation).classes('bold-links arrow-links')
        return demo(f)
    return decorator
