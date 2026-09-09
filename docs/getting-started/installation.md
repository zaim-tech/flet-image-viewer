# Installation

FletImageViewer ships as a Flet extension. Add it to your application's dependencies before building the target client.

## Install from PyPI

```bash
pip install flet-image-viewer
```

Or add it to `pyproject.toml`:

```toml
dependencies = [
    "flet>=0.86.5",
    "flet-image-viewer",
]
```

## Install from GitHub

To use the latest repository version:

```toml
dependencies = [
    "flet>=0.86.5",
    "flet-image-viewer @ git+https://github.com/zaim-tech/flet-image-viewer.git",
]
```

## Import the controls

```python
from flet_image_viewer import FletImageViewer, FletMultiViewer
```

## Next step

Continue to the [quickstart](quickstart.md) to display your first image.
