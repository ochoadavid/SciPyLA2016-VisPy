#!/usr/bin/python3
# -*- coding: utf-8 -*-
## Autor: David Ochoa

import numpy as np
from vispy.scene.visuals import Line

CV = np.arange(0, 2.05, 0.05, dtype=np.float32) * 3.14159
ZCV = np.zeros(CV.size, dtype=np.float32)
C_xy = np.array([np.cos(CV), np.sin(CV), ZCV]).T
C_xz = np.array([np.cos(CV), ZCV, np.sin(CV)]).T
C_yz = np.array([ZCV, np.cos(CV), np.sin(CV)]).T
sphere_pt = np.concatenate([C_xy, C_xz, C_yz])

class Balloon:
    """Balloon Class. It uses vispy to visualization."""
    def __init__(self, position, velocity, boundaries = None, color = (1.0, 1.0, 1.0, 1.0)):
        self.pos = position
        self.vel = velocity
        self.color = color
        self.rad = 0.5
        self.bound = None
        self.sizexyz = [None] * 3
        if boundaries is not None:
            self.set_bound(boundaries)
        self.visual = None

    def set_bound(self, boundaries):
        """Updates the boundaries."""
        self.bound = boundaries
        self.sizexyz = np.abs(boundaries[:,1] - boundaries[:,0])

    def step(self, time_step):
        """Does nothing."""
        pass

    def init_visual(self, view):
        """Initialize the object visual."""
        self.visual = Line(pos = sphere_pt * self.rad + self.pos, color=self.color)
        view.add(self.visual)

    def update_visual(self):
        """Updates the object visual."""
        self.visual.set_data(pos = sphere_pt * self.rad + self.pos)

    def shake(self):
        """Changes to a random color."""
        self.color = np.random.rand(4) / 2 + 0.5
        self.visual.set_data(color=self.color)

if __name__ == '__main__':
    print(Ball.__doc__)
    exit()
