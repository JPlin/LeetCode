import numpy as np
import collections
class Solution:
    # my own version , but time limited
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        
        shorstTime = [0] # record the time
        visited = [K]  # record the join node
        times = np.array(times)
        while len(visited) < N:
            idx , time = self.find_min_next(times , shorstTime , visited)
            print(idx , time)
            if idx == -1:
                break
            shorstTime.append(time)
            visited.append(idx)
        
        if len(visited) < N:
            return -1
        return max(shorstTime)

    def find_min_next(self , times , shorstTime , visited):
        ans_idx = -1
        ans_time = -1
        for cnt , v in enumerate(visited):
            next_list = self.find_next(times , v , visited)
            if len(next_list) > 0:
                min_next_time = times[next_list[0]][2]
                min_next_idx = 0
                for next_i in next_list:
                    next_time = times[next_i][2]
                    if next_time <= min_next_time:
                        min_next_time = next_time
                        min_next_idx = times[next_i][1]
                if ans_time == -1 or ans_time > min_next_time + shorstTime[cnt]:
                    ans_time = min_next_time + shorstTime[cnt]
                    ans_idx = min_next_idx
        return ans_idx , ans_time
        
    def find_next(self , times , v , visited):
        ans = []
        start_list = np.where( times[:,0] == v)[0].tolist()
        idxs = times[start_list , 1]
        for i , idx in enumerate(idxs):
            if idx not in visited:
                ans.append(start_list[i])
        return ans

class Solution2(object):
    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))

        dist = {node: float('inf') for node in range(1, N+1)}

        def dfs(node, elapsed):
            if elapsed >= dist[node]: return
            dist[node] = elapsed
            for time, nei in sorted(graph[node]):
                dfs(nei, elapsed + time)

        dfs(K, 0)
        ans = max(dist.values())
        return ans if ans < float('inf') else -1
if __name__ == '__main__':
    solution = Solution2()
    print(solution.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]] , 4 , 2))
