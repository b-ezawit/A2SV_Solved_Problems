#User function Template for python3
from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        countA = Counter(a)
        for num in b:
            if countA.get(num,0) == 0:
                return False
            countA[num] -= 1
        return True
    
        
    
    
    
    
