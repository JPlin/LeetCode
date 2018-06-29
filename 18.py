class Solution:
    def fourSum(self, nums, target):
        res = []
        nums.sort()
        length = len(nums)
        if length < 4:
            return res

        if 4 * nums[0] > target or 4 * nums[-1] < target:
            return res

        for i in range(length):
            now = nums[i]
            if i > 0 and now == nums[i - 1]:  # avoid duplicate
                continue
            if now + 3 * nums[-1] < target:  # too small or too big
                continue
            if 4 * now > target:
                break
            if 4 * now == target:
                if i + 3 < length and nums[i + 3] == now:
                    print('gg')
                    res.append([now] * 4)
                    break
            self.threeSumForFourSum(nums, target - now, i + 1, length - 1, res,
                                    now)
        return res

    def threeSumForFourSum(self, nums, target, low, high, res, pre):
        if low + 1 >= high:
            return

        if 3 * nums[low] > target or 3 * nums[high] < target:
            return

        for i in range(low, high + 1):
            now = nums[i]
            if i > low and now == nums[i - 1]:
                continue
            if now + 2 * nums[high] < target:
                continue
            if 3 * now > target:
                break
            if 3 * now == target:
                if i + 2 < high and nums[i + 2] == now:
                    print('kk')
                    res.append([pre, now, now, now])
                    break
            self.twoSumForFourSum(nums, target - now, i + 1, high, res, pre,
                                  now)
        return

    def twoSumForFourSum(self, nums, target, low, high, res, pre_1, pre_2):
        if low >= high:
            return

        if 2 * nums[low] > target or 2 * nums[high] < target:
            return

        l, r = low, high
        while l < r:
            sum = nums[l] + nums[r]
            if sum == target:
                res.append([pre_1, pre_2, nums[l], nums[r]])
                l = l + 1
                r = r - 1
                while l < r and nums[l] == nums[l - 1]:
                    l = l + 1
                while r > l and nums[r] == nums[r + 1]:
                    r = r - 1

            if sum < target:
                l = l + 1
            if sum > target:
                r = r - 1
        return
