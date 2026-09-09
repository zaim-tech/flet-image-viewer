import 'package:flet/flet.dart';
import 'package:flutter/widgets.dart';

import 'flet_image_viewer.dart';

class Extension extends FletExtension {
  @override
  Widget? createWidget(Key? key, Control control) {
    switch (control.type) {
      case "FletImageViewer":
        return FletImageViewerControl(control: control);
      case "FletMultiViewer":
        return FletMultiViewerControl(control: control);      
      default:
        return null;
    }
  }
}
