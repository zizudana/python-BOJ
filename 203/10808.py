st = input()
alpa = {}
for i in range(ord('a'), ord('z')+1):
  alpa[chr(i)] = 0
for s in st:
  alpa[s] += 1
for value in alpa.values():
  print(value, end = ' ')