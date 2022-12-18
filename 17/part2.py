file = "demo"
# file = "input"

with open(file, mode="rt") as file:
  dirs = []
  line = file.readline()
  for c in line:
    if c == "<":
      dirs.append(-1)
    elif c == ">":
      dirs.append(1)


# dashPts = [0, 1, 2, 3]
dashPts = [0b0011110]
# plusPts = [1, 7, 8, 9, 15]
plusPts = [0b0001000, 0b0011100, 0b0001000]
# cornerPts = [0, 1, 2, 9, 16]
cornerPts = [0b0011100, 0b0000100, 0b0000100]
# pipePts = [0, 7, 14, 21]
pipePts = [0b0010000, 0b0010000, 0b0010000, 0b0010000]
# boxPts = [0, 1, 7, 8]
boxPts = [0b0011000, 0b0011000]

shapeOrder = [dashPts, plusPts, cornerPts, pipePts, boxPts]
# col = [0, 1, 2, 3, 4, 5, 6]
col = [0b1111111]
# activeShape = None
jetIdx = 0
shapeIdx = 0

class Shape:
  def __init__(self, pts, row) -> None:
    global width
    global col
    self.pts = pts.copy()
    self.row = row

  def applyJet(self, xOffset):
    # print(self.pts, "-> ", end="")
    global col

    if xOffset == 1:
      # print("right?")
      if next((pt for pt in self.pts if pt & 0b0000001), False):
        # print("  edge")
        return
      for i, pt in enumerate(self.pts):
        if self.row + i < len(col) and (pt >> 1) & col[self.row + i]:
          return
      # print("  right!")
      for i, pt in enumerate(self.pts):
        self.pts[i] = pt >> 1
    else:
      # print("left?")
      if next((pt for pt in self.pts if pt & 0b1000000), False):
        # print("  edge")
        return
      for i, pt in enumerate(self.pts):
        if self.row + i < len(col) and (pt << 1) & col[self.row + i]:
          return
      # print("  left!")
      for i, pt in enumerate(self.pts):
        self.pts[i] = pt << 1

    # curRows = []
    # for pt in self.pts:
    #   curRows.append(pt // width)

    # newRows = []
    # for pt in self.pts:
    #   newRows.append((pt + xOffset) // width)

    # collide = False
    # for pt in self.pts:
    #   if pt + xOffset in col:
    #     collide = True
    #     break

    # if not collide and curRows == newRows:
    #   for i in range(len(self.pts)):
    #     self.pts[i] += xOffset
    # # print(self.pts, f"({xOffset})")

  def applyGravity(self) -> bool:
    global col

    # print("testing", self.row, "->", self.row - 1)
    if self.row > len(col):
      self.row -= 1
      return False

    for i, pt in enumerate(self.pts):
      # print(f"  {self.row + i - 1}:  {pt:07b}")
      if self.row + i - 1 < len(col) and pt & col[self.row + i - 1]:
        # print(self.row, i, pt, col[self.row + i - 1], pt & col[self.row + i - 1])
        return True
    self.row -= 1
    return False

    # global width
    # global col
    # for pt in self.pts:
    #   if (pt - width) in col:
    #     return True
    # for i in range(len(self.pts)):
    #   self.pts[i] -= width
    # # print("    ", self.pts)
    # return False

def printField():
  for i in range(len(col) - 1, -1, -1):
    print(f"{i:04}: {rowStr(col[i])}")
  print("---------------")

def rowStr(row):
  s = ""
  if row & 0b1000000:
    s += "#"
  else:
    s += "."
  if row & 0b100000:
    s += "#"
  else:
    s += "."
  if row & 0b10000:
    s += "#"
  else:
    s += "."
  if row & 0b1000:
    s += "#"
  else:
    s += "."
  if row & 0b100:
    s += "#"
  else:
    s += "."
  if row & 0b10:
    s += "#"
  else:
    s += "."
  if row & 0b1:
    s += "#"
  else:
    s += "."
  return s


activeShape = Shape(shapeOrder[0], 4)
shapeIdx = 1

shapesCount = len(shapeOrder)
dirsLen = len(dirs)

for i in range(0, 2022):
# for i in range(0, 1000000000000):
# while shapeIdx < 1000000000000 + 1:
  activeShape.applyJet(dirs[jetIdx])
  jetIdx += 1
  if jetIdx == dirsLen:
    jetIdx = 0

  while not activeShape.applyGravity():
    activeShape.applyJet(dirs[jetIdx])
    jetIdx += 1
    if jetIdx == dirsLen:
      jetIdx = 0

  for i, pt in enumerate(activeShape.pts):
    row = activeShape.row + i
    # print(row)

    if row < len(col):
      col[row] |= pt
    else:
      col.append(pt)

  activeShape = Shape(shapeOrder[shapeIdx % len(shapeOrder)], len(col) + 3)
  shapeIdx += 1
  if shapeIdx == shapesCount:
    shapeIdx = 0

  for i in range(0, len(col) // 2):
    recentSlice = col[-i - 1:]
    olderSlice = col[2 * (-i - 1):-i - 1]

    if recentSlice == olderSlice:
      print("COL LOOP FOUND")

  # printField()

print(len(col) - 1)
