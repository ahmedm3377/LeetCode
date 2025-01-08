class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if(target not in nums):
            return -1
        p1 = 0
        p2 = nums.index(min(nums))

        if target>nums[-1]:
            pass
        else:
            p1 = p2
            p2 = len(nums)
        for i in range(p1,p2+1):
            if target==nums[i]:
                return i