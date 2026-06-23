class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i in nums:
            # print(i, dict, dict.keys(), i in dict.keys())
            if i not in dict.keys():
                dict[i] = 1
            else:
                return True
        return False

        
        