class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_dict = set(nums)
        longest = 0
        for i in num_dict:
            if i - 1 not in num_dict:
                long = 1
                curr = i
                while curr + 1 in num_dict:
                    long += 1
                    curr += 1
                if long > longest:
                    longest = long

        
        return longest