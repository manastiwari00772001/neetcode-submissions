class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = sum(range(0,len(nums)+1))
        actualSum = sum(nums)
        return total - actualSum

