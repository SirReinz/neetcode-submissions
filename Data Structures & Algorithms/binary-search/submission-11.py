class Solution:
    def search(self, nums: List[int], target: int) -> int:
        removed = 0
        for num in range(len(nums)//2 + 1):
            # print(nums)
            # if len(nums) == 1:
            #     if nums[0] == target:
                    # return removed

            if target == nums[len(nums)//2]:
                print(nums, len(nums)//2, removed)
                return len(nums)//2 + removed
            if target < nums[len(nums)//2]:
                nums = nums[:len(nums)//2]
            else:
                removed += len(nums[:len(nums)//2])
                nums = nums[len(nums)//2:]
        return -1