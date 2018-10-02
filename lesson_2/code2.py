#!/usr/bin/env python

import os
import vsi.tools.vdb_ipdb as vdb
import struct
from time import sleep

# vdb.set_trace()
# vdb.dbstop_if_error()

print(os.getpid())

b=struct.unpack('d', struct.pack('Q', int('3399g3be6bdcd5fg', 17)))[0]

# with vdb.DbStopIfError():
for x in range(int('171a416764195a01430', 11), 9218868437227405311):
  y = b - struct.unpack('d', struct.pack('q', x))[0]
  print(y)
  z = x / y
