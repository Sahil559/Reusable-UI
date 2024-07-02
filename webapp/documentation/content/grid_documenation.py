from nicegui import ui, app
from . import doc


@doc.demo('Grid Recipe Page', '''
    A demo page to show the use of grid for recipe page .
''')
def content():
  ui.context.client.content.classes('p-0 gap-0')
  with ui.row().classes("w-full h-full").style('background: linear-gradient(to right, #244855, #2C2E3A);'):
   
    recipes = [
        {
            "image": "https://source.unsplash.com/random/200x200?pizza",
            "title": "Pizza",
            "description": "A delicious homemade pizza recipe with a crispy crust and customizable toppings.",
            "button_text": "View Recipe",
            "link": "/recipe/pizza"
        },
        {
            "image": "https://source.unsplash.com/random/200x200?pasta",
            "title": "Pasta",
            "description": "An easy pasta recipe with a savory sauce and fresh herbs. Perfect for a quick dinner.",
            "button_text": "View Recipe",
            "link": "/recipe/pasta"
        },
        {
            "image": "https://source.unsplash.com/random/200x200?salad",
            "title": "Salad",
            "description": "A classic Caesar salad with fresh lettuce, homemade dressing, and crunchy croutons.",
            "button_text": "View Recipe",
            "link": "/recipe/salad"
        },
        {
            "image": "https://source.unsplash.com/random/200x200?burger",
            "title": "Burger",
            "description": "A juicy burger recipe with all the classic toppings, perfect for a summer BBQ.",
            "button_text": "View Recipe",
            "link": "/recipe/burger"
        },
        {
            "image": "https://source.unsplash.com/random/200x200?cake",
            "title": "Chocolate Cake",
            "description": "A rich and moist chocolate cake recipe that is sure to satisfy your sweet tooth.",
            "button_text": "View Recipe",
            "link": "/recipe/cake"
        },
        {
            "image": "https://source.unsplash.com/random/200x200?icecream",
            "title": "Ice Cream",
            "description": "A creamy and delicious homemade ice cream recipe with your choice of flavors.",
            "button_text": "View Recipe",
            "link": "/recipe/icecream"
        }
    ]

    ui.markdown('''###Recipie Page''').classes("text-lg font-bold text-center").style("margin: 40px; margin-left: 460px; margin-bottom: 5px")
    with ui.grid(columns=3).classes().style("margin: 40px; gap: 60px;"):
        for recipe in recipes:
            with ui.card().tight().classes("border rounded-lg shadow-md card-plus").style('background-color: #fff; color: #000;'):
                ui.image(source=recipe["image"]).classes("w-full h-[150px] object-cover")
                with ui.card_section():
                    ui.label(recipe["title"]).classes("text-lg font-semibold text-center")
                    ui.label(recipe["description"]).classes("text-sm text-center")
                    ui.button(recipe["button_text"], on_click=lambda e, link=recipe["link"]: ui.navigate.to(link)).classes("bg-gray-200 hover:bg-gray-300 text-black font-bold py-2 px-4 mt-4")
