#
import flet
from flet import Page, Text, Row, TextField, ElevatedButton


def main(page):
    name = 'John R'
    t = Text()
    
    def button_clicked(e):
        page.add(Text(f"Hello {name}, this string was formatted"))
    
    page.add(
        Row(controls = [
            TextField(label="Name"),
            ElevatedButton(text="Say my name!", on_click=button_clicked)
        ])
    )
    page.update()

 

flet.app(target=main, view=flet.WEB_BROWSER)
