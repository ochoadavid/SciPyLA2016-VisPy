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

class Ball_trace:
    """Ball Class. It uses vispy to visualization."""
    def __init__(self, position, velocity, boundaries = None, color = (1.0, 1.0, 1.0, 1.0)):
        self.pos = position
        self.vel = velocity
        self.color = color
        self.rad = 0.1
        self.bound = None
        self.sizexyz = [None] * 3
        self.tail_steps = 20
        if boundaries is not None:
            self.set_bound(boundaries)
        self.visual = [None]

    def set_bound(self, boundaries):
        """Updates the boundaries."""
        self.bound = boundaries
        self.sizexyz = np.abs(boundaries[:,1] - boundaries[:,0])

    def step(self, time_step):
        """Calculate the new position and speed."""
        despl = self.vel * time_step
        self.pos = self.pos + despl
        for i in range(3):
#-INF            if self.sizexyz[i] is not None and self.pos[i] < self.bound[i,0]:
#-INF                self.pos[i] = self.pos[i] + self.sizexyz[i]
#-INF            elif self.sizexyz[i] is not None and self.pos[i] > self.bound[i,1]:
#-INF                self.pos[i] = self.pos[i] - self.sizexyz[i]
            if self.sizexyz[i] is not None:
                if self.pos[i] < self.bound[i,0] or self.pos[i] > self.bound[i,1]:
                    self.pos[i] = self.pos[i] - despl[i]
                    self.vel[i] = - self.vel[i] * 0.95
        self.vel[2] = self.vel[2] - 0.1
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
        if self.sizexyz[2] is not None:
            self.pos[2] = self.bound[2, 1] - (self.pos[2] - self.bound[2, 0])
            self.vel = (np.random.rand(3) - 0.5) * 10
            self.trace = np.repeat(self.pos, self.tail_steps).reshape((3,self.tail_steps)).T

if __name__ == '__main__':
    print(Ball_trace.__doc__)
    exit()
