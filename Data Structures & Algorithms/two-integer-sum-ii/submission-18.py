class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, n in enumerate(numbers):
            j = i + 1
            # print("j:",j)
            while j < len(numbers):
                if numbers[j] + n > target:
                    break
                # print("total =", numbers[j] + n, numbers[j], "+", n, "target:", target)
                if numbers[j] + n == target:
                    return [i + 1, j + 1]
                j += 1