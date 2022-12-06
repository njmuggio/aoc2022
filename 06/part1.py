# inputFile = "demo"
inputFile = "input"

with open(inputFile, "rt", encoding="utf-8") as file:
  line = file.read().strip()

buf = [0, line[0], line[1], line[2]]
line = line[3:]
for idx, c in enumerate(line):
  buf.pop(0)
  buf.append(c)

  if buf[0] != buf[1] and buf[0] != buf[2] and buf[0] != buf[3] and buf[1] != buf[2] and buf[1] != buf[3] and buf[2] != buf[3]:
    print(buf)
    print(idx + 4)
    break
