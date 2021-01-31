def countNum(N, num): #N이 갖고있는 num의 개수
  count = 0 
  divNum = num 
  while( N >= divNum): 
    count = count + (N // divNum) 
    divNum = divNum * num 
    return count

#다시풀기
M, N = map(int, input().split()) 
print(min(countNum(M, 5) - countNum(N, 5) - countNum(M-N, 5), countNum(M, 2) - countNum(N, 2) - countNum(M-N, 2)))

