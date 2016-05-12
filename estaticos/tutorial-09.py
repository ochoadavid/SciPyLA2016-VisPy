#!/usr/bin/python3
# -*- coding: utf-8 -*-
## Autor: David Ochoa

import vispy.scene as vscene
import vispy.app as vapp
import numpy as np
import sys
import time

std_ln_dic = dict(color=(1.00, 1.00, 1.00, 1.00), connect='segments')

canvas = vscene.SceneCanvas(show=True, title=sys.argv[0])
view = canvas.central_widget.add_view()
cube_pt = np.array([[0.0, 0.0, 0.0], [0.0, 1.0, 0.0],
                    [0.0, 1.0, 0.0], [1.0, 1.0, 0.0],
                    [1.0, 1.0, 0.0], [1.0, 0.0, 0.0],
                    [1.0, 0.0, 0.0], [0.0, 0.0, 0.0],
                    [0.0, 0.0, 1.0], [0.0, 1.0, 1.0],
                    [0.0, 1.0, 1.0], [1.0, 1.0, 1.0],
                    [1.0, 1.0, 1.0], [1.0, 0.0, 1.0],
                    [1.0, 0.0, 1.0], [0.0, 0.0, 1.0],
                    [0.0, 0.0, 0.0], [0.0, 0.0, 1.0],
                    [1.0, 0.0, 0.0], [1.0, 0.0, 1.0],
                    [0.0, 1.0, 0.0], [0.0, 1.0, 1.0],
                    [1.0, 1.0, 0.0], [1.0, 1.0, 1.0]],
                    dtype=np.float32)
n = 50
cube_vi = vscene.visuals.Line(pos=cube_pt, **std_ln_dic)
view.add(cube_vi)
view.camera = 'turntable'
vapp.process_events()
for i in range(1,n):
    scale = 1.0 - (1 / n) * i
    cube_vi.set_data(pos = (cube_pt * scale + (1 - scale) / 2))
    time.sleep(0.05)
    vapp.process_events()
for i in range(n,1,-1):
    scale = 1.0 - (1 / n) * i
    cube_vi.set_data(pos = (cube_pt * scale + (1 - scale) / 2))
    time.sleep(0.05)
    vapp.process_events()
