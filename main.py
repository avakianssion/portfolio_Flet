import flet
from flet import AppBar, ElevatedButton, Page, Text, View, colors, Image, NavigationRail


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
                    AppBar(title=Text("Sion Avakian"), center_title=True),
                    ElevatedButton("About", on_click=open_settings),
                    ElevatedButton("Projects", on_click=open_projects),
                    ElevatedButton("Experience", on_click=open_experience),
                ],
            ),
        )

        if page.route == "/About":
            page.views.append(
                View(
                    "/About",
                    [
                        AppBar(title=Text("About"), bgcolor=colors.SURFACE_VARIANT),
                        Text("About Page!", style="bodyMedium"),
                    ],
                scroll="always"
                )
            )

        if page.route == "/Projects":
            page.bgcolor = colors.AMBER_100            
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
                scroll="always"
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

    def open_settings(e):
        page.go("/About")
    def open_experience(e):
        page.go("/Experience")
 

    page.go(page.route)


flet.app(
    target=main, view=flet.WEB_BROWSER,
    assets_dir="assets" 
    )
