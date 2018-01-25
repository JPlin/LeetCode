# 769 Mat chunks To Sorted
# greedy algorithm


class Solution(object):
    def maxChunksToSorted(self, arr):
        '''
        :type arr: List[int]
        :rtype : int
        '''
        maxchunck = 0
        last_max = 0
        for idx, i in enumerate(arr):
            if last_max <= idx and idx >= i:
                maxchunck += 1
            elif i > last_max:
                last_max = i
        return maxchunck


solution = Solution()
print(solution.maxChunksToSorted([0]))
