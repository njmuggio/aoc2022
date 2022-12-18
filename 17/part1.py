# file = "demo"
file = "input"

with open(file, mode="rt") as file:
  dirs = []
  line = file.readline()
  for c in line:
    if c == "<":
      dirs.append(-1)
    elif c == ">":
      dirs.append(1)


dashPts = [0, 1, 2, 3]
plusPts = [1, 7, 8, 9, 15]
cornerPts = [0, 1, 2, 9, 16]
pipePts = [0, 7, 14, 21]
boxPts = [0, 1, 7, 8]

shapeOrder = [dashPts, plusPts, cornerPts, pipePts, boxPts]
col = [0, 1, 2, 3, 4, 5, 6]
width = 7
spawnCol = 2
activeShape = None
jetIdx = 0
shapeIdx = 0

class Shape:
  def __init__(self, pts, spawnRow, spawnCol) -> None:
    global width
    global col
    self.pts = [pt + spawnCol + spawnRow * width for pt in pts]

  def applyJet(self, xOffset):
    # print(self.pts, "-> ", end="")
    global col
    curRows = []
    for pt in self.pts:
      curRows.append(pt // width)

    newRows = []
    for pt in self.pts:
      newRows.append((pt + xOffset) // width)

    collide = False
    for pt in self.pts:
      if pt + xOffset in col:
        collide = True
        break

    if not collide and curRows == newRows:
      for i in range(len(self.pts)):
        self.pts[i] += xOffset
    # print(self.pts, f"({xOffset})")

  def applyGravity(self) -> bool:
    global width
    global col
    for pt in self.pts:
      if (pt - width) in col:
        return True
    for i in range(len(self.pts)):
      self.pts[i] -= width
    # print("    ", self.pts)
    return False

def printField():
  s = ""
  for i in range(0, max(col) + 1):
    if i % 7 == 0:
      s += "\n"
    if i in col:
      s += "#"
    else:
      s += "."

  lines = s.split("\n")
  lines.reverse()
  print("\n".join(lines))
  print("-------------------------")

while shapeIdx < 2023:
  if activeShape is None:
    # print("new shape")
    activeShape = Shape(shapeOrder[shapeIdx % len(shapeOrder)], max(col) // 7 + 4, spawnCol)
    shapeIdx += 1

  activeShape.applyJet(dirs[jetIdx % len(dirs)])
  jetIdx += 1

  if activeShape.applyGravity():
    # print("collide")
    col += activeShape.pts
    activeShape = None
    # printField()

  # printField()

print(max(col) // 7)
