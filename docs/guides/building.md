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

Watch the [sample demo video](https://www.image2url.com/r2/default/videos/1788985175034-378cd23e-ec61-469e-8d07-5ce4f3e569aa.mp4)
to see the image viewer and gallery in action.
