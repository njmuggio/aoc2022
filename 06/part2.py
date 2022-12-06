# inputFile = "demo"
inputFile = "input"

with open(inputFile, "rt", encoding="utf-8") as file:
  line = file.read().strip()

buf = [0]
for i in range(0, 13):
  buf.append(line[i])

line = line[13:]

for idx, c in enumerate(line):
  buf.pop(0)
  buf.append(c)

  chars = set(buf)
  if len(chars) == 14:
    print(idx + 14)
    break
