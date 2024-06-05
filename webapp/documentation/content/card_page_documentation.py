from nicegui import ui
from . import doc



def create_card(icon, text):
    with ui.card().tight().classes("cardLang hover:bg-blue-200") as card:
        with ui.row().classes("flex justify-center items-center") as row:
            ui.image(source=f"assets/{icon}").classes("w-1/2 p-6")
            # ui.label(text).classes("text-xs font-semibold text-black text-center")



def content() -> None:
    ui.page_title("Home")
    ui.context.client.content.classes("p-0 gap-0")
   
    ui.add_css(
        """
            .cardLang{
                background-color: #fff;  
                border: #000 2px solid;
                margin: 1rem;
                padding: 3rem;
                border-radius: 10px;
            }
            
            .cardlang img{
                width: 100px;
                padding: 1rem;
            }
            
            .card-plus {
                width: 150px;
                height: 250px;
            }
            
            body {
                margin: 0;
                padding: 0;
                width: 100%;
            }

            textarea{
                resize: none;

            }

            .card-plus {
                max-width: 200px;
                max-height: 300px;
            }

            .card-plus img {
                width: 100%;
                height: auto;
                
            }

            .usul {
                margin-left: -14px;
            }

            #c31 {
                margin-left: -16px;
            }

            .col1_sec{
                margin-left: 10%;
                margin-top: 3%;
            }

            .col2_sec{
                margin-top: 3%;
            }


            .img1 {
                width: 500px;
                height: 500px;
            }

            .first_section{
                margin-left: 7%;
                margin-top: 6%; 
            }

            .card-plus1 {
                background-color: white;
            }

            .set_navbar_el_black{
                color: #000;
            }

            .set_navbar_hr_black{
                border-top: 1px solid #000;
            }

            .text-white1{
                color: #fff;
            }

            .screen-section{
                padding-left: 80%;
            }
            
            .img-spe{
                width: 300px;
                height: 350px;
            }
            
            /*.maxSize{
                max-width: 200px;
            }*/
            
            """
    )

    with ui.row().classes(
        """
        h-screen bg-gray-800 w-full"""
    ):
        ui.label("Mes technologies actuelles").classes(
            "text-5xl font-bold text-white w-full text-center mt-8"
        )
        ui.separator().classes("bg-white h-0.5 w-1/4 mx-auto mb-4")

        with ui.row().classes("flex justify-center items-center mb-2") as row2:
            create_card("windows.png", "Windows")
            create_card("python.png", "Python")
            create_card("cpp.png", "C++")
            create_card("c.png", "C")
            create_card("java.png", "Java")
            create_card("django.png", "Django")
            create_card("node.png", "Node.js")
            create_card("react.png", "React")
            create_card("js.png", "Javascript")
            



