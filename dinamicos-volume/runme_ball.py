#!/usr/bin/python3
# -*- coding: utf-8 -*-
## Autor: David Ochoa

## THIS TUTORAIL NEEDS PYOPENGL

import numpy as np
from ball import Ball
from bworld import Bworld

n = 3
balls = []
#for i in range(n):
balls.append(Ball(np.random.rand(3) * 10, (np.random.rand(3) - 0.5) * 10,
                color =  np.random.rand(4)))

testworld = Bworld(balls)
