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

class Bubble:
    """Bubble Class. It uses vispy to visualization."""
    def __init__(self, position, velocity, boundaries = None, radius = 0.1, color=(1.0, 1.0, 1.0, 1.0)):
        self.pos = position
        self.vel = velocity
        self.rad = radius
        self.color = color
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
        """Calculate the new position and speed."""
        despl = self.vel * time_step
        self.pos = self.pos + despl
        if self.sizexyz[2] is not None and self.pos[2] > self.bound[2,1]:
            self.pos[0] = (self.sizexyz[0]) * np.random.rand(1) + self.bound[0,0]
            self.pos[1] = (self.sizexyz[1]) * np.random.rand(1) + self.bound[1,0]
            self.pos[2] = self.bound[2,0]
            self.rad = 0.01
            self.vel[2] = 0.0
        if self.sizexyz[2] is not None and self.pos[2] == self.bound[2,0]:
            self.rad = self.rad + 0.02 #np.random.rand(1) / 20
            if self.rad + np.random.rand(1) / 2 > 0.4:
                self.vel[2] = self.vel[2] + self.rad
        else:
            self.vel[2] = self.vel[2] + self.rad
        self.update_visual()

    def init_visual(self, view):
        """Initialize the object visual."""
        self.visual = Line(pos = sphere_pt * self.rad + self.pos, color=self.color)
        view.add(self.visual)

    def update_visual(self):
        """Updates the object visual."""
        self.visual.set_data(pos = sphere_pt * self.rad + self.pos)

    def shake(self):
        """Loose the bubble from the bottom."""
        if self.sizexyz[2] is not None:
            self.pos[2] = self.pos[2] + 0.001

if __name__ == '__main__':
    print(Bubble2.__doc__)
    exit()
