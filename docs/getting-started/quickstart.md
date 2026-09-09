# Quickstart

## Display one image

```python
import flet as ft
from flet_image_viewer import FletImageViewer


def main(page: ft.Page):
    page.add(
        FletImageViewer(
            src="https://picsum.photos/900/600",
            BoxFit=ft.BoxFit.CONTAIN,
            min_scale=1.0,
            max_scale=4.0,
            expand=True,
        )
    )


ft.run(main)
```

Use a local path when the image is included with your application:

```python
FletImageViewer(src="assets/photo.jpg")
```

## Display a gallery

```python
import flet as ft
from flet_image_viewer import FletMultiViewer


def main(page: ft.Page):
    page.add(
        FletMultiViewer(
            src=[
                "https://picsum.photos/id/10/900/600",
                "https://picsum.photos/id/20/900/600",
            ],
            viewer_id="quickstart-gallery",
            index=0,
            expand=True,
        )
    )


ft.run(main)
```

## Where next

- Learn each property in the [control reference](../controls/fletimageviewer/index.md).
- Copy more recipes from [Examples](../guides/examples.md).
- Check target requirements in [Platform notes](../reference/platform-notes.md).
