class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        s = Counter(nums)
        return [fre for fre,i in s.most_common(k)]