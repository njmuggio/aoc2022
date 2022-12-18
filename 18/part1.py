# file = "demo"
file = "input"

with open(file, mode="rt") as file:
  points = set()

  for line in file:
    coords = line.split(",")
    points.add((int(coords[0]), int(coords[1]), int(coords[2])))

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
