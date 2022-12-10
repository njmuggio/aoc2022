# file = "demo"
file = "input"

class Machine:
  def __init__(self, instructions):
    self.instructions = instructions
    self.cycle = 0
    self.x = 1
    self.pc = 0

  def run(self) -> int:
    ret = 0
    while self.pc < len(self.instructions):
      self.cycle += 1
      if self.cycle == 20 or (self.cycle - 20) % 40 == 0:
        ret += self.x * self.cycle

      self.instructions[self.pc].step(self)

    return ret


class Noop:
  def __init__(self):
    pass

  def step(self, m: Machine):
    m.pc += 1


class Addx:
  def __init__(self, val: int) -> None:
    self.val = val
    self.cycle = 0

  def step(self, m: Machine):
    self.cycle += 1

    if self.cycle == 2:
      m.pc += 1
      m.x += self.val


with open(file, mode="rt", encoding="utf-8") as file:
  instructions = []
  for line in file:
    if line.startswith("noop"):
      instructions.append(Noop())
    elif line.startswith("addx"):
      instructions.append(Addx(int(line.split(" ")[1])))

  m = Machine(instructions)
  print(m.run())
