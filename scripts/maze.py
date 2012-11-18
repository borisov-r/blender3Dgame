#! /usr/bin/env python3

import random

def field(width, height):
  fld = []
  for i in range(0, height):
    line = []
    fld.append(line)
    for j in range(0, width):
      line.append(0)
  return fld

def maze(fld, startX, startY, endX, endY, pathLength):
#  if fld[startY][startX] == 1:
#    return fld
  fld[startY][startX] = 1
  print("pathLength=", pathLength)
  if startX == endX and startY == endY:
    return fld
#  if (pathLength == 0):
#    return fld
#  stopPath = int(random.random() * 10)
#  if stopPath <= 20:
#    return fld
  while True:
    next = int(random.random() * 4)
    if next == 0: # up
      if startY > 0:
        return maze(fld, startX, startY - 1, endX, endY, pathLength - 1)
    elif next == 1: # down
      if startY < len(fld) - 1:
        return maze(fld, startX, startY + 1, endX, endY, pathLength - 1)
    elif next == 2: # left
      if startX > 0:
        return maze(fld, startX - 1, startY, endX, endY, pathLength - 1)
    elif next == 3: # right
      if startX < len(fld[0]) - 1:
        return maze(fld, startX + 1, startY, endX, endY, pathLength - 1)

def printMaze(fld):
  for line in fld:
    for cell in line:
      print(cell, end=" ")
    print()

printMaze(maze(field(5, 5), 2, 2, 4, 4, pathLength=4))

