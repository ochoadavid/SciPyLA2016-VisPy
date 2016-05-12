#!/usr/bin/python3
# -*- coding: utf-8 -*-
## Autor: David Ochoa

import numpy as np
from ball2 import Ball2
from bworld import Bworld

n = 1000
balls = []
balls.append(Ball2(np.random.rand(n, 3) * 10, (np.random.rand(n, 3) - 0.5) * 10,
              color =  (0.1, 0.3, 0.6, 1.0)))

testworld = Bworld(balls)
