class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        for i in range(len(A)):
            if A[i:] + A[:i] == B:
                return True
        return False


solution = Solution()
print(solution.rotateString('abcde', 'cdeab'))
