from nicegui import ui

from . import (
    doc,
    section_element,
    section_page_layout,
    section_navigations,
    section_input_area
)

doc.title('Reusable U! Documentation')


doc.text('Overview', '''
    NiceGUI is an open-source Python library to write graphical user interfaces which run in the browser.
    It has a very gentle learning curve while still offering the option for advanced customizations.
    NiceGUI follows a backend-first philosophy:
    It handles all the web development details.
    You can focus on writing Python code.
    This makes it ideal for a wide range of projects including short
    scripts, dashboards, robotics projects, IoT solutions, smart home automation, and machine learning.
''')

doc.text('How to use this guide', '''
    This documentation explains how to use NiceGUI.
    Each of the tiles covers a NiceGUI topic in detail.
    It is recommended to start by reading this entire introduction page, then refer to other sections as needed.
''')


tiles = [
     (section_element, '''
        Listed a variety of elements for user interaction, e.g. `ui.button`, `ui.slider`, `ui.inputs`, etc.
    '''),
    (section_page_layout, '''
        This section covers fundamental techniques as well as several elements to structure your UI.
    '''),
    (section_navigations, '''
        This section covers fundamental techniques as well as several elements to structure your UI.
    '''),
     (section_input_area, '''
        This section covers fundamental techniques as well as several elements to structure your UI.
    '''),
  
]


@doc.extra_column
def create_tiles():
    for documentation, description in tiles:
        page = doc.get_page(documentation)
        with ui.link(target=f'/documentation/{page.name}') \
                .classes('bg-[#5898d420] p-4 self-stretch rounded flex flex-col gap-2') \
                .style('box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);background-color: #1260CC'):
            if page.title:
                ui.label(page.title.replace('*', '')).classes(replace='text-2xl')
            ui.markdown(description).classes(replace='bold-links arrow-links')
