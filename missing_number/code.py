class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set=set(nums)
        for i in range(len(nums)+1):
            if i not in num_set:
                return i




        