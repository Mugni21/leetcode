class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i, k in enumerate(nums):
            if i % 10 == k:
                return i
        return -1
        