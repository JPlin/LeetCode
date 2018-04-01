class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_row = list(map(max, grid))
        max_col = list(map(max, * grid))
        diff = [min(max_row[x], max_col[y]) - grid[x][y]
                for x in range(len(grid)) for y in range(len(grid[0]))]
        return sum(diff)


solution = Solution()
print(solution.maxIncreaseKeepingSkyline(
    [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]))
