class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def helper( nums, left, right):
            if left==right:
                return left

            mid = (left+right)//2
            if nums[mid] > nums[mid+1]:
                return  helper(nums, left, mid)
            else:
                return  helper(nums, mid+1, right)

        return helper(nums, 0, len(nums)-1)



        