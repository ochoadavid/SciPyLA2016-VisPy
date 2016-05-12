#!/usr/bin/python3
# -*- coding: utf-8 -*-
## Autor: David Ochoa

import numpy as np
from vispy.scene.visuals import Line
from pymouse import PyMouse

CV = np.arange(0, 2.05, 0.05, dtype=np.float32) * 3.14159
ZCV = np.zeros(CV.size, dtype=np.float32)
C_xy = np.array([np.cos(CV), np.sin(CV), ZCV]).T
C_xz = np.array([np.cos(CV), ZCV, np.sin(CV)]).T
C_yz = np.array([ZCV, np.cos(CV), np.sin(CV)]).T
sphere_pt = np.concatenate([C_xy, C_xz, C_yz])

class Mouse_trace:
    """Mouse tracing Class. It uses vispy to visualization."""
    def __init__(self, color = (1.0, 1.0, 1.0, 1.0)):
        self.mouse = PyMouse()
        self.pos = np.asarray([0, 0, 0])
        self.color = color
        self.rad = 20.0
        size = self.mouse.screen_size()
        boundaries = np.asarray([[0, size[0]], [0, size[1]], [0, 1]])
        print(boundaries)
        self.sizexyz = [None] * 3
        self.tail_steps = 200
        self.set_bound(boundaries)
        self.visual = [None]

    def set_bound(self, boundaries):
        """Updates the boundaries."""
        self.bound = boundaries
        self.sizexyz = np.abs(boundaries[:,1] - boundaries[:,0])

    def step(self, time_step):
        """Calculate the new position and speed."""
        mpos = self.mouse.position()
        self.pos = np.asarray([mpos[0], self.bound[1,1] - mpos[1], 0])
        self.update_visual()

    def init_visual(self, view):
        """Initialize the object visual."""
        self.trace = np.repeat(self.pos, self.tail_steps).reshape((3,self.tail_steps)).T
        pos = np.concatenate([sphere_pt * self.rad + self.pos, self.trace])
        self.visual = Line(pos = pos, color=self.color)
        view.add(self.visual)

    def update_visual(self):
        """Updates the object visual."""
        self.trace[1:] = self.trace[0:-1]
        self.trace[0] = self.pos
        pos = np.concatenate([sphere_pt * self.rad + self.pos, self.trace])
        self.visual.set_data(pos = pos)

    def shake(self):
        """Inverts the z position and gives the ball a random velocity."""
        pass

if __name__ == '__main__':
    print(Ball_trace.__doc__)
    exit()
