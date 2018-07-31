class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            y = str(x)
            z = y[::-1]
            return int(z)
        else:
            y = str(-x)
            z = y[::-1]
            m = int(z)
            return -m

test1 = Solution().reverse(1234)
test2 = Solution().reverse(-5678)
test3 = Solution().reverse(0)

print(test1)
print(test2)
print(test3)
