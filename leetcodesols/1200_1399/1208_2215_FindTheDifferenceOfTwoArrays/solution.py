class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1s=set(nums1)
        nums2s=set(nums2)
        return [list(nums1s-nums2s),list(nums2s-nums1s)]

        
        