# Two Sum
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        key_set = {}
        for idx, n in enumerate(nums):
            key_set[n] = idx
        
        print(key_set)
        for idx , n in enumerate(nums):
            left = target - n
            if left in list(key_set.keys()) and key_set[left] != idx:
                return [idx ,key_set[left]]

solution = Solution()
print(solution.twoSum([3,2,4] , 6))