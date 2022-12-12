# file = "demo"
file = "input"

with open(file, mode="rt", encoding="utf-8") as file:
  heights = []
  startX = 0
  startY = 0
  destX = 0
  destY = 0

  for line in file:
    line = line.strip()

    cur = []
    heights.append(cur)

    for c in line:
      if c == 'S':
        startX = len(cur)
        startY = len(heights) - 1
        cur.append(ord('a'))
      elif c == 'E':
        destX = len(cur)
        destY = len(heights) - 1
        cur.append(ord('z'))
      else:
        cur.append(ord(c))


distMap = []
rowCount = len(heights)
colCount = len(heights[0])
for row in heights:
  distMap.append([])
  for i in range(0, colCount):
    distMap[-1].append(99999999)

distMap[startY][startX] = 0

change = True

def printDist():
  r = -1
  for row in distMap:
    r += 1
    c = -1
    for col in row:
      c += 1
      if r == destY and c == destX:
        print('E', end='')
      else:
        if col < 99999999:
          print(chr(heights[r][c]), end='')
        else:
          print(' ', end='')
    print()
  print()

  import time
  time.sleep(0.2)

while change:
  change = False
  # printDist()
  for curY in range(0, rowCount):
    for curX in range(0, colCount):

      curHeight = heights[curY][curX]
      curDist = distMap[curY][curX]

      if curY > 0 and distMap[curY - 1][curX] > curDist + 1 and heights[curY - 1][curX] - curHeight <= 1:
        change = True
        distMap[curY - 1][curX] = curDist + 1

      if curY < rowCount - 1 and distMap[curY + 1][curX] > curDist + 1 and heights[curY + 1][curX] - curHeight <= 1:
        change = True
        distMap[curY + 1][curX] = curDist + 1

      if curX > 0 and distMap[curY][curX - 1] > curDist + 1 and heights[curY][curX - 1] - curHeight <= 1:
        change = True
        distMap[curY][curX - 1] = curDist + 1

      if curX < colCount - 1 and distMap[curY][curX + 1] > curDist + 1 and heights[curY][curX + 1] - curHeight <= 1:
        change = True
        distMap[curY][curX + 1] = curDist + 1

print(distMap[destY][destX])
