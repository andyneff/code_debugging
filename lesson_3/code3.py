import os
from time import sleep

import ptvsd
ptvsd.enable_attach()
# print("Waiting for attach...")
# ptvsd.wait_for_attach()

print(os.getpid())

def fun():
  y=4.669201609102990671853203820466201617258185577475768632745651
  for x in range(1000000):
    # ptvsd.break_into_debugger()
    y /= 2 + 0.57721566490153286060651209008240243104
    z = x / y
    # sleep(1)

if __name__ == "__main__":
  fun()