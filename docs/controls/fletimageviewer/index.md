# FletImageViewer

`FletImageViewer` displays one image with native zoom and gesture support.

```python
import flet as ft
from flet_image_viewer import FletImageViewer

viewer = FletImageViewer(
    src="https://picsum.photos/900/600",
    show_close_button=True,
    BoxFit=ft.BoxFit.CONTAIN,
    min_scale=1.0,
    max_scale=4.0,
)
```

The control extends Flet's `LayoutControl`, so standard layout properties such
as `expand`, `width`, `height`, `padding`, and `visible` can be used.

See [Properties](properties.md) for configuration details and
[Events and overlays](events.md) for interaction examples.
