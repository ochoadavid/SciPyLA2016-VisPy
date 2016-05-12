#!/usr/bin/python3
# -*- coding: utf-8 -*-
## Autor: David Ochoa

import numpy as np
from vispy.scene.visuals import Line
from cpuutilization import cpuutilization

class Cpu_trace:
    """Mouse tracing Class. It uses vispy to visualization."""
    def __init__(self, color = (1.0, 1.0, 1.0, 1.0)):
        self.pos = np.asarray([0, 0, 0], dtype = np.float32)
        self.color = color
        self.sizexyz = [None] * 3
        self.tail_steps = 100
        self.bound = None
        self.visual = [None]

    def set_bound(self, boundaries):
        """Updates the boundaries."""
        self.bound = boundaries
        self.sizexyz = np.abs(boundaries[:,1] - boundaries[:,0])

    def step(self, time_step):
        """Calculate the new position and speed."""
        cpu = np.float(cpuutilization.get_utilization())
        self.pos = np.asarray([100, cpu, 0])
        self.update_visual()

    def init_visual(self, view):
        """Initialize the object visual."""
        self.trace = np.repeat(self.pos, self.tail_steps).reshape((3,self.tail_steps)).T
        self.trace[:,0] = range(self.tail_steps,0,-1)
        self.trace = self.trace / 100
        self.visual = Line(pos = self.trace, color=self.color)
        view.add(self.visual)

    def update_visual(self):
        """Updates the object visual."""
        self.trace[1:,1] = self.trace[0:-1,1]
        self.trace[0] = self.pos / 100
        self.visual.set_data(pos = self.trace)

    def shake(self):
        """Inverts the z position and gives the ball a random velocity."""
        pass

if __name__ == '__main__':
    print(Ball_trace.__doc__)
    exit()
