#!/usr/bin/python3
# -*- coding: utf-8 -*-
## Autor: David Ochoa

import vispy.scene as vscene
import vispy.app as vapp
import numpy as np
import sys

canvas = vscene.SceneCanvas(show=True, title=sys.argv[0])
view = canvas.central_widget.add_view()
square_pt = np.array([[0.0, 0.0],
                     [0.0, 1.0],
                     [1.0, 1.0],
                     [1.0, 0.0],
                     [0.0, 0.0]],
                     dtype=np.float32)
square_vi = vscene.visuals.Line(pos=square_pt, color=(1.0, 1.0, 1.0, 1.0))
view.add(square_vi)
view.camera = 'panzoom'
vapp.run()
