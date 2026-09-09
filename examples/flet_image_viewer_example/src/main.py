import flet as ft

from flet_image_viewer import FletMultiViewer


def main(page: ft.Page):
    page.add(
        FletMultiViewer(
            src=[
                "https://picsum.photos/id/10/900/600",
                "https://picsum.photos/id/20/900/600",
                "https://picsum.photos/id/30/900/600",
            ],
            viewer_id="photo-gallery",
            index=0,
            BoxFit=ft.BoxFit.CONTAIN,
            overlay=ft.Container(
                content=ft.Text("Swipe to view more"),
                bgcolor=ft.Colors.with_opacity(0.75, ft.Colors.BLACK),
                padding=10,
            ),
            on_long_press=lambda event: print("Image long-pressed"),
            on_double_tap=lambda event: print("Image double-tapped"),
            expand=True,
        )
    )


ft.run(main)