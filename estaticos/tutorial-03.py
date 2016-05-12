#!/usr/bin/python3
# -*- coding: utf-8 -*-
## Autor: David Ochoa

import vispy.scene as vscene
import vispy.app as vapp
import numpy as np
import sys

std_ln_dic = dict(color=(1.00, 1.00, 1.00, 1.00))

canvas = vscene.SceneCanvas(show=True, title=sys.argv[0])
view = canvas.central_widget.add_view()
CV = np.arange(0, 2.05, 0.05, dtype=np.float32) * 3.14159
ZCV = np.zeros(CV.size, dtype=np.float32)
circle_pt = np.array([np.cos(CV), np.sin(CV), ZCV]).T
circle_vi = vscene.visuals.Line(pos=circle_pt, **std_ln_dic)
view.add(circle_vi)
view.camera = 'turntable'
vapp.run()
