import webbrowser
import flet
from flet import AppBar, IconButton ,FilledTonalButton, Page, Text, View, colors, Image, Container, Row, Column, alignment, CircleAvatar, icons, GestureDetector
import webbrowser
from helper import *

def main(page: Page):
    page.title = "Home"
    
    print("Initial route:", page.route)
    

    def route_change(e):
        page.fonts={"Montserrat-Light": "/Fonts/Montserrat-Light.tff",
                    "Montserrat-Bold": "/Fonts/Montserrat-Bold.ttf",
                    "Montserrat-Medium": "/Fonts/Montserrat-Medium.tff",
                    "Montserrat-Regular": "/Fonts/Montserrat-Regular.tff"}

        print("Route change:", e.route)
        page.views.clear()

        navigation_buttons = Row(
                            [
                            Container(
                                content = FilledTonalButton("Projects", on_click=open_projects),
                                alignment=alignment.center,
                                width=120,
                                height=20,
                            ),
                            Container(
                                content=FilledTonalButton("Experience", on_click=open_experience),
                                alignment=alignment.center,
                                width=120,
                                height=20,
                            ),
                            ],
                            alignment="center",
                            )
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Sion Avakian", font_family="Montserrat-Regular", color = colors.WHITE, size = 40), actions=[navigation_buttons], center_title=True, bgcolor=colors.BLUE_GREY_900),
                    # Container(content=Text("Sion Avakian", size=50, font_family="Montserrat-Regular",color=colors.WHITE),alignment=alignment.center),
                    Column(
                    [
                        Column(
                            [
                                Container(content=CircleAvatar(foreground_image_url="Images/headshot.jpg", content=Text("FF"), width=200, height=200),alignment=alignment.center,padding=20),
                                Container(content=Text("Software Engineer and Computer Science Enthusiast", size=25, font_family="Montserrat-Light",color=colors.WHITE),alignment=alignment.center,padding=20),
                            ],
                        ),
                        Row(
                            [   
                                # IconButton(on_click=open_github, icon=icons.CONTACT_PAGE),
                                # IconButton(icon=icons.GITE, on_click=open_linkedin),
                                GestureDetector(
                                    on_tap = open_github,
                                    content=Image(src="icons/github.png",width=50, height=50)
                                ),
                                GestureDetector(
                                    on_tap = open_linkedin,
                                    content=Image(src="icons/linkedin.png",width=50, height=50)
                                )
                            ],alignment="center",
                        )
                    ]

                    )
                ],
            bgcolor=colors.BLUE_GREY,
            scroll="always",

            ),

        )

        # if page.route == "/About":
        #     page.views.append(
        #         View(
        #             "/About",
        #             [
        #                 AppBar(title=Text("About", color=colors.RED_200), bgcolor=colors.LIGHT_BLUE_700),
        #                 Text("About Page!", style="bodyMedium"),
        #             ],
        #         scroll="always",
        #         bgcolor=colors.RED
        #         )
        #     )

        if page.route == "/Projects":
            page.views.append(
                View(
                    "/Projects",
                    [
                        AppBar(title=Text("Projects"), bgcolor=colors.BLUE_GREY_900),
                        Text("Projects Page!", style="bodyMedium"),
                    ],
                scroll="always",
                bgcolor=colors.YELLOW_ACCENT_200

                
                )
            )
        if page.route == "/Experience":
            experience_images = Row(expand=1, wrap=False, scroll="always")
            experience_images.controls.append(general_motors_logo)
            experience_images.controls.append(capgemini_logo)
            experience_images.controls.append(NSF_logo)
            experience_images.controls.append(UCI_logo)
            
            page.views.append(
                View(
                    "/Experience",
                    [
                        AppBar(title=Text("Experience"), bgcolor=colors.SURFACE_VARIANT),
                        Row([experience_images])

                    ],
                bgcolor=colors.BLUE_GREY,
                scroll="always",
                padding=50
                )
            )

        page.update()


    def view_pop(e):
        print("View pop:", e.view)
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    def open_projects(e):
        page.go("/Projects")

    def open_experience(e):
        page.go("/Experience")

    def open_github(e):
        print("Go to Github")
        webbrowser.open_new_tab('https://github.com/avakianssion')


    def open_linkedin(e):
        print("Go to LinkedIn")
        webbrowser.open_new_tab("https://www.linkedin.com/in/sion-avakian/")


    page.go(page.route)

flet.app(
    target=main, view=flet.WEB_BROWSER,
    assets_dir="assets" 
    )
