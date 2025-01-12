class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        max_length = 0
        zero_count = 0
        
        for right in range(len(nums)):
            # Count the zeros in the current window
            if nums[right] == 0:
                zero_count += 1
            
            # If there are more than one zero, shrink the window from the left
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            # Update the maximum length (subtract one to account for deleting one element)
            max_length = max(max_length, right - left)
        
        return max_length

