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

class Ball2:
    """Class containg a n number of balls. It uses vispy to visualization."""
    def __init__(self, position, velocity, boundaries = None, color = (1.0, 1.0, 1.0, 1.0)):
        self.n = position.shape[0]
        self.pos = position
        self.vel = velocity
        self.color = color
        self.rad = 0.1
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
        """Calculate the new positions and speeds for all balls."""
        despl = self.vel * time_step
        self.pos = self.pos + despl
        for i in range(3):
            if self.sizexyz[i] is not None:
#-INF                offbound = np.where(self.pos[:,i] < self.bound[i,0])
#-INF                self.pos[offbound,i] = self.pos[offbound,i] + self.sizexyz[i]
#-INF                offbound = np.where(self.pos[:,i] > self.bound[i,1])
#-INF                self.pos[offbound,i] = self.pos[offbound,i] - self.sizexyz[i]
                offbound = np.where(self.pos[:,i] < self.bound[i,0])
                self.pos[offbound,i] = self.pos[offbound,i] - despl[offbound,i]
                self.vel[offbound,i] = - self.vel[offbound,i] * 0.8
                offbound = np.where(self.pos[:,i] > self.bound[i,1])
                self.pos[offbound,i] = self.pos[offbound,i] - despl[offbound,i]
                self.vel[offbound,i] = - self.vel[offbound,i] * 0.95
        self.vel[:,2] = self.vel[:,2] - 0.1
        self.update_visual()

    def init_visual(self, view):
        """Initialize the object visual."""
        num_seg = sphere_pt.shape[0]
        all_seg = np.zeros((num_seg * self.n, 3))
        for i in range(self.n):
            all_seg[i * num_seg: (i + 1) * num_seg] = sphere_pt * self.rad + self.pos[i,:]
        self.visual = Line(pos = all_seg, color=self.color, connect='segments')
        view.add(self.visual)

    def update_visual(self):
        """Updates the object visual."""
        num_seg = sphere_pt.shape[0]
        all_seg = np.zeros((num_seg * self.n, 3))
        for i in range(self.n):
            all_seg[i * num_seg: (i + 1) * num_seg] = sphere_pt * self.rad + self.pos[i,:]
        self.visual.set_data(pos = all_seg)

    def shake(self):
        """Inverts the z position and gives all the balls random velocity."""
        if self.sizexyz[2] is not None:
            self.pos[:,2] = self.bound[2, 1] - (self.pos[:,2] - self.bound[2, 0])
            self.vel = (np.random.rand(self.n, 3) - 0.5) * 10

if __name__ == '__main__':
    print(Ball2.__doc__)
    exit()
