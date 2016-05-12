#!/usr/bin/python3
# -*- coding: utf-8 -*-
## Autor: David Ochoa

import vispy.scene as vscene
import vispy.app as vapp
import numpy as np
import sys


class Bworld():
    """Ball and bubble world class.
            This clas initialize the view, handle the keypresses and update
            every object every time_step.
    """
    def __init__(self, bubble_list, boundaries = np.asarray([[0, 10], [0, 10], [0, 10]])):
        self.auto = False
        self.time_step = 0.1
        self.bubbles = bubble_list
        self.bound = boundaries
        for bble in self.bubbles:
            bble.set_bound(self.bound)
        canvas = vscene.SceneCanvas(show=True, title=sys.argv[0])
        # canvas.measure_fps()
        view = canvas.central_widget.add_view()
        if self.bound is not None:
            bound_pt = np.array([[self.bound[0, 0], self.bound[1, 0], self.bound[2, 0]],
                                 [self.bound[0, 1], self.bound[1, 0], self.bound[2, 0]],
                                 [self.bound[0, 1], self.bound[1, 1], self.bound[2, 0]],
                                 [self.bound[0, 0], self.bound[1, 1], self.bound[2, 0]],
                                 [self.bound[0, 0], self.bound[1, 0], self.bound[2, 0]],
                                 [self.bound[0, 0], self.bound[1, 0], self.bound[2, 1]],
                                 [self.bound[0, 1], self.bound[1, 0], self.bound[2, 1]],
                                 [self.bound[0, 1], self.bound[1, 1], self.bound[2, 1]],
                                 [self.bound[0, 0], self.bound[1, 1], self.bound[2, 1]],
                                 [self.bound[0, 0], self.bound[1, 0], self.bound[2, 1]]],
                                 dtype=np.float32)
            bound_vi = vscene.visuals.Line(pos=bound_pt, color=(1.00, 1.00, 1.00, 0.25))
            view.add(bound_vi)
        view.camera = 'panzoom'
        for bble in self.bubbles:
            bble.init_visual(view)

        def update(ev):
            for bble in self.bubbles:
                bble.step(self.time_step)

        timer = vapp.Timer()
        timer.connect(update)

        @canvas.events.key_press.connect
        def on_key_press(event):
            if event.key == 'Right':
                for bble in self.bubbles:
                    bble.step(self.time_step)
            if event.key == 'Space':
                if self.auto:
                    timer.stop()
                    self.auto = False
                else:
                    timer.start(self.time_step)
                    self.auto = True
            if event.key == 's':
                for bble in self.bubbles:
                    bble.shake()

        vapp.run()
