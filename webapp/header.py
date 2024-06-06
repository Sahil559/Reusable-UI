from pathlib import Path
from typing import Optional

from nicegui import app, ui
from webapp.search import Search
import yaml
import subprocess


HEADER_HTML = (Path(__file__).parent / 'static' / 'header.html').read_text()
STYLE_CSS = (Path(__file__).parent / 'static' / 'style.css').read_text()

# Function to load menu items from JSON file
def load_menu_items(file_path):
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)
    
file_path = (Path(__file__).parent / 'menu.yaml')
menu_data = load_menu_items(file_path)
menu_items = menu_data.get('items', {})

def add_head_html() -> None:
    """Add the code from header.html and reference style.css."""
    ui.add_head_html(HEADER_HTML + f'<style>{STYLE_CSS}</style>')


def add_header(menu: Optional[ui.left_drawer] = None) -> None:
    """Create the page header."""
    dark_mode = ui.dark_mode(value=app.storage.browser.get('dark_mode'), on_change=lambda e: ui.run_javascript(f'''
        fetch('/dark_mode', {{
            method: 'POST',
            headers: {{'Content-Type': 'application/json'}},
            body: JSON.stringify({{value: {e.value}}}),
        }});
    '''))
    header_properties = menu_data.get('header', {})
    with ui.header() \
            .classes(header_properties.get('classes', '')) \
            .style(header_properties.get('style', '')):
        
        # ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')
        # with ui.left_drawer(elevated=True, value=False).classes('bg-blue-100').style('box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); background-color: #1260CC;') as left_drawer:
        #  ui.label('')  

        if menu:
            ui.button(on_click=menu.toggle, icon='menu').props('flat color=white round').classes('lg:hidden')
        with ui.link(target='/').classes('row gap-4 items-center no-wrap mr-auto'):
            logo = ui.image(source="webapp/static/logo2.png").classes("w-10 h-10")
            ui.label('Resuable U!').classes(replace='text-lg text-white')

        with ui.dropdown_button('Documentation', auto_close=True).props('flat round color=white').classes(header_properties.get('classes', 'text-lg text-white')):
              
              ui.item('Page Layout', on_click=lambda: ui.navigate.to('/documentation/section_page_layout')).classes('text-white bg-blue-900 hover:bg-blue-500')
              ui.item('Navigations', on_click=lambda: ui.navigate.to('/documentation/section_navigations')).classes('text-white bg-blue-900 hover:bg-blue-500')
              ui.item('Elements', on_click=lambda: ui.navigate.to('/documentation/section_element')).classes('text-white bg-blue-900 hover:bg-blue-500')
              ui.item('Input Area', on_click=lambda: ui.navigate.to('/documentation/section_input_area')).classes('text-white bg-blue-900 hover:bg-blue-500')
    

        with ui.row().classes('max-[1050px]:hidden  flex items-center'):
            for title_, target in menu_items.items():
                if isinstance(target, dict): 
                    with ui.menu().classes('text-lg text-white'):
                        ui.button(title_).props('flat color=white round')
                        for sub_title, sub_target in target.items():
                            ui.menu_item(sub_title, on_click=lambda sub_target=sub_target: ui.navigate.to(sub_target))
               
                else:
                    if title_ == "Login":
                        with ui.button(on_click=lambda e: ui.navigate.to('/login')).props('flat color=white round').classes('flex items-center'):
                         ui.icon('login').style('margin-right: 8px;')
                         ui.html('<span>Login</span>')
                    else:
                        ui.link(title_, target).classes(replace='text-lg text-white')


        search = Search()
        search.create_button()
        