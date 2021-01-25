st = input()
result = {}
result['sm'] = 0
result['bi'] = 0
result['nu'] = 0
result['bl'] = 0
for s in st:
  if s >= 'a' and s <= 'z':
    result['sm'] += 1
  elif s >= 'A' and s <='Z':
    result['bi'] += 1
  elif s >= '0' and s <= '9':
    result['nu'] += 1
  elif s == ' ':
    result['bl'] += 1
for value in result.values():
  print(value, end = ' ')

