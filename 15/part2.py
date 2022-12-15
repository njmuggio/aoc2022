# filename = "demo"
filename = "input"

rightBottom = 4000000 if filename == "input" else 20

class Sensor:
  def __init__(self, sx, sy, bx, by) -> None:
    self.sx = sx
    self.sy = sy
    self.bx = bx
    self.by = by
    self.dist = abs(self.sx - self.bx) + abs(self.sy - self.by)

    self.edgeLen = self.dist + 1

  def inRange(self, x, y) -> bool:
    return abs(self.sx - x) + abs(self.sy - y) <= self.dist

  def getEdge(self):
    edge = []

    for x in range(self.sx - self.dist - 1, self.sx + self.dist + 2):
      if x < 0 or x > rightBottom:
        continue

      yOff = self.dist + 1 - abs(self.sx - x)
      y = self.sy + yOff

      if y >= 0 and y <= rightBottom:
        edge.append((x, y))

      y = self.sy - yOff
      if y != self.sy and y >= 0 and y <= rightBottom:
        edge.append((x, y))

    return edge

with open(filename, mode="rt") as file:
  sensors = []

  for line in file:
    if len(line) == 0:
      continue

    parts = line.split("=")
    sx = int(parts[1].split(",")[0])
    sy = int(parts[2].split(":")[0])
    bx = int(parts[3].split(",")[0])
    by = int(parts[4])

    sensors.append(Sensor(sx, sy, bx, by))

edges = []
for s in sensors:
  edges += s.getEdge()
  print(len(edges))

i = 0
for point in edges:
  i += 1

  if i % 1000000 == 0:
    print(i)
  for s in sensors:
    if s.inRange(point[0], point[1]):
      break
  else:
    print(point[0] * 4000000 + point[1])
    exit()
