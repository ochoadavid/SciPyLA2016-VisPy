#!/usr/bin/python3
# -*- coding: utf-8 -*-
## Autor: David Ochoa

import numpy as np
from bubble2 import Bubble2
from bworld import Bworld

n = 1000
bubbles = []
bubbles.append(Bubble2(np.random.rand(n, 3) * 10, np.zeros((n, 3)),
                radius = (np.random.rand(n) / 6), color = (0.5, 0.8, 1.0, 0.8)))

testworld = Bworld(bubbles, boundaries = np.asarray([[0, 20], [0,10], [0, 10]]))
