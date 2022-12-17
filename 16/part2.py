file = "demo"
# file = "input"

class Valve:
  def __init__(self, name: str, rate: int, dests: list[str]) -> None:
    self.name = name
    self.rate = rate
    self.dests = {}
    for name in dests:
      self.dests[name] = None
    self.maxVal = {(0, ""): 0}

  def update(self, valves):
    for key in self.dests.keys():
      self.dests[key] = valves[key]


  def findMaxValue(self, remaining: int, openValves: str) -> int:
    if (remaining, openValves) in self.maxVal:
      return self.maxVal[(remaining, openValves)]

    if remaining == 0:
      return 0

    maxVal = 0

    if self.rate > 0 and self.name not in openValves and remaining > 2:
      releaseValue = self.rate * (remaining - 1)
      withOpen = openValves + " " + self.name

      for myDest in self.dests.values():
        value = releaseValue + myDest.findMaxValue(remaining - 2, withOpen)

        for elephantDest in self.dests.values():
          value += elephantDest.findMaxValue(remaining - 2, withOpen)

        if value > maxVal:
          maxVal = value
          # print(f"{self.name} open -> {myDest.name}")


    for dest in self.dests.values():
      value = dest.findMaxValue(remaining - 1, openValves)

      for elephantDest in self.dests.values():
          value += elephantDest.findMaxValue(remaining - 2, openValves)

      if value > maxVal:
        maxVal = value
        # print(f"{self.name}      -> {dest.name}")

    self.maxVal[(remaining, openValves)] = maxVal
    return maxVal


with open(file, mode="rt") as file:

  valves = {}

  for line in (line.strip() for line in file):
    words = line.split(" ")
    name = words[1]
    rate = int(words[4][5:-1])
    dests = []
    for i in range(9, len(words)):
      if words[i][-1] == ",":
        dests.append(words[i][:-1])
      else:
        dests.append(words[i])

    valve = Valve(name, rate, dests)
    valves[name] = valve

for valve in valves.values():
  valve.update(valves)

for i in range(1, 27):
  for valve in valves.values():
    valve.findMaxValue(i, "")

print(valves["AA"].findMaxValue(26, ""))
