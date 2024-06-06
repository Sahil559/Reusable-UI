from nicegui import ui

from . import doc


@doc.demo('Avatar','''You can also add a avatar.
          ''')
def main_demo() -> None:
    ui.avatar('favorite_border', text_color='grey-11')


@doc.demo('Photos', '''
    To use a photo as an avatar, you can use `ui.image` within `ui.avatar`.
''')
def photos() -> None:
    with ui.avatar():
        ui.image('https://robohash.org/robot?bgset=bg2')


