class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        maxArea = 0
   
        # Greddy Approach O(N) time
        # two pointers left and right 
        # calc area 
        # return max area possible

        while left <= right:
            area = (right-left) * min(height[left], height[right]) # l*h
            maxArea = max(area, maxArea)

            if height[left] < height[right]:
                left += 1 # advance left pointer
            else:
                right -= 1 # advance right pointer
 
        return maxArea
