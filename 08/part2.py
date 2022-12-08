# file = "demo"
file = "input"

with open(file, mode="rt", encoding="utf-8") as file:
  forest = []

  for line in file:
    row = []
    forest.append(row)
    for c in line.strip():
      row.append([int(c), False])

height = len(forest)
width = len(forest[0])

visible = 0

def countVis(x0, y0):
  maxHeight = forest[y0][x0][0]

  up = 0
  for y in range(y0 - 1, -1, -1):
    if forest[y][x0][0] < maxHeight:
      up += 1
    else:
      up += 1
      break

  down = 0
  for y in range(y0 + 1, height):
    if forest[y][x0][0] < maxHeight:
      down += 1
    else:
      down += 1
      break

  left = 0
  for x in range(x0 - 1, -1, -1):
    if forest[y0][x][0] < maxHeight:
      left += 1
    else:
      left += 1
      break

  right = 0
  for x in range(x0 + 1, width):
    if forest[y0][x][0] < maxHeight:
      right += 1
    else:
      right += 1
      break

  return up * down * left * right

maxVis = 0
for row in range(0, height):
  for col in range(0, width):
    vis = countVis(col, row)
    if vis > maxVis:
      maxVis = vis

print(maxVis)
