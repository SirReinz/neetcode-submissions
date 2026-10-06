class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_cnt = 1, 0
        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt +=  1
        if zero_cnt > 1: return [0] * len(nums)
        
        num_arr = [0] * len(nums)
        
        i = 0
        while i < len(num_arr):
            if zero_cnt: 
                num_arr[i] = 0 if nums[i] != 0 else prod
            else: 
                num_arr[i] = prod // nums[i]
            i += 1
        
        return num_arr