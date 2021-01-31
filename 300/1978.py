import sys

n = int(input())
num = list(map(int, sys.stdin.readline().rstrip().split()))
res = 0
 
if len(num) == n:       
    for i in num:               
        count = 0                    
        for j in range(1,i+1):      # 1부터 리스트의 수까지          
            if i % j == 0:                     
                count += 1                
        if count == 2:                        
            res += 1    
print(res)