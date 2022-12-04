# inFile = "real_demo"
inFile = "real_input"

with open(inFile, "rt", encoding="utf-8") as file:
  score = 0
  letterCounts = {}
  for line in file:
    line = line.strip()
    letters = set(c for c in line)
    for c in letters:
      if c in letterCounts:
        letterCounts[c] += 1

        if letterCounts[c] == 3:
          score += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".index(c) + 1
          letterCounts.clear()
          break
      else:
        letterCounts[c] = 1
print(score)
