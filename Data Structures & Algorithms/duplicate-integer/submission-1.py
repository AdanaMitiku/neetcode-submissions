class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        s=Counter(nums)
        c=0
        for i in s:
            if s[i]>=2:
                return True
        else:
            return False


        