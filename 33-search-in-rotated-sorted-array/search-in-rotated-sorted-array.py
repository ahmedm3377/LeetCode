class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        def minIndex(i, j):
            left, right = 0, len(nums) - 1

            while left < right:
                mid = (left + right) // 2

                # Compare mid element with the rightmost element
                if nums[mid] > nums[right]:
                    left = mid + 1  # Minimum must be in the right half
                else:
                    right = mid  # Minimum is in the left half (including mid)

            # When left == right, we've found the minimum
            return left




        def helper(i, j):
            if i > j:
                return -1

            mid = (i + j) // 2

            if nums[mid] == target:
                return mid

            if target < nums[mid]:
                return helper(i, mid-1 )
            if target > nums[mid]:
                return helper(mid+1 , j)

        mn = minIndex(0, len(nums) - 1)

        if target>nums[-1]:
            return helper(0, mn-1)

        else:
            return helper(mn, len(nums)-1)

