# 752: open the clock

class Solution(object):
    def openLock(self , deadends , target):
        '''
        :type deadends: List[str]
        :type target: str
        :rtype: int
        '''
        if '0000' in deadends: return -1
        queue = ['0000']
        visits = set(queue + deadends)
        step = 0
        while queue:
            queue0 = []
            for status in queue:
                if status == target: return step
                for sub_status in self.nextState(status):
                    if sub_status in visits: continue
                    visits.add(sub_status)
                    queue0.append(sub_status)
            queue = queue0
            step += 1
        return -1

    def nextState(self , status):
        for i , n in enumerate(status):
            for move in [-1 , 1]:
                digit = (int(status[i]) + move) % 10
                yield status[:i] + str(digit) + status[i+1:]

if __name__ == '__main__':
    solution = Solution()
    print(solution.openLock(['0201' , '0101' , '0102' , '1212' , '2002'] , '0202'))
    print(solution.openLock(['0000'] , '0200'))
