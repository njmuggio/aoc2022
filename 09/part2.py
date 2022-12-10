# file = "demo2"
file = "input"

with open(file, mode="rt", encoding="utf-8") as file:
  tailPos = set()

  knots = []
  for i in range(0, 10):
    knots.append((0, 0))

  for line in (line.strip() for line in file):
    if len(line) == 0:
      continue

    direction, steps = line.split(" ")
    steps = int(steps)

    for i in range(0, steps):
      if direction == "U":
        knots[0] = (knots[0][0], knots[0][1] + 1)
      elif direction == "D":
        knots[0] = (knots[0][0], knots[0][1] - 1)
      elif direction == "L":
        knots[0] = (knots[0][0] - 1, knots[0][1])
      else:
        knots[0] = (knots[0][0] + 1, knots[0][1])

      for i in range(1, 10):
        lead = knots[i - 1]
        knot = knots[i]
        x = 0
        y = 0

        if lead[0] == knot[0] + 2:
          x = 1
          if lead[1] > knot[1]:
            y = 1
          elif lead[1] < knot[1]:
            y = -1
        elif lead[0] == knot[0] - 2:
          x = -1
          if lead[1] > knot[1]:
            y = 1
          elif lead[1] < knot[1]:
            y = -1
        elif lead[1] == knot[1] + 2:
          y = 1
          if lead[0] > knot[0]:
            x = 1
          elif lead[0] < knot[0]:
            x = -1
        elif lead[1] == knot[1] - 2:
          y = -1
          if lead[0] > knot[0]:
            x = 1
          elif lead[0] < knot[0]:
            x = -1

        knots[i] = (knots[i][0] + x, knots[i][1] + y)

      tailPos.add(knots[-1])

print(len(tailPos))
