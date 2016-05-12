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
C_xy = np.array([np.cos(CV), np.sin(CV), ZCV]).T
C_xz = np.array([np.cos(CV), ZCV, np.sin(CV)]).T
C_yz = np.array([ZCV, np.cos(CV), np.sin(CV)]).T
sphere_pt = np.concatenate([C_xy, C_xz, C_yz])
sphere_vi = vscene.visuals.Line(pos=sphere_pt, **std_ln_dic)
view.add(sphere_vi)
view.camera = 'turntable'
vapp.run()
