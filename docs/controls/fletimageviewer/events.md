# Events and overlays

## Gesture events

Use `on_long_press` and `on_double_tap` to respond to user interaction:

```python
import flet as ft
from flet_image_viewer import FletImageViewer


def on_double_tap(event: ft.ControlEvent):
    print("Image double-tapped")


def on_long_press(event: ft.ControlEvent):
    print("Image long-pressed")


viewer = FletImageViewer(
    src="https://picsum.photos/900/600",
    on_double_tap=on_double_tap,
    on_long_press=on_long_press,
)
```

## Add an overlay

`overlay` accepts any Flet control:

```python
viewer = FletImageViewer(
    src="https://picsum.photos/900/600",
    overlay=ft.Container(
        content=ft.Text("Photo preview"),
        bgcolor=ft.Colors.with_opacity(0.75, ft.Colors.BLACK),
        padding=10,
    ),
)
```

The same properties and event handlers are available on
[`FletMultiViewer`](../fletmultiviewer/index.md).
