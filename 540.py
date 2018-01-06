# 01 matrix
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        h , w = len(matrix), len(matrix[0])
        ans = [[0] * w for x in range(h)]
        queue = [(x, y) for x in range(h) for y in range(w) if matrix[x][y]]
        step = 0
        while queue:
            step += 1
            new_queue = []
            for value in queue:
                for dx , dy in list(zip([1 , 0 , -1 , 0] , [0 , 1 , 0 , -1])):
                    nx , ny = value[0]+dx , value[1]+dy
                    if 0 <= nx < h and 0 <= ny < w and matrix[nx][ny] == 0:
                        ans[value[0]][value[1]] = step
                        new_queue.append(value)
                        break
            queue = list(set(queue).difference(set(new_queue)))
            print(queue)
            for x , y in new_queue:
                matrix[x][y] = 0
        return ans

matrix2 =[[0,0,0],[0,1,0],[1,1,1]]
solution = Solution()
print(solution.updateMatrix(matrix2))