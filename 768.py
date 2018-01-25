# max chunks to make sorted II


class Solution(object):
    def maxChunksToSorted(self, arr):
        ans = 1
        for x in range(len(arr)):
            x += 1
            if x == len(arr):
                break
            if max(arr[:x]) <= min(arr[x:]):
                ans += 1
        return ans


solution = Solution()
print(solution.maxChunksToSorted([2, 1, 3, 4, 4]))
