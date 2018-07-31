class Solution:
    def twoSum(self, nums, target):
        a = -1
        for i in nums:
            a = a+1
            if a+1 < len(nums):
                x = nums[a+1]
            else:
                break
            y = x + i
            if target == y:
                m = [a,a+1]
        return m
    
j = Solution().twoSum([1,5,4,4],9)
k = print(j)
