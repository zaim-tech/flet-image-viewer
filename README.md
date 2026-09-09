# flet-image-viewer

`flet-image-viewer` is a Flet extension for displaying zoomable images and
swipeable image galleries in Flet applications.

[![PyPI](https://img.shields.io/pypi/v/flet-image-viewer)](https://pypi.org/project/flet-image-viewer/)
[![Documentation](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://zaim-tech.github.io/flet-image-viewer/)
[![Repository](https://img.shields.io/badge/source-GitHub-181717)](https://github.com/zaim-tech/flet-image-viewer)

The package provides `FletImageViewer` for a single image and `FletMultiViewer`
for a swipeable gallery. Both controls support pinch-to-zoom, configurable
image fitting, overlays, and long-press or double-tap events.

## Demo

Want to see it in action? Watch the [sample demo video](https://www.image2url.com/r2/default/videos/1788985175034-378cd23e-ec61-469e-8d07-5ce4f3e569aa.mp4).

## Installation

Install the published package from PyPI:

```bash
pip install flet-image-viewer
```

Or add it to your application's `pyproject.toml`:

```toml
[project]
dependencies = [
    "flet>=0.86.5",
    "flet-image-viewer",
]
```

To install the latest version directly from GitHub instead, use:

```toml
[project]
dependencies = [
    "flet>=0.86.5",
    "flet-image-viewer @ git+https://github.com/zaim-tech/flet-image-viewer.git",
]
```

## Usage

```python
import flet as ft

from flet_image_viewer import FletImageViewer


def main(page: ft.Page):
    page.title = "Image viewer example"
    page.add(
        FletImageViewer(
            src="https://picsum.photos/900/600",
            show_close_button=True,
            BoxFit=ft.BoxFit.CONTAIN,
            min_scale=1.0,
            max_scale=4.0,
            expand=True,
        )
    )


ft.run(main)
```

The `src` property accepts an image URL or a local file path. For example:

```python
base = os.path.dirname(os.path.abspath(__file__))
image = os.path.join(base, "assets/photo.jpg")
FletImageViewer(src=image)
```

## Swipeable gallery

Use `FletMultiViewer` to display multiple images. The `index` property selects
the image shown first, starting at `0`.

```python
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
```

## Control properties

| Property | Type | Default | Description |
| --- | --- | --- | --- |
| `src` | `str` / `list` | required | Image URL or local path, or a list of URLs and paths for `FletMultiViewer`. |
| `viewer_id` | `str` | required for `FletMultiViewer` | Identifier for the multi-image viewer. |
| `index` | `int` | `0` | Initial image index for `FletMultiViewer`. |
| `show_close_button` | `bool` | `False` | Shows a close button on `FletImageViewer`. |
| `BoxFit` | `ft.BoxFit \\| None` | `None` | Controls how the image fits inside the viewer. |
| `overlay` | `ft.Control \\| None` | `None` | Flet control displayed over the image viewer. |
| `min_scale` / `max_scale` | `float \\| None` | `None` | Minimum and maximum zoom levels. |
| `on_long_press` | event handler | `None` | Called when the image is long-pressed. |
| `on_double_tap` | event handler | `None` | Called when the image is double-tapped. |

## Events

Register handlers directly on either viewer:

```python
def handle_double_tap(event: ft.ControlEvent):
    print("Viewer double-tapped")


viewer = FletImageViewer(
    src="https://picsum.photos/900/600",
    on_double_tap=handle_double_tap,
)
```

## Platform support

The extension supports all Flet platforms except Web:

| Platform | Support |
| --- | --- |
| Android | Supported |
| iOS | Supported |
| Linux | Supported |
| macOS | Supported |
| Windows | Supported |
| Web | Not supported |

## Build and run

For desktop development, build the client once and then use `flet run`:

```bash
flet build windows
flet run
```

Rebuild the client when the extension's Dart code changes. Python-only changes
can be picked up with the normal Flet development workflow after the extension
has been built.

## Build the example

The example application is in
[`examples/flet_image_viewer_example/`](examples/flet_image_viewer_example/):

```bash
cd examples/flet_image_viewer_example
flet build windows
flet run
```

Replace `windows` with another supported desktop or mobile target.

## Documentation

See the [complete API documentation](https://zaim-tech.github.io/flet-image-viewer/)
for the generated control reference.

## Development

The project follows Flet's extension structure:

```text
src/flet_image_viewer/               Python controls
src/flutter/flet_image_viewer/       Native Flutter extension
examples/flet_image_viewer_example/  Sample Flet application
docs/                                API documentation
```

## License

See [LICENSE](LICENSE).

---

**Made with ❤️ by [Zaim Sheali](https://github.com/zaim-tech)**
