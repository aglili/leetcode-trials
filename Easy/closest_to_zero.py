# Day 1
# 8th Jan 2025





class Solution:
    def find_closest_number(self, nums: list[int]) -> int:
        """
        Find the number closest to zero in the given array. If multiple numbers are equally
        close to zero, returns the larger one.
        
        Time Complexity: O(n) where n is the length of nums
        Space Complexity: O(1) as we only use a single variable
        
        Args:
            nums (list[int]): A non-empty array of integers
            
        Returns:
            int: The number closest to zero. In case of ties, returns the larger value
            
        Examples:
            >>> sol = Solution()
            >>> sol.find_closest_number([4, -2, 1, -1, 3, -3])
            1
            >>> sol.find_closest_number([-4, -2, 2, 4])
            2
            >>> sol.find_closest_number([-2, 2])
            2
            
        Note:
            - If nums has length 1, that number is returned
            - For values equidistant from zero, the positive number is chosen
              (e.g., between -2 and 2, 2 is returned)
            - The input array is assumed to be non-empty
        """
        # Initialize closest with the first number
        closest = nums[0]
        
        # Iterate through each number in the array
        for num in nums:
            # Update closest if either:
            # 1. Current number is closer to zero (smaller absolute value)
            # 2. Current number is equally close but larger (handles ties)
            if abs(num) < abs(closest) or (abs(num) == abs(closest) and num > closest):
                closest = num
                
        return closest









        