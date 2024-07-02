from nicegui import ui

from . import doc


@doc.demo('Slider', '''This is the demo of slider
          ''')
def main_demo() -> None:
    slider = ui.slider(min=0, max=100, value=50)
    ui.label().bind_text_from(slider, 'value')



@doc.demo('Disable slider', '''
    You can disable a slider with the `disable()` method.
    This will prevent the user from moving the slider.
    The slider will also be grayed out.
''')
def disable_slider():
    slider = ui.slider(min=0, max=100, value=50)
    ui.button('Disable slider', on_click=slider.disable)
    ui.button('Enable slider', on_click=slider.enable)


