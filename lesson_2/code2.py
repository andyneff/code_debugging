#!/usr/bin/env python

import os
import vsi.tools.vdb_ipdb as vdb
import struct
from time import sleep

# vdb.set_trace()
# vdb.dbstop_if_error()

print(os.getpid())

b=struct.unpack('d', b'\xff\xff\xff\xff\xff\xff\x7f\x7f')[0]

# with vdb.DbStopIfError():
for x in range(0o0775777777777567307000, 9218868437227405311):
  y = b - struct.unpack('d', struct.pack('q', x))[0]
  # print(y)
  z = x / y
