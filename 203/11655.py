st = input()
result = ''
for s in st:
  if s >='a' and s<='z':
    i = ord(s) + 13
    if i > ord('z'):
      i -= 26
    result += chr(i)
  elif s >='A' and s<='Z':
    i = ord(s) + 13
    if i > ord('Z'):
      i -= 26
    result += chr(i)
  else:
    result += s
print(result)
    
