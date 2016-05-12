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
cube_vi = vscene.visuals.Line(pos=cube_pt, **std_ln_dic)
view.add(cube_vi)
cube_vi = vscene.visuals.Line(pos=(cube_pt * 0.5 + 0.25), **std_ln_dic)
view.add(cube_vi)
view.camera = 'turntable'
vapp.run()
