# Troubleshooting

## The viewer is not rendering

Build the Flet client with the extension included before running the example:

```bash
flet build windows
flet run
```

Use the matching build target for macOS, Linux, Android, or iOS.

## Web is not supported

`flet-image-viewer` uses native Flutter functionality and does not currently
support the Web target.

## Local images do not load

Check that the path exists at runtime and that the image is included in your
application assets. Prefer an absolute path while diagnosing path issues.

## Changes are not visible

Rebuild after changing Dart or Flutter code. Python-only changes can be
reloaded after the native client has already been built.
