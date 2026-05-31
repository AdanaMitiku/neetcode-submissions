class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = []
        b = []
        visited = set()

        for i in range(len(strs)):
            if strs[i] in visited:
                continue

            a = [strs[i]]
            visited.add(strs[i])

            for j in range(i + 1, len(strs)):
                if sorted(strs[i]) == sorted(strs[j]):
                    a.append(strs[j])
                    visited.add(strs[j])

            b.append(a)

        return b