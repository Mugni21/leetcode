class Solution:
    def countElements(self, nums: List[int]) -> int:
        maxi=max(nums)
        mini=min(nums)
        numaxi=nums.count(maxi)
        numini=nums.count(mini)
        return max(len(nums)-numaxi-numini,0)