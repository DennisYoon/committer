from datetime import datetime
from time import sleep
from os import system as exe

n = 0

repeat = 10
term = 1

with open("n.txt") as f:
  ns = f.read()
  n = int(ns)

def string(count, date):
  returning = "# COMMITTER\n\n{}th commit\n{}".format(count, date)
  return returning

for i in range(n, n + repeat, 1):
  pushingStr = string(i, datetime.now())
  with open("README.md", "w") as f:
    f.write(pushingStr)
  sleep(term)

with open("n.txt", "w") as f:
  f.write(str(n + repeat))