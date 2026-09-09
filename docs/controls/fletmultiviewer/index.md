# FletMultiViewer

`FletMultiViewer` displays a swipeable gallery of images.

```python
import flet as ft
from flet_image_viewer import FletMultiViewer

viewer = FletMultiViewer(
    src=[
        "https://picsum.photos/id/10/900/600",
        "https://picsum.photos/id/20/900/600",
        "https://picsum.photos/id/30/900/600",
    ],
    viewer_id="photo-gallery",
    index=0,
    BoxFit=ft.BoxFit.CONTAIN,
    expand=True,
)
```

`src` is a list of image URLs or local paths. `viewer_id` identifies the
viewer, and `index` selects the initial image starting at `0`.

The gallery also supports `overlay`, `min_scale`, `max_scale`,
`on_long_press`, and `on_double_tap`.
