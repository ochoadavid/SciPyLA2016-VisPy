#!/usr/bin/python3
# -*- coding: utf-8 -*-
## Autor: David Ochoa

import numpy as np
#from vispy.scene.visuals import Line
from vispy.scene.visuals import Volume
from vispy import scene

class Ball:
    """Ball Class. It uses vispy to visualization."""
    def __init__(self, position, velocity, boundaries = None, color = (1.0, 1.0, 1.0, 1.0)):
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
        temp_mg = np.meshgrid(np.arange(41), np.arange(41), np.arange(41))
        self.meshgrid = np.asarray([temp_mg[0], temp_mg[2], temp_mg[1]])

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
        """Initialize the class visual."""
        ball_ln_dic = dict(color=self.color)
        dist_sq = np.zeros(self.meshgrid[0].shape)
        for i in range(3):
            axis_sq = np.multiply((self.meshgrid[i] - self.pos[i] * 4),
                                (self.meshgrid[i] - self.pos[i] * 4))
            dist_sq = dist_sq + axis_sq
        dist_sq = 4.0 - dist_sq
        dist_sq[dist_sq < 0] = 0
        self.visual = Volume(dist_sq, clim=(0.0, 10.0), method='mip',
                               emulate_texture=False, cmap='hot')
        self.visual.transform = scene.STTransform(scale=(.25, .25, .25))
        view.add(self.visual)
        self.last_dist_sq = dist_sq

    def update_visual(self):
        """Updates the class visual."""
        dist_sq = np.zeros(self.meshgrid[0].shape)
        for i in range(3):
            axis_sq = np.multiply((self.meshgrid[i] - self.pos[i] * 4),
                                (self.meshgrid[i] - self.pos[i] * 4))
            dist_sq = dist_sq + axis_sq
        dist_sq = 4.0 - dist_sq
        dist_sq[dist_sq < 0] = 0
        dist_sq = dist_sq + 0.99 * self.last_dist_sq
        self.visual.set_data(dist_sq)
        self.visual.update()
        self.last_dist_sq = dist_sq

    def shake(self):
        """Inverts the z position and gives the ball a random velocity."""
        if self.sizexyz[2] is not None:
            self.pos[2] = self.bound[2, 1] - (self.pos[2] - self.bound[2, 0])
            self.vel = (np.random.rand(3) - 0.5) * 10

if __name__ == '__main__':
    print(Ball.__doc__)
    exit()
