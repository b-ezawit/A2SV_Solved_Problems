t = int(input())
for _ in range(t):
  n,k = map(int,input().split())
  grid = [list(map(int,input().split())) for _ in range(n)]
  
  grid.sort(key= lambda x: x[1])
  res = k
  
  for l,r,real in grid:
    if l<=res<=r:
      res = max(res,real)
  
  print(res)