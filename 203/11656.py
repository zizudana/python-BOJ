st = input()
arr = []
for i in range(len(st)):
  arr.append(st[i:])
arr.sort()
for s in arr:
  print(s)