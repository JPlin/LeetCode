class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        left = 0
        right = length - 1
        max_area = 0
        max_idx_left = left
        max_idx_right = right
        while left < right:
            left_height = height[left]
            right_height = height[right]
            short = right_height if left_height > right_height else left_height
            area = (right - left) * short
            
            if area > max_area:
                max_area = area
                max_idx_left = left
                max_idx_right = right
            
            if left_height > right_height:
                right -= 1
            else:
                left += 1
        return max_area

solution = Solution()
print(solution.maxArea([1,1]))