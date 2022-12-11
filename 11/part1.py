# file = "demo"
file = "input"

class Monkey:
  def __init__(self) -> None:
    self.items = []
    self.opIsAdd = False
    self.opVal = 0
    self.test = 0
    self.trueDest = 0
    self.falseDest = 0
    self.throwCount = 0

  def turn(self, monkeys):
    self.throwCount += len(self.items)
    while self.items:
      val = self.items.pop(0)
      old = val

      if self.opVal == "old":
        opVal = old
      else:
        opVal = self.opVal

      if self.opIsAdd:
        val = old + opVal
      else:
        val = old * opVal

      val = val // 3

      if val % self.test == 0:
        monkeys[self.trueDest].items.append(val)
      else:
        monkeys[self.falseDest].items.append(val)

  def __repr__(self) -> str:
    return str(self.items)


with open(file, mode="rt", encoding="utf-8") as file:
  monkeys = []

  try:
    while True:
      m = Monkey()
      file.readline()
      items = file.readline().split(" ")[2:]
      for item in items[2:]:
        if item.endswith(","):
          m.items.append(int(item[:-1]))
        else:
          m.items.append(int(item))

      opLine = file.readline().split(" ")
      m.opIsAdd = "+" == opLine[-2]
      try:
        m.opVal = int(opLine[-1])
      except:
        m.opVal = "old"

      testLine = file.readline().split(" ")
      m.test = int(testLine[-1])

      trueLine = file.readline().split(" ")
      m.trueDest = int(trueLine[-1])

      falseLine = file.readline().split(" ")
      m.falseDest = int(falseLine[-1])

      monkeys.append(m)

      file.readline()
  except:
    pass

  for i in range(0, 20):
    for m in monkeys:
      m.turn(monkeys)


  monkeys.sort(key=lambda m: m.throwCount)
  print(monkeys[-1].throwCount * monkeys[-2].throwCount)
