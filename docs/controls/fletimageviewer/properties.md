# Properties

## `src`

```python
src: str
```

Required image URL or local file path.

```python
FletImageViewer(src="https://picsum.photos/900/600")
FletImageViewer(src="assets/photo.jpg")
```

## `show_close_button`

```python
show_close_button: bool = False
```

Shows the viewer's close button when enabled.

## `BoxFit`

```python
BoxFit: Optional[ft.BoxFit] = None
```

Controls how the image fits inside the viewer. Common values include
`ft.BoxFit.CONTAIN` and `ft.BoxFit.COVER`.

## `overlay`

```python
overlay: Optional[ft.Control] = None
```

Places a Flet control over the image viewer. Use it for labels, actions, or
status information.

## `min_scale` and `max_scale`

```python
min_scale: Optional[float] = None
max_scale: Optional[float] = None
```

Set the minimum and maximum zoom levels.

## Layout properties

As a `LayoutControl`, the viewer also supports layout properties such as
`expand`, `width`, `height`, `padding`, `alignment`, and `visible`.
