#!/usr/bin/python3
# -*- coding: utf-8 -*-
## Autor: David Ochoa

import numpy as np
from balloon import Balloon
from bworld import Bworld

n = 30
balloons = []
for i in range(n):
    balloons.append(Balloon(np.random.rand(3) * 10, (np.random.rand(3) - 0.5) * 10,
                    color =  np.random.rand(4) / 2 + 0.5))

testworld = Bworld(balloons)
