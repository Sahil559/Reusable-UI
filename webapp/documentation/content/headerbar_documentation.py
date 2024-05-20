# from nicegui import ui
# from . import doc


# @doc.demo('Header', '''
#     Use the `auto-close` prop to automatically close the menu on any click event directly without a server round-trip.
# ''')
# def add_header(menu) -> None:
#     """Create the page header."""
#     menu_items = {
#         'Installation': '/#installation',
#         'Features': '/#features',
#         'Demos': '/#demos',
#         'Documentation': '/documentation',
#         'Examples': '/#examples',
#         'Why?': '/#why',
#     }

#     with ui.header() \
#             .classes('items-center duration-200 p-0 px-4 no-wrap') \
#             .style('box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1)'):

#         # if menu:
#         #     ui.button(on_click=menu.toggle, icon='menu').props('flat color=white round').classes('lg:hidden')
#         # with ui.link(target='/').classes('row gap-4 items-center no-wrap mr-auto'):
#         #     logo = ui.image(source="webapp/static/logo2.png").classes("w-10 h-10")
#         #     ui.label('Resuable U!').classes(replace='text-lg text-white')

#         # with ui.row().classes('max-[1050px]:hidden'):
#         #     for title_, target in menu_items.items():
#         #         if isinstance(target, dict):  # Check if the item is a dictionary (dropdown)
#         #             with ui.menu().classes('text-lg text-white'):
#         #                 ui.button(title_).props('flat color=white round')
#         #                 for sub_title, sub_target in target.items():
#         #                     ui.menu_item(sub_title, on_click=lambda sub_target=sub_target: ui.navigate.to(sub_target))
               
#         #         else:
#         #             ui.link(title_, target).classes(replace='text-lg text-white')

         