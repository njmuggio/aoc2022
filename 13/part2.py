# file = "demo"
file = "input"

with open(file, mode="rt", encoding="utf-8") as file:
  lists = [[[2]], [[6]]]
  for line in file:
    line = line.strip()
    if len(line) > 0:
      lists.append(eval(line))

CORRECT = -1
NO_DET = 0
INCORRECT = 1

def handlePair(left, right, depth=0):
  if isinstance(left, list) and isinstance(right, list):
    # print(depth * "  " + f"- Compare {left} vs {right}")
    for i in range(0, len(left)):
      if i >= len(right):
        return INCORRECT
      status = handlePair(left[i], right[i], depth + 1)
      if status == CORRECT or status == INCORRECT:
        return status
    if len(left) < len(right):
      return CORRECT
  elif isinstance(left, int) and isinstance(right, int):
    # print(depth * "  " + f"- Compare {left} vs {right}")
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

sortedLists = [lists.pop()]

for l in lists:
  for i in range(0, len(sortedLists)):
    if CORRECT == handlePair(l, sortedLists[i]):
      sortedLists.insert(i, l)
      break
  else:
    sortedLists.append(l)

print((1 + sortedLists.index([[2]])) * (1 + sortedLists.index([[6]])))
