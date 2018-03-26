# Friend Circles
class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        nb_friend = len(M)
        visited = []
        ans = 0
        def findFriend(i):
            for f_idx in range(nb_friend):
                if f_idx not in visited and M[i][f_idx]:
                    visited.append(f_idx)
                    findFriend(f_idx)
        
        for i in range(nb_friend):
            if i not in visited:
                findFriend(i)
                ans += 1
        
        return ans


solution = Solution()
a = [[1, 1, 0],
     [1, 1, 0],
     [0, 0, 1]]
print(solution.findCircleNum(a))
