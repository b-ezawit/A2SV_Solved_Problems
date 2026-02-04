class Solution:    
    def findUnion(self, a, b):
        # code here
        #return list(set(a+b))
        
        #or:
        c = a+b
        c.sort()
                
        i = 0 
        for j in range(1,len(c)):
            if c[i]!=c[j]:
                i += 1
                c[i] = c[j]
        return c[:i+1]
            
            