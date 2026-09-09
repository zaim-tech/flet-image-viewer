import 'package:flet/flet.dart';
import 'package:flutter/material.dart';
import 'package:photo_viewer/photo_viewer.dart';

class FletImageViewerControl extends StatelessWidget {
  final Control control;

  const FletImageViewerControl({
    super.key,
    required this.control,
  });

  @override
  Widget build(BuildContext context) {
    ResolvedAssetSource asset = control.getSrc("src");
    String imageUrl = asset.uri ?? "";
    Widget? overlayWidget = control.buildWidget("overlay");

    
    Widget myControl = PhotoViewerImage(
      imageUrl: imageUrl,
      showDefaultCloseButton: control.getBool("show_close_button", false)!,
      fit: control.getBoxFit("BoxFit", BoxFit.none)!,
      maxScale: control.getDouble("max_scale"),
      minScale: control.getDouble("min_scale"),
      overlayBuilder: overlayWidget != null
          ? (BuildContext ctx) => overlayWidget
          : null,
      onLongPress: control.getBool("on_long_press", false)!
          ? () => control.triggerEvent("long_press")
          : null,
      onDoubleTap: control.getBool("on_double_tap", false)!
          ? () => control.triggerEvent("double_tap")
          : null,    

    );

    return LayoutControl(control: control, child: myControl);
  }
}


class FletMultiViewerControl extends StatelessWidget {
  final Control control;

  const FletMultiViewerControl({
    super.key,
    required this.control,
  });

  @override
  Widget build(BuildContext context) {
    List<String> src = control.getList<String>("src", (item) => item.toString(), defaultValue: [],) ?? [];
    Widget? overlayWidget = control.buildWidget("overlay");

    Widget multicontrol = PhotoViewerMultipleImage(
      imageUrls: src,
      id: control.getString("viewer_id", "")!,
      index: control.getInt("index", 0)!,
      fit: control.getBoxFit("BoxFit", BoxFit.none)!,
      maxScale: control.getDouble("max_scale"),
      minScale: control.getDouble("min_scale"),
      overlayBuilder: overlayWidget != null
          ? (BuildContext ctx) => overlayWidget
          : null,
      onLongPress: control.getBool("on_long_press", false)!
          ? () => control.triggerEvent("long_press")
          : null,
      onDoubleTap: control.getBool("on_double_tap", false)!
          ? () => control.triggerEvent("double_tap")
          : null,    


    );

    return LayoutControl(control: control, child: multicontrol);
  }
}
