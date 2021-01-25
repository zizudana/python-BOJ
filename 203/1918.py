st = input()
alpa = []
oper = []
for i in range(len(st)):
  if st[i] >='A' and st[i]<'Z':
    alpa.append(st[i])
  elif st[i] == '(':
    while st[i] != ')':
      

