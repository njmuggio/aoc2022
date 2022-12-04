# inputFile = "demo"
inputFile = "input"

with open(inputFile, "rt", encoding="utf-8") as file:
  count = 0
  for line in file:
    parts = line.split(",")
    aBounds = parts[0].split("-")
    bBounds = parts[1].split("-")
    lowA = int(aBounds[0])
    highA = int(aBounds[1])
    lowB = int(bBounds[0])
    highB = int(bBounds[1])

    if (lowA >= lowB and lowA <= highB) or (highA >= lowB and highA <= highB) or (lowB >= lowA and lowB <= highA) or (highB >= lowA and highB <= highA):
      count += 1

print(count)
