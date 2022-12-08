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

for row in range(0, height):
  lineMax = -1
  for col in range(0, width):
    if forest[row][col][0] > lineMax:
      lineMax = forest[row][col][0]
      if not forest[row][col][1]:
        visible += 1
        forest[row][col][1] = True

  lineMax = -1
  for col in range(width - 1, -1, -1):
    if forest[row][col][0] > lineMax:
      lineMax = forest[row][col][0]
      if not forest[row][col][1]:
        visible += 1
        forest[row][col][1] = True

for col in range(0, width):
  lineMax = -1
  for row in range(0, height):
    if forest[row][col][0] > lineMax:
      lineMax = forest[row][col][0]
      if not forest[row][col][1]:
        visible += 1
        forest[row][col][1] = True

  lineMax = -1
  for row in range(height - 1, -1, -1):
    if forest[row][col][0] > lineMax:
      lineMax = forest[row][col][0]
      if not forest[row][col][1]:
        visible += 1
        forest[row][col][1] = True

print(visible)
