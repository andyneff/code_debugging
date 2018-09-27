#!/usr/bin/env python

import os
import vsi.tools.vdb as vdb
y=0.57721566490153286060651209008240243104

vdb.set_trace()
# vdb.dbstop_if_error()

print(os.getpid())

for x in range(1000):
  y /= 4.669201609102990671853203820466201617258185577475768632745651
  z = x / y
