from nicegui import ui
from . import doc


@doc.demo('Profile page', '''
    A demo page to show the profile page for a webpage using cards.
''')
def main_demo() -> None:
    ui.page_title("Home")
    ui.context.client.content.classes("p-0 gap-0")
   
    with ui.row().classes(
        "w-full h-2/3 bg-blue-500 text-white flex justify-center section2"
    ):
        with ui.column().classes(
            "bg-blue-500 w-full p-4 text-white text-center mb-10"
        ) as col1:
            ui.label("Who am I ?").classes(
                "text-center text-5xl font-bold w-full mb-2 mt-2"
            )
            ui.label(
                """I am a young person interested in computer science who would like to combine my passions with the field of innovative 
                technology, such as aeronautics and space, banking, research, and others. I am a jack-of-all-trades, I love learning, and
                  I enjoy understanding how things work. I have four predominant areas of interest which are as follows:
                    """
            )
            with ui.column().classes(
                "w-full flex justify-center items-center"
            ) as container:
                with ui.row().classes("w-full flex justify-center items-center") as row:
                    with ui.card().tight().classes("card-plus1 bg-white") as card1:
                        with ui.card_section():
                            with ui.row().classes("") as row:
                                ui.icon("done").classes(
                                    "text-5xl bg-blue-500 text-white rounded-full mr-4"
                                )

                                with ui.column().classes(""):
                                    ui.label("Python").classes(
                                        " font-semibold text-black"
                                    )
                                    ui.label(
                                        "For simplicity and its community"
                                    ).classes("text-black")

                    with ui.column().classes(""):
                        with ui.card().tight().classes("card-plus1 bg-white") as card2:
                            with ui.card_section():
                                with ui.row().classes("") as row:
                                    ui.icon("done").classes(
                                        "text-5xl bg-blue-500 text-white rounded-full mr-4"
                                    )

                                    with ui.column().classes(""):
                                        ui.label("C++").classes(
                                            " font-semibold text-black"
                                        )
                                        ui.label(
                                            "For performance and architecture"
                                        ).classes("text-black")

                with ui.row().classes(""):
                    with ui.card().tight().classes("card-plus1 bg-white") as card3:
                        with ui.card_section():
                            with ui.row().classes("") as row:
                                ui.icon("done").classes(
                                    "text-5xl bg-blue-500 text-white rounded-full mr-4"
                                )

                                with ui.column().classes(""):
                                    ui.label("Aeronautics").classes(
                                        " font-semibold text-black"
                                    )
                                    ui.label(
                                        "It's a passion that is close to my heart"
                                    ).classes("text-black")
                    with ui.column().classes(""):
                        with ui.card().tight().classes("card-plus1 bg-white") as card4:
                            with ui.card_section():
                                with ui.row().classes("") as row:
                                    ui.icon("done").classes(
                                        "text-5xl bg-blue-500 text-white rounded-full mr-4"
                                    )

                                    with ui.column().classes(""):
                                        ui.label("Computer Science").classes(
                                            " font-semibold text-black"
                                        )
                                        ui.label(
                                            "I want to make it my profession in the future"
                                        ).classes("text-black")


 


