from nicegui import app, ui

def add_footer()-> None:
   with ui.footer(fixed=False).classes("flex justify-around items-start w-full bg-gray-800 text-white py-8").style("margin-top:60px"):
    with ui.grid(columns=4).classes():
     with ui.column().classes("flex flex-col  px-16 space-y-2"):
        with ui.row().classes("flex items-center "):
            ui.image(source="webapp/static/logo2.png").classes("w-8 h-8")  
            ui.label("Reusable U!").classes("font-bold text-lg ")
        ui.label("Designed and built with all the love in the world by the Reusablw U! team with the help of our contributors.")
        ui.label("Code licensed MIT, docs CC BY 3.0.")
        ui.label("Currently v5.0.2.")
        ui.label("Analytics by Fathom.")
    
     with ui.column().classes("flex flex-col  px-16 space-y-2"):
        ui.label("Links").classes("font-bold text-lg mb-2")
        ui.link("Home", "#")
        ui.link("Docs", "#")
        ui.link("Examples", "#")
        ui.link("Themes", "#")
        ui.link("Blog", "#")
        ui.link("Swag Store", "#")
    
     with ui.column().classes("flex flex-col  px-16 space-y-2"):
        ui.label("Guides").classes("font-bold text-lg mb-2")
        ui.link("Getting started", "#")
        ui.link("Starter template", "#")
        ui.link("Webpack", "#")
        ui.link("Parcel", "#")

     with ui.column().classes("flex flex-col  px-16 space-y-2"):
        ui.label("Guides").classes("font-bold text-lg mb-2")
        ui.link("Getting started", "#")
        ui.link("Starter template", "#")
        ui.link("Webpack", "#")
        ui.link("Parcel", "#")   
 
    

                   
