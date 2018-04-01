class Solution(object):
    def minmaxGasDist(self, stations, K):
        """
        :type stations: List[int]
        :type K: int
        :rtype: float
        """

        stations = stations.sort()
        left, right = 0, 1e9
        step = 1e-9
        while left <= right:
            mid = (left + right) / 2.0
            if self.isValid(mid, stations, K):
                right = mid - step
            else:
                left = mid + step
        return mid

    def isValid(self, mid, stations, K):
        import math
        for i in range(len(stations) - 1):
            gap = stations[i + 1] - stations[i]
            K -= int(math.ceil(gap / mid)) - 1
        return K >= 0
