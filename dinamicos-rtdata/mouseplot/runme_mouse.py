#!/usr/bin/python3
# -*- coding: utf-8 -*-
## Autor: David Ochoa

## This example requires PyUserInput ('pip3 install PyUserInput')

import numpy as np
from mouse_trace import Mouse_trace
from bworld import Bworld

mouse = Mouse_trace()

testworld = Bworld([mouse], boundaries=mouse.bound)
