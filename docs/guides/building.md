# Building and running

Flet extensions include native Flutter code, so the extension must be included
in the client before the viewer can render.

## Build the example

```bash
cd examples/flet_image_viewer_example
flet build windows
flet run
```

Replace `windows` with another supported target such as `macos`, `linux`,
`apk`, or `ipa`.

Rebuild after changing the extension's Dart code. Python-only changes can be
run again without rebuilding the native extension.

## Demo video

See the [sample demo video](../../examples/sample.mp4) for a quick view of the
image viewer and gallery in action.
