#!/usr/bin/python3
# -*- coding: utf-8 -*-
## Autor: David Ochoa

import vispy.scene as vscene
import vispy.app as vapp
import numpy as np
import sys

std_ln_dic = dict(color=(1.00, 1.00, 1.00, 1.00), connect='segments')

canvas = vscene.SceneCanvas(show=True, title=sys.argv[0])
view = canvas.central_widget.add_view()
CV = np.arange(0, 2.05, 0.05, dtype=np.float32) * 3.14159
CV_seg = np.zeros(((CV.size) - 1) * 2)
CV_seg[0::2] = CV[:-1]
CV_seg[1::2] = CV[1:]
ZCV_seg = np.zeros(CV_seg.size, dtype=np.float32)
C_xy = np.array([np.cos(CV_seg), np.sin(CV_seg), ZCV_seg]).T
C_xz = np.array([np.cos(CV_seg), ZCV_seg, np.sin(CV_seg)]).T
C_yz = np.array([ZCV_seg, np.cos(CV_seg), np.sin(CV_seg)]).T
sphere_pt = np.concatenate([C_xy, C_xz, C_yz])
sphere_vi = vscene.visuals.Line(pos=sphere_pt, **std_ln_dic)
view.add(sphere_vi)
view.camera = 'turntable'
vapp.run()
