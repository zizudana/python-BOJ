def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True

#잘 모르겠다...다시풀기     
while True:
  flag = 0
  n = int(input())
  if n == 0:
    break
  for i in range(1, n//2+1, 2):
    b = n - i
    if b % 2 == 1:
      flag = 1
      a = i
      break
  if flag == 1:
    print(f"{n} = {a} + {b}")
  else:
    print("Goldbach's conjecture is wrong.")
  