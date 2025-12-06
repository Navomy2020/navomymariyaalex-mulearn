class Solution:
    def maxProduct(self, nums):
        max_prod = nums[0]
        min_prod = nums[0]
        result = nums[0]

        for x in nums[1:]:
            temp_max = max(x, max_prod * x, min_prod * x)
            temp_min = min(x, max_prod * x, min_prod * x)

            max_prod = temp_max
            min_prod = temp_min

            result = max(result, max_prod)

        return result
