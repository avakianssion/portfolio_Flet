import flet
from flet import AppBar, ElevatedButton,OutlinedButton, Page, Text, View, colors, Image, Container, Row, alignment, CircleAvatar


def main(page: Page):
    page.title = "Home"
    
    print("Initial route:", page.route)

    def route_change(e):
        print("Route change:", e.route)
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Sion Avakian", size=50), center_title=True, bgcolor=colors.LIGHT_BLUE_100),
                    # Container(CircleAvatar(foreground_image_url="https://avatars.githubusercontent.com/u/5041459?s=88&v=4", content=Text("FF")), alignment="center"),
                    Container(content=CircleAvatar(foreground_image_url="Images/plato.jpg", content=Text("FF"), width=200, height=200), alignment=alignment.center,padding=20),
                    # CircleAvatar(foreground_image_url="Images/plato.jpg", content=Text("FF"), alignment="center"),
                    Row(
                        [
                        Container(
                            content=OutlinedButton("Contact", on_click=open_settings),
                            alignment=alignment.center,
                            width=150,
                            height=150,
                        ),
                        Container(
                            content = OutlinedButton("Projects", on_click=open_projects),
                            alignment=alignment.center,
                            width=150,
                            height=150,
                        ),
                        Container(
                            content=OutlinedButton("Experience", on_click=open_experience),
                            alignment=alignment.center,
                            width=150,
                            height=150,
                        ),
                        ],
                        alignment="center",

                    ),

                ],
            bgcolor=colors.YELLOW_200,
            scroll="always"

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
