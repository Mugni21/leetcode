from itertools import combinations

#Bruteforce approach, I am just iterating oover all posible sublists of lenght 4
#and checking the condition.....This is basically O(n^4)..I think it can be made much faster 
#by writing it as nums[a]+nums[b]=nums[d]-nums[c] and then for each fixed pair on the left
#check possible pairs on the right and check the conditon.... \todo{} I guess for now
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        count = 0
        for a, b, c, d in combinations(range(len(nums)), 4):
            if nums[a] + nums[b] + nums[c] == nums[d]:
                count += 1
        return count

        