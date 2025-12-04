import math
class Solution(object):

    def productExceptSelf(self, nums):

       n=len(nums)
       result=[1]*n
       #Finding the left product
       left=1
       for i in range(n):
        result[i]=left
        left*=nums[i]
       #Multiplying the right product
       right=1
       for i in range(n-1,-1,-1):
        result[i]*=right
        right*=nums[i]
       return(result) 


        



        