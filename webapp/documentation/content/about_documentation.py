from nicegui import ui
from . import doc


@doc.demo('About Page', '''
    A demo page to show the about section page for a webpage.
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

