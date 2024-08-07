from nicegui import ui

from . import doc

def on_click(button_submit):
    
    ui.notify("Button clicked")
    button_submit.text = "Clicked"

@doc.demo('Contact Page', '''
    A demo page to show the contact or form section page for a webpage.
''')
def main_demo() -> None:
        ui.page_title('Contact Me')   
        ui.context.client.content.classes('p-0 gap-0')
        with ui.row().classes(
        "flex justify-center items-center w-full h-2/3 gap-0"
        ):
            with ui.column().classes("bg-black w-1/2 p-4 shadow-lg rounded-xl") as col1:
                welcomeLabel = ui.markdown("### Get in touch").classes( 
                    "text-lg font-semibold mx-auto"
                )
                separator = ui.separator().classes("w-2/3 bg-gray-800 mb-4 mx-auto")
                input_name = ui.input(label="Your Name", placeholder="John Doe").classes(
                    "w-full mb-4 px-4 py-2 focus:outline-none focus:border-green-500 rounded-lg"
                )
                input_email = ui.input(
                    label="Your Email", placeholder="example@example.com"
                ).classes(
                    "w-full mb-4 px-4 py-2 focus:outline-none focus:border-green-500 rounded-lg"
                )
                subject = ui.input(label="Subject", placeholder="Subject").classes(
                    "w-full px-4 py-2 focus:outline-none focus:border-green-500 rounded-lg"
                )
                textarea_message = ui.textarea(label="Your Message").classes(
                    "w-full mb-4 px-4 py-2 focus:outline-none focus:border-green-500 resize-none h-32 rounded-lg"
                )
                button_submit = ui.button("Send Message", color="blue").classes(
                    "w-full px-4 py-2 bg-blue-500 text-white hover:bg-blue-600 focus:outline-none focus:bg-blue-600 rounded-lg mx-auto"
                )
                button_submit.on_click(lambda: on_click(button_submit))


            with ui.column().classes(
                "bg-blue-400 w-1/3 h-1/2 p-8 shadow-lg text-white"
            ) as col2:
                contactLabel = ui.markdown("### Contact Me").classes(
                    "text-lg font-semibold mb-4"
                )
                separator = ui.separator().classes("w-2/3 bg-white mb-4")
                with ui.row().classes("flex items-center mb-4"):
                    icon = ui.icon("phone").classes("text-5xl text-blue-500 mr-4")
                    phoneLabel = ui.label("Phone : +1 234 567 890").classes("text-lg")
                with ui.row().classes("flex items-center mb-4"):
                    icon = ui.icon("email").classes("text-5xl text-blue-500 mr-4")
                    emailLabel = ui.label("Email : example@email.com").classes("text-lg")
                with ui.row().classes("flex items-center mb-4"):
                    icon = (
                        ui.icon("o_home")
                        .classes("text-4xl text-blue-500 mr-4")
                        .classes("ml-1")
                    )
                    locationLabel = ui.label("Loc : 123 Street, City, Country").classes(
                        "text-lg"
                    )
                    





