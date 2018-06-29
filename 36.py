class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        cloest = []

        for i, num in enumerate(nums[0:-2]):
            l, r = i + 1, length - 1

            if num + nums[r - 1] + nums[r] < target:
                cloest.append(num + nums[r] + nums[r - 1])
            elif num + nums[l] + nums[l + 1] > target:
                cloest.append(num + nums[l] + nums[l + 1])
            else:
                while l <= r:
                    cloest.append(num + nums[l] + nums[r])
                    if num + nums[l] + nums[r] > target:
                        r = r - 1
                    elif num + nums[l] + nums[r] < target:
                        l = l + 1
                    else:
                        return target

        cloest.sort(key=lambda x: abs(x - target))
        return cloest[0]
