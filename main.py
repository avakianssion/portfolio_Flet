import webbrowser
import flet
from flet import AppBar, FilledTonalButton, Page, Text, View, colors, Image, Container, Row, Column, alignment, CircleAvatar, GestureDetector, padding, TextButton
import webbrowser
from helper import *

def main(page: Page):
    page.title = "Home"
    githhub_text = Text("Find me on Github", size=25, font_family="Inconsolata-Light",color=colors.WHITE)
    
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
                                # Container(content=TextButton("Find me on Linkedin", on_click=open_linkedin, ),alignment=alignment.center,padding=20),
                                # Container(content=TextButton("Find me on Github", on_click=open_github ),alignment=alignment.center,padding=20),

                                TextButton(
                                    content=Container(
                                        content=Text("Click for Linkedin", size=18, font_family="Inconsolata-Light",color=colors.WHITE), bgcolor=colors.PURPLE_400, padding=5,
                                    ),
                                    on_click=open_linkedin,
                                ),
                                TextButton(
                                    content=Container(
                                        content=Text("Click for Github", size=18, font_family="Inconsolata-Light",color=colors.WHITE), bgcolor=colors.PURPLE_400, padding=5,
                                    ),
                                    on_click=open_github,
                                ),
                             ],alignment="center",
                         )
                    ]

                    )
                ],
            bgcolor=colors.BLUE_GREY_700,
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
                                    TextButton(
                                    content=Container(content=Phoenix_logo, padding=5,width=180, height=180),
                                    on_click=open_phoenix,
                                    ),
                                    TextButton(
                                    content=Container(content=Text("Phoenix Robotics",font_family="Inconsolata-Light", color = colors.BLUE_900, size = 25), padding=5,),
                                    on_click=open_phoenix,
                                    ),

                                ], alignment="start"
                                ),
                                
                                Row(
                                [
                                    TextButton(
                                    content=Container(content=RSNA_logo, padding=5,width=180, height=180),
                                    on_click=open_RSNA,
                                    ),
                                    TextButton(
                                    content=Container(content=Text("RSNA Pneumonia Detection",font_family="Inconsolata-Light", color = colors.BLUE_900, size = 25), padding=5,),
                                    on_click=open_RSNA,
                                    ),
 
                                ],alignment="start"
                                ),
                                
                                Row(
                                [
                                    TextButton(
                                    content=Container(content=Vaccine_logo, padding=5, width=180, height=180),
                                    on_click=open_mRNA,
                                    ),
                                    TextButton(
                                    content=Container(content=Text("COVID-19 mRNA Vaccine Degradation Prediction",font_family="Inconsolata-Light", color = colors.BLUE_900, size = 25), padding=5,),
                                    on_click=open_mRNA,
                                    ),
                                    
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
                                        Container(content=general_motors_logo, width=180,height=180, padding=25),
                                        Text("Software Engineer @ General Motors: \nWorking on Ultifi Platforms for Autonomous and Electric Vehciles",font_family="Inconsolata-Light", color = colors.BLUE_900, size = 25)
                                    ], alignment="start"),
                                   
                                   Row(
                                    [
                                        Container(content=capgemini_logo, width=180,height=180, padding=25),
                                        Text("Software Engineer @ Capgemini: \nWorked on Internal Communication Hub System",font_family="Inconsolata-Light", color = colors.BLUE_900, size = 25)
                                    ],alignment="start"),
                                   Row(
                                    [
                                        Container(content=NSF_logo, width=180,height=180, padding=25),
                                        Text("Undergraduate Researcher @ National Science Foundation: \nResearch Project on Online Mis-Information",font_family="Inconsolata-Light", color = colors.BLUE_900, size = 25)
                                     
                                    ],alignment="start"),
                                   Row(
                                    [
                                        Container(content=UCI_logo, width=180,height=180, padding=25),
                                        Text("Undergraduate Researcher @ UC Irvine Data Science Lab: \nRsearch Project on The Use of Data Science In Community Organizations",font_family="Inconsolata-Light", color = colors.BLUE_900, size = 25) 
                                    ],
                                    alignment="start"),
                                    Row(
                                    [
                                        Container(content=YPI_logo, width=180,height=180, padding=25),
                                        Text("Software Engineering Intern @ UC Youth Policy Institute: \nWorked on Fellow Tracking/Feedback System on MERN Stack",font_family="Inconsolata-Light", color = colors.BLUE_900, size = 25)

                                    ],alignment="start"),
                                    
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
        # webbrowser.open_new_tab('https://github.com/avakianssion')
        page.launch_url("https://github.com/avakianssion")


    def open_linkedin(e):
        print("Go to LinkedIn")
        # webbrowser.open_new_tab("https://www.linkedin.com/in/sion-avakian/")
        page.launch_url("https://www.linkedin.com/in/sion-avakian/")

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
