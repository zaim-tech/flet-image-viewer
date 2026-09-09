# Examples

## Image with overlay

```python
import flet as ft
from flet_image_viewer import FletImageViewer


viewer = FletImageViewer(
    src="https://picsum.photos/900/600",
    overlay=ft.Container(
        content=ft.Text("Photo preview"),
        bgcolor=ft.Colors.with_opacity(0.75, ft.Colors.BLACK),
        padding=10,
    ),
    expand=True,
)
```

## Local image gallery

```python
import os
import flet as ft
from flet_image_viewer import FletMultiViewer


base = os.path.dirname(os.path.abspath(__file__))
images = [
    os.path.join(base, "assets/photo-1.jpg"),
    os.path.join(base, "assets/photo-2.jpg"),
]

gallery = FletMultiViewer(
    src=images,
    viewer_id="local-gallery",
    index=0,
    expand=True,
)
```

## Run the example application

The complete sample app is in
[`examples/flet_image_viewer_example/`](../../examples/flet_image_viewer_example/).
See [Building and running](building.md) for the client build command.
