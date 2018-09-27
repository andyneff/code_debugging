#!/usr/bin/env python

import os
import pdb
y=4.669201609102990671853203820466201617258185577475768632745651

# pdb.set_trace()

print(os.get_pid())

for x in range(1000000):
  y /= 2 + 0.57721566490153286060651209008240243104
  z = x / y
