n = int(input())
result = 1

if n > 0:
  for i in range(1,n+1):
    result *= i

st = list(map(int, reversed(str(result)))) 

num = 0
for i in st:
  if i != 0:
    break
  num += 1
print(num)