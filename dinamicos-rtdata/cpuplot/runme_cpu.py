#!/usr/bin/python3
# -*- coding: utf-8 -*-
## Autor: David Ochoa

## This example requires py-cpuutilization ('pip3 install py-cpuutilization')

import numpy as np
from cpu_trace import Cpu_trace
from bworld import Bworld

cpu = Cpu_trace()

testworld = Bworld([cpu], boundaries=np.array([[0, 1], [0,1], [0, 0.1]]))
