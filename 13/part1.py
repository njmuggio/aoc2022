# file = "demo"
file = "input"

with open(file, mode="rt", encoding="utf-8") as file:
  lists = []
  for line in file:
    line = line.strip()
    if len(line) > 0:
      lists.append(eval(line))

CORRECT = -1
NO_DET = 0
INCORRECT = 1

def handlePair(left, right, depth=0):
  if isinstance(left, list) and isinstance(right, list):
    print(depth * "  " + f"- Compare {left} vs {right}")
    for i in range(0, len(left)):
      if i >= len(right):
        return INCORRECT
      status = handlePair(left[i], right[i], depth + 1)
      if status == CORRECT or status == INCORRECT:
        return status
    if len(left) < len(right):
      return CORRECT
  elif isinstance(left, int) and isinstance(right, int):
    print(depth * "  " + f"- Compare {left} vs {right}")
    if left < right:
      return CORRECT
    if left == right:
      return NO_DET
    return INCORRECT
  else:
    if isinstance(left, int):
      return handlePair([left], right, depth + 1)
    else:
      return handlePair(left, [right], depth + 1)

total = 0
for i in range(0, len(lists) // 2):
  print(f"== Pair {i + 1} ==")
  status = handlePair(lists[i * 2], lists[i * 2 + 1])
  if status == CORRECT:
    print("CORRECT")
  elif status == "NO_DET":
    print("NO_DET")
  else:
    print("INCORRECT")

  if status == CORRECT:
    total += i + 1
  print()

print(total)
