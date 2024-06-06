from nicegui import ui,app

from .header import add_head_html, add_header
from .style import features, heading, link_target, section_heading
from . import documentation
from webapp.footer import add_footer



def create() -> None:
    """Create the content of the main page."""
    ui.context.client.content.classes('p-0 gap-0')
    STYLE='''
    
        .card-container1 .card-plus,
        .card-container2 .card-plus {
            transition: transform 0.5s ease-in-out, box-shadow 0.3s ease-in-out, background-color 0.3s ease-in-out;
            border-radius: 12px;
        }

        .card-container1 .card-plus:hover,
        .card-container2 .card-plus:hover {
            transform: translateY(-10px) scale(1.05);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
            background-color: #2C3E50; /* Slightly darker background color on hover */
        }
        .logo-card {
            transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
            border-radius: 40px;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 0px;
            background-color: #ffffff;
        }
        .logo-card:hover {
            transform: scale(1.1);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
        }
    '''
    ui.add_css(STYLE)
    add_head_html()
    add_header()
    
    with ui.row().classes("w-full h-[90vh]")\
    .style('background: linear-gradient(to right, #3D52A0, #244855, #2C2E3A, #244855 ); color: #ffffff;'):
      with ui.grid().style("display: grid; grid-template-columns: 2fr 1fr; width: 100%;"):
        with ui.column().classes(' gap-4 md:gap-8 pt-32').style('margin-left:50px;margin-top:5px') :
            with ui.row().style("display: flex; justify-content: center; width: 100%; margin-bottom: -20px;"):
                    with ui.card().classes('logo-card').style("width: 15%; height: auto;"):
                        ui.image(source="webapp/static/logo2.png").style("width: 100%; height: auto;")
            with ui.row().style("display: flex; justify-content: center; width: 100%; margin-bottom: -20px;"):  
              ui.html("<h1 class='text-6xl font-bold text-white text-left  pl-8 pt-2 pr-8' style='letter-spacing: 0.025em'>Crafts Seamless Experience<br><center> with Resuable U!</center></h1>")
            with ui.row().style("display: flex; justify-content: center; width: 100%;"):  
              ui.html("<h2 class='text-2xl text-white text-left pl-8 pt-2 pr-8'>Build beautiful UIs effortlessly with our intuitive GUI components.</h2>")
            with ui.row().style("display: flex; justify-content: center; width: 100%;  margin-top: -10px;"):  
              ui.html("<h2 class='text-2xl text-white text-left pl-2 pt-2 pr-0'>Jump right into building</h2>")
              ui.button("Read Docs",icon='book',color=None ,on_click=lambda e: ui.navigate.to(
                                           '/documentation'),
                                    ).classes(
                                        "bg-blue-600 hover:bg-blue-500 text-white font-bold py-2 px-4 "
                                    ).style(
                    "font-size: 18px; padding: 10px 20px margin-left: 40px;"
                )
            with ui.row().classes('gap-2 bold-links arrow-links text-lg').style("display: flex; justify-content: center; width: 100%;  margin-top: -10px;"):  
              ui.markdown('''
                    #####Available on [GitHub](https://github.com/Sahil559/Reusable-UI)
                ''')


        with ui.column().classes("mt-[7%] ml-[15%]") as col2:
                with ui.grid(columns=2).classes().style(" margin-top:40px"):
                    with ui.column().classes("card-container1") as col_2_1:
                        with ui.row().classes("flex flex-col"):
                            with ui.card().tight().classes(
                                "border rounded-lg shadow-md card-plus flex flex-col justify-center items-center pt-6"
                            )\
                            .style('background-color: #3D52A0; color: #ffffff;') as card1:
                                ui.image(source="webapp/static/PG.png").classes("w-1/2")
                                with ui.card_section():
                                    ui.label("Page Section").classes(
                                        "text-lg font-semibold text-center w-[120px]"
                                    )
                                with ui.card_section().classes(""):
                                    ui.button(
                                        "Try now",
                                        on_click=lambda e: ui.navigate.to('/documentation/section_page_layout'
                                        ),
                                    ).classes(
                                        "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4"
                                    )

                            with ui.card().classes(
                                "border rounded-lg shadow-md card-plus flex flex-col justify-center items-center pt-6"
                            )\
                            .style('background-color: #3D52A0; color: #ffffff;') as card2:
                                ui.image(source="webapp/static/ns.png").classes("w-2/3")
                                with ui.card_section():
                                    ui.label("Navigation").classes(
                                        "text-lg font-semibold text-center"
                                    )
                                with ui.card_section().classes("").style('margin-top: -30px'):
                                    ui.button(
                                        "Try now",
                                        on_click=lambda e: ui.navigate.to(
                                            '/documentation/section_navigations'
                                        ),
                                    ).classes(
                                        "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4"
                                    )
                    with ui.column().classes("card-container2") as col_2_2:
                        with ui.row().classes("flex flex-col"):
                            with ui.card().tight().classes(
                                "border rounded-lg shadow-md card-plus flex flex-col justify-center items-center pt-6"
                            )\
                            .style('background-color: #3D52A0; color: #ffffff;') as card3:
                                ui.image(source="webapp/static/ia.png").classes("w-1/2")
                                with ui.card_section():
                                    ui.label("Input Area").classes(
                                        "text-lg font-semibold w-[120px] text-center"
                                    )
                                with ui.card_section().classes(""):
                                    ui.button(
                                        "Try now",
                                        on_click=lambda e: ui.navigate.to(
                                            '/documentation/section_input_area'
                                        ),
                                    ).classes(
                                        "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4"
                                    )

                            with ui.card().tight().classes(
                                "border rounded-lg shadow-md card-plus flex flex-col justify-center items-center pt-6"
                            )\
                            .style('background-color: #3D52A0; color: #ffffff;') as card4:
                                ui.image(source="webapp/static/es.jpg").classes("w-1/2")
                                with ui.card_section():
                                    ui.label("Elements").classes(
                                        "text-lg font-semibold w-[120px] text-center"
                                    )
                                with ui.card_section().classes():
                                    ui.button(
                                        "Try now",
                                        on_click=lambda e: ui.navigate.to(
                                           '/documentation/section_element'),
                                    ).classes(
                                        "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 "
                                    )  


# Feature Section
    features_list = [
    ('anchor', 'Modularity', 'Highlight the modularity of your UI components, emphasizing how they are designed to be independent and can be easily reused across different parts of your web application. Users can mix and match these components to create custom layouts and interfaces tailored to their needs.'),
    ('brush', 'Customization', 'Discuss the flexibility of your UI components, showcasing how users can customize their appearance, behavior, and functionality according to specific project requirements. This could include options for styling, theming, and configuration settings.'),
    ('insights', 'Accessibility', 'Emphasize the accessibility features built into your UI components, ensuring that they meet WCAG (Web Content Accessibility Guidelines) standards and are inclusive to all users, including those with disabilities. Highlight any features such as keyboard navigation support, screen reader compatibility, and semantic HTML structure.'),
    ('swap_horiz', 'Responsive Design', 'Showcase how your UI components are designed to be responsive, meaning they adapt and display appropriately across various devices and screen sizes. Whether it\'s desktops, tablets, or smartphones, users can expect consistent and optimized experiences.'),
    ('source', 'Cross-Browser Compatibility', 'Assure users that your UI components are tested and compatible with a wide range of web browsers, including popular ones such as Chrome, Firefox, Safari, and Edge. This ensures a consistent experience regardless of the browser used by the end-user.'),
    ('space_dashboard', 'Documentation and Support', 'Highlight the availability of comprehensive documentation and support resources for your UI components. Provide links to guides, tutorials, API references, and community forums where users can find help, report issues, and collaborate with others using the components.')
    ]


    # JavaScript to enable carousel sliding
    ui.run_javascript("""
      const carousel = document.getElementById('carousel');
      let scrollAmount = 0;
      const scrollMax = carousel.scrollWidth - carousel.clientWidth;

     function scrollLeft() {
        scrollAmount -= carousel.clientWidth / 3;
        if (scrollAmount < 0) scrollAmount = 0;
        carousel.scrollTo({ left: scrollAmount, behavior: 'smooth' });
     }

     function scrollRight() {
        scrollAmount += carousel.clientWidth / 3;
        if (scrollAmount > scrollMax) scrollAmount = scrollMax;
        carousel.scrollTo({ left: scrollAmount, behavior: 'smooth' });
     }

     document.getElementById('left-arrow').addEventListener('click', scrollLeft);
     document.getElementById('right-arrow').addEventListener('click', scrollRight);
    """)

    ui.add_head_html('''
    <style>
        #carousel {
            scroll-behavior: smooth;
            display: flex;
            align-items: center;
        }
        #carousel::-webkit-scrollbar {
            display: none;
        }
        #carousel {
            -ms-overflow-style: none;
            scrollbar-width: none;
        }
        .carousel-btn {
            background-color: rgba(0, 0, 0, 0.5);
            border: none;
            color: white;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .carousel-btn:hover {
            background-color: rgba(0, 0, 0, 0.7);
        }
        .feature-card {
            height: 400px;
            overflow: hidden;
        }
        .feature-card:hover {
            transform: scale(1.05);
            transition: transform 0.3s ease-in-out;
        }
        .feature-card .content {
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        .feature-card .content .description {
            overflow-y: auto;
            max-height: 200px;
        }
    </style>
''')

    def create_feature_card(icon, title, description):
     with ui.card().classes('feature-card flex-shrink-0 w-80 mx- rounded-lg shadow-lg bg-white text-black transition-transform duration-300 ease-in-out'):
        with ui.column().classes('content p-4'):
            ui.icon(icon).classes('text-5xl mb-4 text-blue-500')
            ui.label(title).classes('text-2xl font-bold mb-2 text-gray-800')
            ui.label(description).classes('description text-lg text-gray-600')

    
    # Create the carousel component
    with ui.column().classes('w-full p-8 lg:p-16 bold-links arrow-links max-w-[1600px] mx-auto')\
     .style('background: linear-gradient(to right, #3D52A0, #244855, #2C2E3A, #244855); color: #ffffff; position: relative;'):
     link_target('features', '-50px')
     heading('Features').classes('text-center text-5xl mb-0 text-white').style('font-size: 3rem')
     ui.label('Explore the key features of our application').style('font-size: 1.25rem')
     ui.button('◀').classes('carousel-btn absolute left-2 top-1/2 transform -translate-y-1/2 z-10').props('id="left-arrow"')
     ui.button('▶').classes('carousel-btn absolute right-2 top-1/2 transform -translate-y-1/2 z-10').props('id="right-arrow"')
     with ui.row().classes('overflow-x-auto flex-nowrap w-full py-8 items-center justify-start space-x-12').props('id="carousel"'):
        for icon, title, description in features_list:
            create_feature_card(icon, title, description)



# Demos Section
    with ui.column().classes('w-full p-8 lg:p-16 max-w-[1600px] mx-auto')\
            .style('box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); background-color: #5579C6; color: #ffffff;'):
        link_target('demos', '-50px')
        heading('Demos').style('font-size: 3rem')
        with ui.column().classes('w-full'):
            documentation.create_intro()
        with ui.column().classes('gap-2 bold-links arrow-links text-lg mt-10').style("display: flex; justify-content: center; width: 100%;"):  
              ui.markdown('###Browse through plenty of live [Demos](/documentation).')


# About Section
    with ui.row().classes('w-full p-8 lg:p-5 bold-links arrow-links max-w-[1600px] mx-auto')\
        .style('box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); background-color: #1768AC; color: #ffffff;'):
     link_target('about')
     with ui.column().classes('''
            max-w-[1500px] m-auto
            py-20 px-8 lg:px-16
            items-center justify-between flex-wrap flex-col md:flex-row gap-16
        '''):
        with ui.column().classes('gap-6 flex-1'):
            heading('Why Reusable UI ?').classes('text-center text-5xl mb-8 text-white').style('font-size: 3rem')
            with ui.column().classes('gap-4 text-xl text-white bold-links arrow-links'):
                ui.markdown('''
                    **"Reusable UI"** is a comprehensive project aimed at providing developers with a robust toolkit for creating elegant and consistent user interfaces effortlessly. Each component is thoughtfully designed to seamlessly integrate into any project, whether it be a simple webpage or a complex web application.
                ''')
                ui.markdown('''
                    With **Reusable UI**, developers can streamline their workflow, reduce redundancy, and focus on what truly matters: delivering exceptional user experiences.
                ''')
                ui.markdown('''
                    Experience the power of reusability with **Reusable UI**, and unlock a new era of web development possibilities.
                ''')
        ui.image(source="webapp/static/ux.png").style("width: 30%; height: 60%;")



# footer section
    add_footer()