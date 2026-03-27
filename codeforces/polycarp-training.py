n = int(input())
problems = list(map(int,input().split()))

problems.sort()
count = 0
day = 1

#1,1,3,4
for p in problems:
  if p >= day: #4 >= 3
    count += 1 # 3
    day += 1 #day = 4
    
print(count)