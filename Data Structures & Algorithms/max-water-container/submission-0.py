class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_i = 0
        right_i = len(heights) - 1

        left = heights[left_i]
        right = heights[right_i]
        
        max_vol = 0
        while left_i != right_i:
            curr_vol = (right_i - left_i) * (min(left, right))
            if curr_vol > max_vol:
                max_vol = curr_vol
            if left > right:
                right_i -= 1
            else:
                left_i += 1
            left = heights[left_i]
            right = heights[right_i]
        
        return max_vol

