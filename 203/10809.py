st = input()
alpa = {}
for i in range(ord('a'), ord('z')+1):
  alpa[chr(i)] = -1
for s in range(len(st)):
  if alpa[st[s]] == -1:
    alpa[st[s]] = s
for value in alpa.values():
  print(value, end = ' ')