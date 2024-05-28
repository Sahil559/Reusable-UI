from pathlib import Path
from typing import Optional

from nicegui import app, ui
from .search import Search
import json

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import subprocess


HEADER_HTML = (Path(__file__).parent / 'static' / 'header.html').read_text()
STYLE_CSS = (Path(__file__).parent / 'static' / 'style.css').read_text()

# Function to load menu items from JSON file
def load_menu_items(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)
    
file_path = (Path(__file__).parent / 'menu.json')
menu_data = load_menu_items(file_path)
menu_items = menu_data.get('items', {})

def add_head_html() -> None:
    """Add the code from header.html and reference style.css."""
    ui.add_head_html(HEADER_HTML + f'<style>{STYLE_CSS}</style>')

def start_auth_server():
    """Start the authentication server by running main2.py."""
    subprocess.Popen(['python', 'main2.py'])

@app.get("/login")
def login():
    """Endpoint to start the authentication server."""
    start_auth_server()
    return HTMLResponse(content="<html><body><h1>Authentication Server Started</h1></body></html>")



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
        
        ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')
        
        with ui.left_drawer().classes('bg-blue-100').style('box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); background-color: #1260CC;') as left_drawer:
         ui.label('Side menu')   
        if menu:
            ui.button(on_click=menu.toggle, icon='menu').props('flat color=white round').classes('lg:hidden')
        with ui.link(target='/').classes('row gap-4 items-center no-wrap mr-auto'):
            logo = ui.image(source="webapp/static/logo2.png").classes("w-10 h-10")
            ui.label('Resuable U!').classes(replace='text-lg text-white')

        with ui.row().classes('max-[1050px]:hidden'):
            for title_, target in menu_items.items():
                if isinstance(target, dict):  # Check if the item is a dictionary (dropdown)
                    with ui.menu().classes('text-lg text-white'):
                        ui.button(title_).props('flat color=white round')
                        for sub_title, sub_target in target.items():
                            ui.menu_item(sub_title, on_click=lambda sub_target=sub_target: ui.navigate.to(sub_target))
               
                else:
                    if title_ == "Login":
                        ui.button(title_, on_click=lambda: ui.run_javascript("fetch('/login')")).classes(replace='text-lg text-white')
                    else:
                        ui.link(title_, target).classes(replace='text-lg text-white')


            with ui.dropdown_button('Documentation', auto_close=True, color=None).classes(header_properties.get('classes', '')):
                ui.item('Elements', on_click=lambda: ui.navigate.to('/documentation/section_element'))
                ui.item('Page Layout', on_click=lambda: ui.navigate.to('/documentation/section_page_layout'))
                ui.item('Navigations', on_click=lambda: ui.navigate.to('/documentation/section_navigations'))
                ui.item('Input Area', on_click=lambda: ui.navigate.to('/documentation/section_input_area'))
        

        search = Search()
        search.create_button()
        
                    #  # Add documentation dropdown items
                    # documentation_menu = menu_items.get("Documentation", {})
                    # with ui.menu():
                    #     for doc_title, doc_target in documentation_menu.items():
                    #         ui.menu_item(doc_title, on_click=lambda doc_target=doc_target: ui.navigate.to(doc_target))

                  