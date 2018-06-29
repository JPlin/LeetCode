class Solution(object):
    def uniqueLetterString(self, S):
        """
        :type S: str
        :rtype: int
        """
        letterIdx = collections.defaultdict(list)
        for i, c in enumerate(S):
            letterIdx[c].append(i)
        ans = 0
        for letter, idx in letterIdx.items():
            idx = [-1] + idx + [len(S)]
            for x in range(1, len(idx) - 1):
                ans += (idx[x] - idx[x - 1]) * (idx[x + 1] - idx[x])
        return ans