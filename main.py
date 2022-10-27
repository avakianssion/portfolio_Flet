import flet
from flet import AppBar, ElevatedButton, Page, Text, View, colors


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
                    AppBar(title=Text("Personal Portfolio")),
                    ElevatedButton("About", on_click=open_settings),
                    ElevatedButton("Projects", on_click=open_projects),

                ],
            )
        )
        
        if page.route == "/About":
            page.views.append(
                View(
                    "/About",
                    [
                        AppBar(title=Text("About"), bgcolor=colors.SURFACE_VARIANT),
                        Text("About Page!", style="bodyMedium"),
                    ],
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
                )
            )
        # if page.route == "/settings/mail":
        #     page.views.append(
        #         View(
        #             "/settings/mail",
        #             [
        #                 AppBar(
        #                     title=Text("Mail Settings"), bgcolor=colors.SURFACE_VARIANT
        #                 ),
        #                 Text("Mail settings!"),
        #             ],
        #         )
        #     )
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

    page.go(page.route)


flet.app(target=main, view=flet.WEB_BROWSER)