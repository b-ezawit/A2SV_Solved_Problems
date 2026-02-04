class Solution:    
    def findUnion(self, a, b):
        # code here
        #return list(set(a+b))
        
        #or:
        c = a+b
        c.sort()#[1,1,2,2,2,2,2,3,3,3]
                # i j
        i = 0 #c[i]=1 #c[j]=1
        for j in range(1,len(c)):
            if c[i]!=c[j]:
                i += 1
                c[i] = c[j]
        return c[:i+1]
            
            