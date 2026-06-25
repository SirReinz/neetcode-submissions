class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = 99999999999999999999
        dif = -999999999999999999999
        for price in prices:
            if price < smallest:
                smallest = price
            if (price - smallest) > dif:
                dif = price - smallest
        return dif
