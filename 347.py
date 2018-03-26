class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import collections
        n = len(nums)
        cntDict = collections.defaultdict(int)
        for i in nums:
            cntDict[i] += 1
        freqList = [[] for i in range(n + 1)]
        for p in cntDict:
            freqList[cntDict[p]] += p,
        ans = []
        for p in range(n, 0, -1):
            ans += freqList[p]
        return ans[:k]

    def topKFrequent_2(self, nums, k):
        import collections
        c = collections.Counter(nums)
        return[x[0] for x in c.most_common(k)]


solution = Solution()
print(solution.topKFrequent([1, 1, 1, 2, 2, 3, 3, 4], 3))
