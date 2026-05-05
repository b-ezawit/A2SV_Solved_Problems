n, k = map(int, input().split())
a = list(map(int, input().split()))
 
if k == n:
    print(0)
else:
    gaps = []
    for i in range(n - 1):
        gaps.append(a[i+1] - a[i])
    
    gaps.sort(reverse=True)
    
    ans = a[-1] - a[0]
    for i in range(k - 1):
        ans -= gaps[i]
        
    print(ans)