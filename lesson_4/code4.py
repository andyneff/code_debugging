import time

print(111)

def fun():
  for x in range(1000):
    print(x)
    time.sleep(1)

if __name__ == '__main__':
  fun()