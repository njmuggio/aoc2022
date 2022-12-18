# file = "demo"
file = "input"

with open(file, mode="rt") as file:
  points = set()
  mins = [99999, 99999, 99999]
  maxs = [-99999, -99999, -99999]

  for line in file:
    coords = line.split(",")
    points.add((int(coords[0]), int(coords[1]), int(coords[2])))

    mins[0] = min(mins[0], int(coords[0]))
    maxs[0] = max(maxs[0], int(coords[0]))

    mins[1] = min(mins[1], int(coords[1]))
    maxs[1] = max(maxs[1], int(coords[1]))

    mins[2] = min(mins[2], int(coords[2]))
    maxs[2] = max(maxs[2], int(coords[2]))

mins[0] -= 1
mins[1] -= 1
mins[2] -= 1

maxs[0] += 2
maxs[1] += 2
maxs[2] += 2

for x in range(mins[0], maxs[0]):
  for y in range(mins[1], maxs[1]):
    for z in range(mins[2], maxs[2]):
      if (x, y, z) in points:
        continue

      air = {(x, y, z)}
      prevLen = 0

      exposedToSteam = False

      while len(air) != prevLen and not exposedToSteam:
        prevLen = len(air)
        nextAir = set()
        for p in air:
          px = p[0]
          py = p[1]
          pz = p[2]

          if (px - 1, py, pz) not in points:
            nextAir.add((px - 1, py, pz))
          if (px + 1, py, pz) not in points:
            nextAir.add((px + 1, py, pz))
          if (px, py - 1, pz) not in points:
            nextAir.add((px, py - 1, pz))
          if (px, py + 1, pz) not in points:
            nextAir.add((px, py + 1, pz))
          if (px, py, pz - 1) not in points:
            nextAir.add((px, py, pz - 1))
          if (px, py, pz + 1) not in points:
            nextAir.add((px, py, pz + 1))

        air.update(nextAir)

        for p in air:
          if p[0] <= mins[0] or p[0] >= maxs[0] or p[1] <= mins[1] or p[1] >= maxs[1] or p[2] <= mins[2] or p[2] >= maxs[2]:
            exposedToSteam = True
            break
      if not exposedToSteam:
        points.update(air)

exposed = 0
for point in points:
  if (point[0] - 1, point[1], point[2]) not in points:
    exposed += 1
  if (point[0] + 1, point[1], point[2]) not in points:
    exposed += 1
  if (point[0], point[1] - 1, point[2]) not in points:
    exposed += 1
  if (point[0], point[1] + 1, point[2]) not in points:
    exposed += 1
  if (point[0], point[1], point[2] - 1) not in points:
    exposed += 1
  if (point[0], point[1], point[2] + 1) not in points:
    exposed += 1

print(exposed)
