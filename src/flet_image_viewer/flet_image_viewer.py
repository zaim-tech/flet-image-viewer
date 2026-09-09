from enum import Enum
from typing import Any, Optional

import flet as ft

@ft.control("FletImageViewer")
class FletImageViewer(ft.LayoutControl):
    """
    flet-photo-viewer
    A Flet extension that wraps the photo_viewer Flutter package,
    bringing pinch-to-zoom, swipeable image viewing to your Flet apps — as a single full-screen viewer or a swipeable multi-image gallery.
    Full-screen, pinch-zoomable image viewer (FletImageViewer)

    import flet as ft

    from flet_photo_viewer import FletImageViewer

    def main(page: ft.Page):
        page.add(
            FletImageViewer(
                src="https://picsum.photos/800",  # URL or local file path 
                show_close_button=True,
                BoxFit=ft.BoxFit.COVER,
            )
        )

    ft.run(main)
    """

    src: str
    show_close_button: bool = False
    BoxFit: Optional[ft.BoxFit] = None 
    overlay: Optional[ft.Control] = None
    min_scale: Optional[float] = None
    max_scale: Optional[float] = None
    on_long_press: Optional[ft.ControlEventHandler["FletImageViewer"]] = None
    on_double_tap: Optional[ft.ControlEventHandler["FletImageViewer"]] = None 


@ft.control("FletMultiViewer")
class FletMultiViewer(ft.LayoutControl):
    """
    flet-photo-viewer
        A Flet extension that wraps the photo_viewer Flutter package,
        bringing pinch-to-zoom, swipeable image viewing to your Flet apps — as a single full-screen viewer or a swipeable multi-image gallery.
        Swipeable multi-image gallery viewer (FletMultiViewer)

        import flet as ft

        from flet_photo_viewer import FletMultiViewer

        def main(page: ft.Page):
            page.add(
                FletMultiViewer(
                    src=[
                        "https://picsum.photos/800?1",
                        "https://picsum.photos/800?2",
                        "https://picsum.photos/800?3",
                    ],
                    index=0,          # which image to open on
                    BoxFit=ft.BoxFit.COVER,
                )
            )

        ft.run(main)

    
    """    
    src: list
    viewer_id: str
    index: int = 0
    BoxFit: Optional[ft.BoxFit] = None
    overlay: Optional[ft.Control] = None
    min_scale: Optional[float] = None
    max_scale: Optional[float] = None
    on_long_press: Optional[ft.ControlEventHandler["FletMultiViewer"]] = None
    on_double_tap: Optional[ft.ControlEventHandler["FletMultiViewer"]] = None


