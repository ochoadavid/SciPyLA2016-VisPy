#!/usr/bin/python3
# -*- coding: utf-8 -*-
## Autor: David Ochoa

import numpy as np
from bubble import Bubble
from bworld import Bworld

n = 30
bubbles = []
for i in range(n):
    bubbles.append(Bubble(np.random.rand(3) * 10, np.zeros(3), radius = np.random.rand(1) / 6,
                    color = (0.5, 0.8, 1.0, 0.8)))

testworld = Bworld(bubbles, boundaries = np.asarray([[0, 20], [0,10], [0, 10]]))
