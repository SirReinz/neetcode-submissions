class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            # print(i, dict, dict.keys(), i in dict.keys())
            if i not in seen:
                seen.add(i)
            else:
                return True
        return False

        
        