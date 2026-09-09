import flet as ft

from flet_image_viewer import FletImageViewer, FletMultiViewer

import os


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    base = os.path.dirname(os.path.abspath(__file__))
    image = os.path.join(base, "assets/test.jpg")
    image2 = os.path.join(base, "assets/IMG.jpg")


    multi = FletMultiViewer(
        src=["https://avatars.githubusercontent.com/u/201727728?v=4", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBB4LQTn0vRq4ydPLp-uTj_lEUHOHYWUU18JlCq5KuMw&s=10", image, image2],
        viewer_id="photos",
        index=0,
        on_long_press=lambda e: print("long press"),
        on_double_tap=lambda e: print("double tap")
        

    )

    page.add(multi)


ft.run(main)
