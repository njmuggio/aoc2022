# inputFile = "demo"
inputFile = "input"

with open(inputFile, "rt", encoding="utf-8") as file:
  cargoInit = []
  cargoStacks = []
  for line in file:
    if line.startswith(" 1 "):
      colCount = int(line.split(" ")[-1])

      for colNum in range(0, colCount):
        cargoStacks.append([])

      for cargoLine in cargoInit:
        for colNum in range(0, colCount):
          idx = colNum * 4 + 1
          if idx > len(cargoLine):
            break
          if cargoLine[idx] != " ":
            cargoStacks[colNum].insert(0, cargoLine[idx])

      # print(cargoStacks)
    elif len(line) == 0:
      continue
    elif line.startswith("move"):
      parts = line.split(" ")
      count = int(parts[1])
      source = int(parts[3]) - 1
      dest = int(parts[5]) - 1

      # print("\n" + line.strip())

      for i in range(0, count):
        crate = cargoStacks[source].pop()
        cargoStacks[dest].append(crate)
        # print(cargoStacks)
    else:
      cargoInit.append(line)


for stack in cargoStacks:
  print(stack[-1], end='')

print()
