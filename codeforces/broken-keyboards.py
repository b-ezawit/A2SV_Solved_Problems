
t = int(input())
for _ in range(t):
  s = input().strip()
  s = list(s)
  if len(s) == 1:
    print(s[0])
    continue
  
  left,right = 0,1
  res = ""

  while left < len(s):
    curr = s[left]
    charCount = 1
    while right<len(s) and s[right] == curr:
      charCount += 1
      right += 1
    if charCount%2 != 0:
      res += curr
    
    left = right
    right = left + 1
  
  res = list(set(res))
  res.sort()
  print("".join(res))
  

    