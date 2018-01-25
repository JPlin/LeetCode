# valid square
class Solution:
    def validSquare(self , p1 , p2 , p3 , p4):
        import collections
        def D(P , Q):
            print(P , Q)
            return (P[0] - Q[0]) ** 2 + (P[1] - Q[1]) ** 2
        S = collections.Counter()
        Pts = [p1, p2, p3, p4]
        for i , x in enumerate(Pts):
            for j , y in enumerate(Pts):
                if i != j:
                    S[D(x , y)] += 1
        return 8 in S.values() and 4 in S.values()

solution = Solution()
print(solution.validSquare([1,0] , [0,1] , [0,-1] , [-1,0]))
