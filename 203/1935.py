import sys
n = int(input())
st = input()
stack = []
nums = []
for i in range(n):
  nums.append(int(input()))

for s in st:
  if s >='A' and s <='Z':
    stack.append(nums[ord(s)-ord('A')])
  else:
    b = stack.pop()
    a = stack.pop()
    if s == '+':
      stack.append(a+b)
    elif s == '-':
      stack.append(a-b)
    elif s == '*':
      stack.append(a*b)
    elif s == '/':
      stack.append(a/b)
print(f"{stack[0]:.2f}")