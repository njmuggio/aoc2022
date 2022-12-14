# file = "demo"
file = "input"

ROCK = 0
AIR = 1
SAND = 2

with open(file, mode="rt", encoding="utf-8") as file:
  segments = []
  minX = 9999999
  maxX = -9999999

  maxY = -9999999

  for line in file:
    points = line.split(" -> ")
    for i in range(1, len(points)):
      p0 = points[i - 1].split(",")
      p0 = (int(p0[0]), int(p0[1]))
      p1 = points[i].split(",")
      p1 = (int(p1[0]), int(p1[1]))
      segments.append((p0, p1))

      minX = min(minX, p0[0], p1[0])
      maxX = max(maxX, p0[0], p1[0])

      maxY = max(maxY, p0[1], p1[1])

def printGrid():
  for r in grid:
    for c in r:
      if c == ROCK:
        print("#", end="")
      elif c == AIR:
        print(".", end="")
      else:
        print("o", end="")
    print()
  print()


grid = []
minX -= 1
maxX += 1
maxY += 1
entry = 500 - minX

for r in range(0, maxY):
  row = []
  grid.append(row)

  for c in range(minX, maxX):
    row.append(AIR)

origSegments = segments
segments = []

for segment in origSegments:
  def _x(i):
    return i - minX

  def _y(i):
    return i
  segments.append(((_x(segment[0][0]), _y(segment[0][1])), (_x(segment[1][0]), _y(segment[1][1]))))

for segment in segments:
  p0 = segment[0]
  p1 = segment[1]

  if p0[0] == p1[0]: # vertical segment
    x = p0[0]
    for y in range(min(p0[1], p1[1]), max(p0[1], p1[1]) + 1):
      grid[y][x] = ROCK

  else: # horiz segment
    y = p0[1]
    for x in range(min(p0[0], p1[0]), max(p0[0], p1[0]) + 1):
      grid[y][x] = ROCK

def addGrain():
  x = entry
  y = 0

  while True:
    if y + 1 == len(grid):
      return False

    if grid[y + 1][x] == AIR:
      y += 1
      continue

    if grid[y + 1][x - 1] == AIR:
      y += 1
      x -= 1
      continue

    if grid[y + 1][x + 1] == AIR:
      y += 1
      x += 1
      continue

    break

  grid[y][x] = SAND
  # printGrid()
  return True


count = 0
while addGrain():
  count += 1

print(count)
