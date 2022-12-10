# file = "demo"
file = "input"

with open(file, mode="rt", encoding="utf-8") as file:
  tailPos = set()

  head = (0, 0)
  tail = (0, 0)

  for line in (line.strip() for line in file):
    if len(line) == 0:
      continue

    direction, steps = line.split(" ")
    steps = int(steps)

    for i in range(0, steps):
      if direction == "U":
        head = (head[0], head[1] + 1)
      elif direction == "D":
        head = (head[0], head[1] - 1)
      elif direction == "L":
        head = (head[0] - 1, head[1])
      else:
        head = (head[0] + 1, head[1])

      x = 0
      y = 0

      if head[0] == tail[0] + 2:
        x = 1
        if head[1] > tail[1]:
          y = 1
        elif head[1] < tail[1]:
          y = -1
      elif head[0] == tail[0] - 2:
        x = -1
        if head[1] > tail[1]:
          y = 1
        elif head[1] < tail[1]:
          y = -1
      elif head[1] == tail[1] + 2:
        y = 1
        if head[0] > tail[0]:
          x = 1
        elif head[0] < tail[0]:
          x = -1
      elif head[1] == tail[1] - 2:
        y = -1
        if head[0] > tail[0]:
          x = 1
        elif head[0] < tail[0]:
          x = -1

      tail = (tail[0] + x, tail[1] + y)

      tailPos.add(tail)

print(len(tailPos))
