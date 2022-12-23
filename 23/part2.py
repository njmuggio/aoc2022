# file = "demo"
# file = "demo2"
file = "input"

class Elf:
  def __init__(self, x, y) -> None:
    self.x = x
    self.y = y
    self.destX = 0
    self.destY = 0
    self.dirKey = 0
    self.shouldMove = False

  def __repr__(self) -> str:
    return f"({self.x}, {self.y})"

  def identifyDest(self, elfPts):
    x = self.x
    y = self.y

    hasNeighbor = False
    for xoff in range(-1, 2):
      for yoff in range(-1, 2):
        if xoff == 0 and yoff == 0:
          continue
        if (x + xoff, y + yoff) in elfPts:
          hasNeighbor = True

    if not hasNeighbor:
      self.dirKey += 1
      return None

    for i in range(5):
      if (i + self.dirKey) % 4 == 0:
        if (x - 1, y - 1) not in elfPts and (x, y - 1) not in elfPts and (x + 1, y - 1) not in elfPts:
          self.shouldMove = True
          self.destX = x
          self.destY = y - 1
          break
      elif (i + self.dirKey) % 4 == 1:
        if (x - 1, y + 1) not in elfPts and (x, y + 1) not in elfPts and (x + 1, y + 1) not in elfPts:
          self.shouldMove = True
          self.destX = x
          self.destY = y + 1
          break
      elif (i + self.dirKey) % 4 == 2:
        if (x - 1, y - 1) not in elfPts and (x - 1, y) not in elfPts and (x - 1, y + 1) not in elfPts:
          self.shouldMove = True
          self.destX = x - 1
          self.destY = y
          break
      elif (i + self.dirKey) % 4 == 3:
        if (x + 1, y - 1) not in elfPts and (x + 1, y) not in elfPts and (x + 1, y + 1) not in elfPts:
          self.shouldMove = True
          self.destX = x + 1
          self.destY = y
          break

    self.dirKey += 5

    if self.shouldMove:
      return (self.destX, self.destY)
    return None

  def move(self):
    if self.shouldMove:
      self.x = self.destX
      self.y = self.destY
      self.shouldMove = False
      return True
    return False


with open(file, mode="rt") as file:
  elves = []

  for y, line in enumerate(file):
    for x, c in enumerate(line.strip()):
      if c == '#':
        elves.append(Elf(x, y))

# print(elves)

def printGrid():
  elfPts = set()

  for elf in elves:
    elfPts.add((elf.x, elf.y))

  minX = min(0, min(elf.x for elf in elves))
  maxX = max(13, max(elf.x for elf in elves))
  minY = min(0, min(elf.y for elf in elves))
  maxY = max(11, max(elf.y for elf in elves))

  for y in range(minY, maxY + 1):
    for x in range(minX, maxX + 1):
      if (x, y) in elfPts:
        print("#", end="")
      else:
        print(".", end="")
    print()
  print()


moved = True
rounds = 0
while moved:
  rounds += 1
  moved = False

  elfPts = set()
  destPts = {}

  for elf in elves:
    elfPts.add((elf.x, elf.y))

  for elf in elves:
    pt = elf.identifyDest(elfPts)
    if pt:
      if pt in destPts:
        destPts[pt].append(elf)
        for e in destPts[pt]:
          e.shouldMove = False
      else:
        destPts[pt] = [elf]

  for elf in elves:
    if elf.move():
      moved = True

  # print(f"End of round {rounds}")
  # printGrid()


print(rounds)
