# flet-image-viewer

flet-image-viewer [Flet](https://flet.dev) extension.

<!--- If your extension wraps a Flutter package, credit it here, ex:
It is based on the [xyz](https://pub.dev/packages/xyz) Flutter package. -->

## Platform Support

<!--- Update the table accordingly for your extension, using ✅ and ❌. -->

| Platform  | iOS | Android | Web | Windows | macOS | Linux |
|-----------|-----|---------|-----|---------|-------|-------|
| Supported | ✅   | ✅       | ❌   | ✅       | ✅     | ✅     |

## Usage

### Installation

Add `flet-image-viewer` dependency to the `pyproject.toml` of your Flet project:

* **From Git**

```toml
dependencies = [
  "flet-image-viewer @ git+https://github.com/zaim-tech/flet-image-viewer",
  "flet>=0.86.5",
]
```

<!--- Remove below list item, if your extension isn't yet available on PyPI. -->

* **From PyPI**

```toml
dependencies = [
  "flet-image-viewer",
  "flet>=0.86.5",
]
```

### Tutorial

Use `FletImageViewer` for one image and `FletMultiViewer` for a swipeable gallery.
The `src` value can be an image URL or a local file path.

```python
import flet as ft

from flet_image_viewer import FletImageViewer, FletMultiViewer


def main(page: ft.Page):
  page.title = "Image viewer tutorial"
  page.padding = 20

  single_image = FletImageViewer(
    src="https://picsum.photos/900/600",
    show_close_button=True,
    BoxFit=ft.BoxFit.CONTAIN,
    min_scale=1.0,
    max_scale=4.0,
    overlay=ft.Container(
      content=ft.Text("Photo preview"),
      bgcolor=ft.Colors.with_opacity(0.75, ft.Colors.BLACK),
      padding=10,
    ),
    on_double_tap=lambda event: print("Image double-tapped"),
  )

  gallery = FletMultiViewer(
    src=[
      "https://picsum.photos/id/10/900/600",
      "https://picsum.photos/id/20/900/600",
      "https://picsum.photos/id/30/900/600",
    ],
    viewer_id="tutorial-gallery",
    index=0,
    BoxFit=ft.BoxFit.CONTAIN,
    on_long_press=lambda event: print("Gallery image long-pressed"),
  )

  page.add(
    ft.Text("Single image", size=20, weight=ft.FontWeight.BOLD),
    ft.Container(content=single_image, height=300),
    ft.Text("Image gallery", size=20, weight=ft.FontWeight.BOLD),
    ft.Container(content=gallery, height=300),
  )


ft.run(main)
```

Save the code as `main.py`, install the dependencies, and start it with:

```bash
flet debug macos
```

Replace `macos` with `windows`, `linux`, `ios`, or `android` when targeting another
supported platform. For iOS and Android, specify a connected device with
`-d <device-id>`. Web is not supported by this extension.

For local images, pass a file path instead of a URL:

```python
FletImageViewer(src="assets/photo.jpg")
```

Important options:

| Option | Description |
|--------|-------------|
| `src` | Image URL or local path for `FletImageViewer`; list of URLs or paths for `FletMultiViewer`. |
| `viewer_id` | Required identifier for `FletMultiViewer`. |
| `index` | Initial image index for `FletMultiViewer`, starting at `0`. |
| `BoxFit` | How the image fits inside the viewer, such as `ft.BoxFit.CONTAIN`. |
| `min_scale` / `max_scale` | Minimum and maximum zoom levels. |
| `overlay` | Optional Flet control displayed over the image viewer, such as a label or action bar. |
| `on_long_press` / `on_double_tap` | Optional Flet event handlers. |

### Run your app

A Flet extension has two sides: its Python controls/services and the native Flutter/Dart widgets behind them.
That native code must be compiled into a Flet client before your controls can render, and the
prebuilt client that a plain `flet run` uses does **not** include this extension.

So run your app in one of these two ways:

**1. [`flet debug`](https://flet.dev/docs/cli/flet-debug)** — supported platforms: *Windows, macOS, Linux, iOS, Android*

Compiles the extension and launches your app on the supported target you pick.

```bash
flet debug macos                   # desktop: no device needed
flet debug android -d <device-id>  # mobile: connect a device/emulator first
```

For iOS and Android, pass `-d <device-id>` (run `flet debug --show-devices` to list connected devices).
Edits to your **Python** code are picked up the next time you run `flet debug`.

**2. [`flet build`](https://flet.dev/docs/cli/flet-build) once, then [`flet run`](https://flet.dev/docs/cli/flet-run)** — desktop only: *Windows, macOS, Linux*

Build a custom client that bundles the extension **once**, then use `flet run` for a fast hot-reload loop while you edit Python:

```bash
flet build macos  # or: flet build windows / flet build linux
flet run          # run from the folder where build/ was created, so it reuses that client
```

`flet run` auto-detects the client under `build/<platform>/`, so your Python edits hot-reload instantly.
Rebuild only when the extension's **Dart** code changes.

### Examples

See the [examples](examples) directory.

### Documentation

<!--- Update the link, if your docs are elsewhere. Alternatively, you could write out all docs in this section directly. -->

Detailed documentation for this package can be found [here](https://MY_GITHUB_ACCOUNT.github.io/flet-image-viewer/).

Made with ❤️ by Zaim.
