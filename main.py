import flet
from flet import AppBar, FilledTonalButton ,OutlinedButton, Page, Text, View, colors, Image, Container, Row, alignment, CircleAvatar,NavigationRail, NavigationRailDestination, FloatingActionButton, Icon, icons, VerticalDivider



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
        rail = NavigationRail(
                            selected_index=0,
                            label_type="all",
                            # extended=True,
                            min_width=100,
                            min_extended_width=400,
                            height=500,
                            leading=FloatingActionButton(icon=icons.CREATE, text="Add"),
                            group_alignment=-0.9,
                            destinations=[
                                NavigationRailDestination(
                                    icon=icons.FAVORITE_BORDER, selected_icon=icons.FAVORITE, label="First"
                                ),
                                NavigationRailDestination(
                                    icon_content=Icon(icons.BOOKMARK_BORDER),
                                    selected_icon_content=Icon(icons.BOOKMARK),
                                    label="Second",
                                ),
                                NavigationRailDestination(
                                    icon=icons.SETTINGS_OUTLINED,
                                    selected_icon_content=Icon(icons.SETTINGS),
                                    label_content=Text("Settings"),
                                ),
                            ],
                        )
        page.views.append(
            View(
                "/",
                [
                    # AppBar(title=Text("Sion Avakian", size=50, font_family="Montserrat-Regular", color=colors.WHITE), center_title=True, bgcolor=colors.BLUE_GREY),
                    Container(content=Text("Sion Avakian", size=50, font_family="Montserrat-Regular",color=colors.WHITE),alignment=alignment.center),
                    Row(
                        [
                        rail,
                        VerticalDivider(width=1),
                        Container(
                            content=FilledTonalButton("Contact", on_click=open_settings),
                            alignment=alignment.center,
                            width=150,
                            height=150,
                        ),
                        Container(
                            content = FilledTonalButton("Projects", on_click=open_projects),
                            alignment=alignment.center,
                            width=150,
                            height=150,
                        ),
                        Container(
                            content=FilledTonalButton("Experience", on_click=open_experience),
                            alignment=alignment.center,
                            width=150,
                            height=150,
                        ),
                        ],
                        alignment="start",

                    ),
                    Container(content=CircleAvatar(foreground_image_url="Images/headshot.jpg", content=Text("FF"), width=200, height=200), alignment=alignment.center,padding=20),
                    Container(content=Text("Software engineer and computer science enthusiast.", size=25, font_family="Montserrat-Light",color=colors.WHITE),alignment=alignment.center,padding=20),

                ],
            bgcolor=colors.BLUE_GREY,
            scroll="always",
    

            ),
        )

        if page.route == "/About":
            page.views.append(
                View(
                    "/About",
                    [
                        AppBar(title=Text("About", color=colors.RED_200), bgcolor=colors.LIGHT_BLUE_700),
                        Text("About Page!", style="bodyMedium"),
                    ],
                scroll="always",
                bgcolor=colors.RED
                )
            )

        if page.route == "/Projects":
            page.views.append(
                View(
                    "/Projects",
                    [
                        AppBar(title=Text("Projects"), bgcolor=colors.SURFACE_VARIANT),
                        Text("Projects Page!", style="bodyMedium"),
                    ],
                scroll="always"
                )
            )
        if page.route == "/Experience":
            img = Image(
                src="Images/resume.jpg",
                # width=1000,
                # height=1500,
                fit="fill",
                )

            page.views.append(
                View(
                    "/Experience",
                    [
                        AppBar(title=Text("Experience"), bgcolor=colors.SURFACE_VARIANT),
                        img,  
                    ],
                padding= 50,
                scroll="always",
                bgcolor=colors.RED

                )
            )

        page.bgcolor=colors.RED_ACCENT
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

    def open_settings(e):
        page.go("/About")
    def open_experience(e):
        page.go("/Experience")
 

    page.go(page.route)


flet.app(
    target=main, view=flet.WEB_BROWSER,
    assets_dir="assets" 
    )
