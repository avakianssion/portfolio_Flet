import webbrowser
import flet
from flet import AppBar, IconButton ,FilledTonalButton, Page, Text, View, colors, Image, Container, Row, Column, alignment, CircleAvatar, icons, GestureDetector, padding
import webbrowser
from helper import *

def main(page: Page):
    page.title = "Home"
    
    print("Initial route:", page.route)
    

    def route_change(e):
        page.fonts={
                    "Inconsolata-Light": "/Fonts/Inconsolata-Light.ttf",
                    "Inconsolata-Medium": "/Fonts/Inconsolata-Medium.ttf",}

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
                    AppBar(title=Text("Sion Avakian", font_family="Inconsolata-Medium", color = colors.WHITE, size = 40), actions=[navigation_buttons], center_title=True, bgcolor=colors.BLUE_GREY_900),
                    # Container(content=Text("Sion Avakian", size=50, font_family="Montserrat-Regular",color=colors.WHITE),alignment=alignment.center),
                    Column(
                    [
                        Column(
                            [
                                Container(content=CircleAvatar(foreground_image_url="Images/headshot.jpg", content=Text("FF"), width=200, height=200),alignment=alignment.center,padding=20),
                                Container(content=Text("Software Engineer and Computer Science Enthusiast", size=25, font_family="Inconsolata-Light",color=colors.WHITE),alignment=alignment.center,padding=20),
                            ],
                        ),
                        Row(
                            [   
                               GestureDetector(
                                    on_tap = open_linkedin,
                                    content=Image(src="icons/linkedin1010.png",width=50, height=50)
                                
                                ),
                                GestureDetector(
                                    on_tap = open_github,
                                    content=Image(src="icons/github.png",width=50, height=50)
                                ),

                            ],alignment="center",
                        )
                    ]

                    )
                ],
            bgcolor=colors.BLUE_GREY,
            scroll="always",
            ),

        )

        if page.route == "/Projects":
            page.views.append(
                View(
                    "/Projects",
                    [
                        AppBar(title=Text("Projects", font_family="Inconsolata-Medium", color = colors.WHITE, size = 40), actions=[navigation_buttons], center_title=True, bgcolor=colors.BLUE_GREY_900),                  
                    
                    Column(
                        [
                                Row(
                                [
                                    GestureDetector
                                    (
                                        on_tap = open_phoenix,
                                        content = Container(content=Phoenix_logo, width=180,height=180)
                                    ),
                                    Text("Phoenix Robotics",font_family="Inconsolata-Light", color = colors.BLUE_900, size = 25)
                                ], alignment="start"
                                ),
                                
                                Row(
                                [
                                    GestureDetector
                                    (
                                        on_tap = open_RSNA,
                                        content = Container(content=RSNA_logo, width=180,height=180)
                                    ),
                                    Text("RSNA Pneumonia Detection",font_family="Inconsolata-Light", color = colors.BLUE_900, size = 25)
                                ],alignment="start"
                                ),
                                Row(
                                [
                                    GestureDetector
                                    (
                                        on_tap = open_mRNA,
                                        content = Container(content=Vaccine_logo, width=180,height=180)
                                    ),
                                    Text("COVID-19 mRNA Vaccine Degradation Prediction",font_family="Inconsolata-Light", color = colors.BLUE_900, size = 25)
                                    
                                ],alignment="start"
                                ),
                        ],alignment="center",
                    ),
                    ],
                bgcolor=colors.ORANGE_200,
                scroll="always",
                padding=100
                )
            )
        if page.route == "/Experience":
            page.views.append(
                View(
                    "/Experience",
                    [
                        AppBar(title=Text("Experience", font_family="Inconsolata-Medium", color = colors.WHITE, size = 40), actions=[navigation_buttons], center_title=True, bgcolor=colors.BLUE_GREY_900),                  
                    Column(
                    [
                        Column(
                            [
                                   Row(
                                    [
                                        Container(content=general_motors_logo, width=180,height=180),
                                        Text("Working on Ultifi Platforms for Autonomous and Electric Vehciles",font_family="Inconsolata-Light", color = colors.BLUE_900, size = 25)
                                    ], alignment="start"),
                                   
                                   Row(
                                    [
                                        Container(content=capgemini_logo, width=180,height=180),
                                        Text("Worked on internal communication hub system",font_family="Inconsolata-Light", color = colors.BLUE_900, size = 25)
                                    ],alignment="start"),
                                   Row(
                                    [
                                        Container(content=NSF_logo, width=180,height=180),
                                        Text("Research project on online mis-information",font_family="Inconsolata-Light", color = colors.BLUE_900, size = 25)
                                     
                                    ],alignment="start"),
                                   Row(
                                    [
                                        Container(content=UCI_logo, width=180,height=180),
                                        Text("Rsearch project on the use of data science in community organizations",font_family="Inconsolata-Light", color = colors.BLUE_900, size = 25) 
                                    ],
                                    alignment="start"),
                            ],
                        ),

                    ]
                    )
                    ],
                bgcolor=colors.ORANGE_200,
                scroll="always",
                padding=100
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

    def open_phoenix(e):
        print("Go to Phoenix")
        webbrowser.open_new_tab("https://twitter.com/phoenixrobotics?lang=en")

    def open_RSNA(e):
        print("Go to RSNA")
        webbrowser.open_new_tab("https://github.com/avakianssion/RSNA-Pneumonia-Detection-Challenge")

    def open_mRNA(e):
        print("Go to mRNA")
        webbrowser.open_new_tab("https://github.com/avakianssion/COVID-19-mRNA-Vaccine-Degradation-Prediction")


    page.go(page.route)

flet.app(
    target=main, view=flet.WEB_BROWSER,
    assets_dir="assets" 
    )
