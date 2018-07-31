class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x >= 0:
            y = str(x)
            z = y[::-1]
            a = int(z)
            if x == a:
                return True
            else:
                return False
        else:
            return False

test1 = Solution().isPalindrome(1234321)
test2 = Solution().isPalindrome(-5678765)
test3 = Solution().isPalindrome(0)

print(test1)
print(test2)
print(test3)
