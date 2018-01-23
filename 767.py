# reorganize string
class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        import collections
        cnt = collections.Counter(S)
        res = ''
        while cnt:
            curs = cnt.most_common()
            print(cnt , res)
            flag = True
            for cur, nb in curs:
                if not res.endswith(cur):
                    res += cur
                    if nb == 1:
                        del cnt[cur]
                    else:
                        cnt[cur] = nb - 1
                    flag = False
                    break
            if flag: return ''
        return res

solution = Solution()
print(solution.reorganizeString('aab'))
