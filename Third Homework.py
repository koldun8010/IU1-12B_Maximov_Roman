n, m = map(int, input().split())
c = [int(input()) for i in range(n)]
 
left = 0
right = 10000000000
while right - left > 1:
    mid = (left + right) // 2
    
    if sum([c[i] // mid for i in range(n)]) < m:
        right = mid
    else:
        left = mid        
print(left)