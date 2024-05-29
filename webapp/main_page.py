from nicegui import ui

from .header import add_head_html, add_header
from .style import features, heading, link_target, section_heading
from . import documentation
from webapp.footer import add_footer

def create() -> None:
    """Create the content of the main page."""
    ui.context.client.content.classes('p-0 gap-0')
    add_head_html()
    add_header()

    with ui.row().classes("w-full h-[110vh]")\
            .style('box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); background-color: #5579C6; color: #ffffff;'):
        
     with ui.grid(columns=2).classes():
        with ui.column().classes('gap-4 md:gap-8 pt-32').style('margin-left: 60px;') :
            ui.image(source="webapp/static/logo2.png").style("width: 40%; height:100%; margin-left: 160px;")
            ui.html("<h1 class='text-6xl font-bold text-white text-left pl-8 pt-2 pr-8'>Crafts Seamlessly<br> with Resuable U!</h1>")
            ui.html("<p class='text-white text-left pl-9'>Build Any Component Any Time.</p>") \
                .classes('max-w-[10rem] sm:max-w-[24rem] md:max-w-[30rem]')


        with ui.column().classes("mt-[7%] ml-[35%]") as col2:
                with ui.grid(columns=2).classes().style("margin-left:40px; margin-top:40px"):
                    with ui.column().classes("card-container1") as col_2_1:
                        with ui.row().classes("flex flex-col"):
                            with ui.card().tight().classes(
                                "border rounded-lg shadow-md card-plus flex flex-col justify-center items-center pt-6"
                            )\
                            .style('background-color: #1260CC; color: #ffffff;') as card1:
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

                            with ui.card().tight().classes(
                                "border rounded-lg shadow-md card-plus flex flex-col justify-center items-center pt-6"
                            )\
                            .style('background-color: #1260CC; color: #ffffff;') as card2:
                                ui.image(source="webapp/static/ns.png").classes("w-1/2")
                                with ui.card_section():
                                    ui.label("Navigation").classes(
                                        "text-lg font-semibold text-center"
                                    )
                                with ui.card_section().classes(""):
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
                            .style('background-color: #1260CC; color: #ffffff;') as card3:
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
                            .style('background-color: #1260CC; color: #ffffff;') as card4:
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
                                        "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                                    )  



    with ui.column().classes('w-full p-8 lg:p-16 bold-links arrow-links max-w-[1600px] mx-auto')\
            .style('box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); background-color: #1768AC; color: #ffffff;'):
     link_target('features', '-50px')
     heading('Features')
     with ui.row().classes('w-full text-lg leading-tight grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-3 gap-8'):
        with ui.column():
            features('anchor', 'Modularity', [
                'Highlight the modularity of your UI components, emphasizing how they are designed to be independent and can be easily reused across different parts of your web application. Users can mix and match these components to create custom layouts and interfaces tailored to their needs.',
            ])
        with ui.column():
            features('brush', 'Customization', [
                'Discuss the flexibility of your UI components, showcasing how users can customize their appearance, behavior, and functionality according to specific project requirements. This could include options for styling, theming, and configuration settings.',
            ])
        with ui.column():
            features('insights', 'Accessibility', [
                'Emphasize the accessibility features built into your UI components, ensuring that they meet WCAG (Web Content Accessibility Guidelines) standards and are inclusive to all users, including those with disabilities. Highlight any features such as keyboard navigation support, screen reader compatibility, and semantic HTML structure.',
            ])
        with ui.column():
            features('swap_horiz', 'Responsive Design', [
                'Showcase how your UI components are designed to be responsive, meaning they adapt and display appropriately across various devices and screen sizes. Whether it\'s desktops, tablets, or smartphones, users can expect consistent and optimized experiences.',
            ])
        with ui.column():
            features('source', 'Cross-Browser Compatibility', [
                'Assure users that your UI components are tested and compatible with a wide range of web browsers, including popular ones such as Chrome, Firefox, Safari, and Edge. This ensures a consistent experience regardless of the browser used by the end-user.',
            ])
        with ui.column():
            features('space_dashboard', 'Documentation and Support', [
                'Highlight the availability of comprehensive documentation and support resources for your UI components. Provide links to guides, tutorials, API references, and community forums where users can find help, report issues, and collaborate with others using the components.',
            ])


    with ui.column().classes('w-full p-8 lg:p-16 max-w-[1600px] mx-auto')\
            .style('box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); background-color: #5579C6; color: #ffffff;'):
        link_target('demos', '-50px')
        heading('Demos')
        with ui.column().classes('w-full'):
            documentation.create_intro()
        with ui.column().classes('gap-1 max-lg:items-center max-lg:text-center'):
                ui.markdown('Browse through plenty of live demos.') \
                    .classes('text-white text-2xl md:text-3xl font-medium')
                ui.link('Documentation', '/documentation').style('color: black !important') \
                .classes('rounded-full mx-auto px-12 py-2 bg-white font-medium text-lg md:text-xl')    



    with ui.row().classes('w-full p-8 lg:p-16 bold-links arrow-links max-w-[1600px] mx-auto')\
            .style('box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); background-color: #1768AC; color: #ffffff;'):
        link_target('why')
        with ui.column().classes('''
                max-w-[1600px] m-auto
                py-20 px-8 lg:px-16
                items-center justify-center no-wrap flex-col md:flex-row gap-16
            '''):
            with ui.column().classes('gap-8'):
                heading('Why Reusable UI?')
                with ui.column().classes('gap-2 text-xl text-white bold-links arrow-links'):
                    ui.markdown('''
                        "Resuable UI" is a comprehensive project aimed at providing developers with a robust toolkit for creating elegant and consistent user interfaces effortlessly. 
                                Each component is thoughtfully designed to seamlessly integrate into any project, whether it be a simple webpage or a complex web application. 
                                With Resuable UI, developers can streamline their workflow, reduce redundancy, and focus on what truly matters: delivering exceptional user experiences.
                    ''')
                    ui.markdown('''
                        Resuable UI is your go-to solution for building beautiful, cohesive interfaces with ease. 
                                Experience the power of reusability with Resuable UI, and unlock a new era of web development possibilities.
                    ''')

    add_footer()