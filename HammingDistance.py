class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        counter = 0
        result = bin(x^y)
        for i in result:
            if i=='1':
                counter=counter+1
        return counter
                
