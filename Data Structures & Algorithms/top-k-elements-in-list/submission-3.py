class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        
        sort = dict(sorted(d.items(), key=lambda item: item[1]))

        return list(sort.keys())[:-k-1:-1]