from nicegui import app, ui

def add_footer()-> None:
   with ui.footer(fixed=False).classes("flex justify-around items-start w-full bg-gray-800 text-white py-8").style("margin-top:60px"):
    with ui.grid(columns=4).classes():
     with ui.column().classes("flex flex-col  px-16 space-y-2"):
        with ui.row().classes("flex items-center "):
            ui.image(source="webapp/static/logo2.png").classes("w-8 h-8")  
            ui.label("Reusable U!").classes("font-bold text-lg ")
        ui.label("Designed and built with all the love by the Reusablw U!.")
        
    
     with ui.column().classes("flex flex-col  px-16 space-y-2"):
        ui.label("Links").classes("font-bold text-lg mb-2")
        ui.link("Home", "#")
        ui.link("Features", "/#features")
        ui.link("Login", "/login")
        ui.link("About", "/#why")
        
    
     with ui.column().classes("flex flex-col  px-16 space-y-2"):
        ui.label("Demos").classes("font-bold text-lg mb-2")
        ui.link("Grid Recipe Page", "/documentation/section_page_layout#grid_recipe_page")
        ui.link("About Page", "/documentation/section_page_layout#about_page")
        ui.link("Contact Page", "/documentation/section_page_layout#contact_page")
        ui.link("Tech Stack Page", "/documentation/section_page_layout#tech_stack_page")

     with ui.column().classes("flex flex-col  px-16 space-y-2"):
        ui.label("Documentation").classes("font-bold text-lg mb-2")
        ui.link("Page Layout", "/documentation/section_page_layout")
        ui.link("Elements", "/documentation/section_element")
        ui.link("Navigations", "/documentation/section_navigations")
        ui.link("Input Area", "/documentation/section_input_area")   
 
    

                   
