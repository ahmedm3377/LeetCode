class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(1, k + 1):
        #     x = nums.pop(-1)
        #     nums.insert(0,x)

        k = k % len(nums)
        x = nums[-k:]
        nums[k:] = nums[:-k]
        nums[:k] = x

        
        