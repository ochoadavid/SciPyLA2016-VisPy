#!/usr/bin/python3
# -*- coding: utf-8 -*-
## Autor: David Ochoa

import numpy as np
from vispy.scene.visuals import Line

CV = np.arange(0, 2.05, 0.05, dtype=np.float32) * 3.14159
CV_seg = np.zeros((CV.size) * 2)
CV_seg[0:-2:2] = CV[0:-1]
CV_seg[1:-3:2] = CV[1:-1]
ZCV_seg = np.zeros(CV_seg.size, dtype=np.float32)
C_xy = np.array([np.cos(CV_seg), np.sin(CV_seg), ZCV_seg]).T
C_xz = np.array([np.cos(CV_seg), ZCV_seg, np.sin(CV_seg)]).T
C_yz = np.array([ZCV_seg, np.cos(CV_seg), np.sin(CV_seg)]).T
sphere_pt = np.concatenate([C_xy, C_xz, C_yz])

class Bubble2:
    """Class containg a n number of bubbles. It uses vispy to visualization."""
    def __init__(self, position, velocity, boundaries = None, radius = None, color=(1.0, 1.0, 1.0, 1.0)):
        self.n = position.shape[0]
        self.pos = position
        self.vel = velocity
        self.color = color
        if radius is not None:
            self.rad = radius
        else:
            self.rad = np.zeros(self.n) + 0.1
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
        """Calculate the new positions and speeds for all bubbles."""
        despl = self.vel * time_step
        self.pos = self.pos + despl
        if self.sizexyz[2] is not None:
            offbound = np.where(self.pos[:,2] > self.bound[2,1])
            off_n = offbound[0].size
            self.pos[offbound,0] = (self.sizexyz[0]) * np.random.rand(off_n) + self.bound[0,0]
            self.pos[offbound,1] = (self.sizexyz[1]) * np.random.rand(off_n) + self.bound[1,0]
            self.pos[offbound,2] = self.bound[2,0]
            self.rad[offbound] = 0.01
            self.vel[offbound,2] = 0.0
            on_bottom = np.where(self.pos[:,2] == self.bound[2,0])
            self.rad[on_bottom] = self.rad[on_bottom] + 0.02
            vel_free = self.vel[on_bottom,2][0]
            rad_free = self.rad[on_bottom]
            free = np.where(rad_free + np.random.rand(on_bottom[0].size) / 2 > 0.4)
            vel_free[free] = vel_free[free] + rad_free[free]
            self.vel[on_bottom,2] = vel_free
            not_on_bottom = np.where(self.pos[:,2] > self.bound[2,0])
            self.vel[not_on_bottom,2] = self.vel[not_on_bottom,2] + self.rad[not_on_bottom]
        self.update_visual()

    def init_visual(self, view):
        """Initialize the object visual."""
        num_seg = sphere_pt.shape[0]
        all_seg = np.zeros((num_seg * self.n, 3))
        for i in range(self.n):
            all_seg[i * num_seg: (i + 1) * num_seg] = sphere_pt * self.rad[i] + self.pos[i,:]
        self.visual = Line(pos = all_seg, color=self.color, connect='segments')
        view.add(self.visual)

    def update_visual(self):
        """Updates the object visual."""
        num_seg = sphere_pt.shape[0]
        all_seg = np.zeros((num_seg * self.n, 3))
        for i in range(self.n):
            all_seg[i * num_seg: (i + 1) * num_seg] = sphere_pt * self.rad[i] + self.pos[i,:]
        self.visual.set_data(pos = all_seg)

    def shake(self):
        """Loose all the bubbles from the bottom."""
        if self.sizexyz[2] is not None:
            self.pos[:,2] = self.pos[:,2] + 0.001

if __name__ == '__main__':
    print(Bubble2.__doc__)
    exit()
