class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         found = []
         for i in nums:
            if i in found:
                return True
            else:
                found.append(i)
         return False