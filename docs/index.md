# Introduction

FletImageViewer for Flet.

## Platform Support

FletImageViewer supports all Flet platforms except Web:

| Platform  | iOS | Android | Web | Windows | macOS | Linux |
|-----------|-----|---------|-----|---------|-------|-------|
| Supported | ✅   | ✅       | ❌   | ✅       | ✅     | ✅     |

## Examples

```
import flet as ft

from flet_image_viewer import FletImageViewer


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(

                ft.Container(height=150, width=300, alignment = ft.Alignment.CENTER, bgcolor=ft.Colors.PURPLE_200, content=FletImageViewer(
                    tooltip="My new FletImageViewer Control tooltip",
                    value = "My new FletImageViewer Flet Control",
                ),),

    )


ft.run(main)
```

## Classes

[FletImageViewer](FletImageViewer.md)
