grid = [list(map(int,input().split())) for _ in range(5)]

for i in range(5):
  for j in range(5):
    if grid[i][j] == 1:
      row = i
      col = j
      break
print(abs(2-row) + abs(2-col))