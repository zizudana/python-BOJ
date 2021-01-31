import sys

n =int(input())
result = []
for _ in range(n):
  A, B = map(int, sys.stdin.readline().rstrip().split()) 
  a, b = A, B 
  while b != 0: 
    a = a % b 
    a, b = b, a 
    # gcd 
  #print(a) 
    #lcm 
  result.append(A*B//a)
for i in result:
  print(i)