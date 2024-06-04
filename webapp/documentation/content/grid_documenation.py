from nicegui import ui, app
from . import doc


@doc.demo('Grid Recipie Page', '''
    To use a photo as an avatar, you can use `ui.image` within `ui.avatar`.
''')
def content():
  ui.context.client.content.classes('p-0 gap-0')
  with ui.row().classes("w-full h-[100vh]")\
        .style('background: linear-gradient(to right, #244855, #2C2E3A);'):

    with ui.grid(columns=4).classes().style("margin-left:80px; margin-top:80px;"):

        with ui.column().classes("card-container1").style("margin-right:80px") as col_1:
          with ui.row().classes("flex flex-col"):  
            with ui.card().tight().classes(
                    "border rounded-lg shadow-md card-plus flex flex-col justify-center items-center pt-6"
            )\
                    .style('background-color: #3D52A0; color: #ffffff;') as card1:
                ui.image(source="https://source.unsplash.com/random/200x200?pizza").classes("w-1/2")
                with ui.card_section():
                    ui.label("Pizza").classes(
                        "text-lg font-semibold text-center w-[120px]"
                    )
                with ui.card_section().classes(""):
                    ui.button(
                        "View Recipe",
                        on_click=lambda e: ui.navigate.to('/recipe/pizza'),

                    ).classes(
                        "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4"
                    )

            with ui.card().tight().classes(
                    "border rounded-lg shadow-md card-plus flex flex-col justify-center items-center pt-6"
            )\
                    .style('background-color: #3D52A0; color: #ffffff;') as card1:
                ui.image(source="https://source.unsplash.com/random/200x200?pizza").classes("w-1/2")
                with ui.card_section():
                    ui.label("Pizza").classes(
                        "text-lg font-semibold text-center w-[120px]"
                    )
                with ui.card_section().classes(""):
                    ui.button(
                        "View Recipe",
                        on_click=lambda e: ui.navigate.to('/recipe/pizza'),

                    ).classes(
                        "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4"
                    )

        with ui.column().classes("card-container1").style("margin-right:80px") as col_1:
          with ui.row().classes("flex flex-col"):  
            with ui.card().tight().classes(
                    "border rounded-lg shadow-md card-plus flex flex-col justify-center items-center pt-6"
            )\
                    .style('background-color: #3D52A0; color: #ffffff;') as card1:
                ui.image(source="https://source.unsplash.com/random/200x200?pizza").classes("w-1/2")
                with ui.card_section():
                    ui.label("Pizza").classes(
                        "text-lg font-semibold text-center w-[120px]"
                    )
                with ui.card_section().classes(""):
                    ui.button(
                        "View Recipe",
                        on_click=lambda e: ui.navigate.to('/recipe/pizza'),

                    ).classes(
                        "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4"
                    )

            with ui.card().tight().classes(
                    "border rounded-lg shadow-md card-plus flex flex-col justify-center items-center pt-6"
            )\
                    .style('background-color: #3D52A0; color: #ffffff;') as card1:
                ui.image(source="https://source.unsplash.com/random/200x200?pizza").classes("w-1/2")
                with ui.card_section():
                    ui.label("Pizza").classes(
                        "text-lg font-semibold text-center w-[120px]"
                    )
                with ui.card_section().classes(""):
                    ui.button(
                        "View Recipe",
                        on_click=lambda e: ui.navigate.to('/recipe/pizza'),

                    ).classes(
                        "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4"
                    )

        with ui.column().classes("card-container3") as col_3:
          with ui.row().classes("flex flex-col"):  
            with ui.card().tight().classes(
                    "border rounded-lg shadow-md card-plus flex flex-col justify-center items-center pt-6"
            )\
                    .style('background-color: #3D52A0; color: #ffffff;') as card3:
                ui.image(source="https://source.unsplash.com/random/200x200?pasta").classes("w-1/2")
                with ui.card_section():
                    ui.label("Pasta").classes(
                        "text-lg font-semibold w-[120px] text-center"
                    )
                with ui.card_section().classes(""):
                    ui.button(
                        "View Recipe",
                        on_click=lambda e: ui.navigate.to('/recipe/pasta'),
                    ).classes(
                        "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4"
                    )

            with ui.card().tight().classes(
                    "border rounded-lg shadow-md card-plus flex flex-col justify-center items-center pt-6"
            )\
                    .style('background-color: #3D52A0; color: #ffffff;') as card1:
                ui.image(source="https://source.unsplash.com/random/200x200?pizza").classes("w-1/2")
                with ui.card_section():
                    ui.label("Pizza").classes(
                        "text-lg font-semibold text-center w-[120px]"
                    )
                with ui.card_section().classes(""):
                    ui.button(
                        "View Recipe",
                        on_click=lambda e: ui.navigate.to('/recipe/pizza'),

                    ).classes(
                        "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4"
                    )