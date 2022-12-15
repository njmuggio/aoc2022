# filename = "demo"
filename = "input"

class Sensor:
  def __init__(self, sx, sy, bx, by) -> None:
    self.sx = sx
    self.sy = sy
    self.bx = bx
    self.by = by

  def dist(self) -> int:
    return abs(self.sx - self.bx) + abs(self.sy - self.by)

  def inRange(self, x, y) -> bool:
    return abs(self.sx - x) + abs(self.sy - y) <= self.dist()

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

row = 2000000 if filename == "input" else 10

blocked = 0

covered = []

for s in sensors:
  d = s.dist()
  if abs(s.sy - d) <= row:
    width = d - abs(row - s.sy)
    left = s.sx - width
    right = s.sx + width
    covered.append((left, right))

covered.sort(key=lambda k: k[0])

maxX = -9999999999
ranges = [range(covered[0][0], covered[0][1] + 1)]
blocked += covered[0][1] - covered[0][0] + 1
for i in range(1, len(covered)):
  prev = covered[i - 1]
  cur = covered[i]

  if cur[1] <= maxX:
    continue

  if cur[0] <= maxX:
    cur = (maxX + 1, cur[1])

  if cur[0] <= prev[1]:
    cur = (prev[1] + 1, cur[1])

  if cur[0] > cur[1]:
    continue


  blocked += cur[1] - cur[0] + 1
  ranges.append(range(cur[0], cur[1] + 1))
  maxX = cur[1]

beaconSpots = []
for s in sensors:
  if s.by != row:
    continue

  beaconAddr = (s.bx, s.by)

  for r in ranges:
    if s.by == row and s.bx in r and not beaconAddr in beaconSpots:
      blocked -= 1
      beaconSpots.append(beaconAddr)
      break

print(blocked)
