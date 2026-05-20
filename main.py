import flet as ft

def main(page: ft.Page):
    page.title = "Flet App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.add(
        ft.Row(
            [
                ft.Text("សួស្តី! នេះជា App របស់ខ្ញុំ", size=30),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
