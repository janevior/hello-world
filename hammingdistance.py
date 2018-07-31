class Solution():
    def hammingDistance(self, x, y):
        a = '{0:08b}'.format(x)        
        b = '{0:08b}'.format(y)         
        j = -1
        k = 0
        for i in a[0:]:
            j = j+1 
            l = b[j]
            if (i == l) is True:
                continue
            else:
                k = k+1
            m = k
        return(m)

soln = Solution()
solved1 = soln.hammingDistance(100,14)
solved2 = soln.hammingDistance(1,5)
print (solved1)
print (solved2)
