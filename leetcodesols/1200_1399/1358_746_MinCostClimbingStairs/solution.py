class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n=len(cost)
        dp=[0]*(n+1)
        dp[-1]=0
        dp[-2]=cost[n-1]
        dp[-3]=cost[n-2]
        for j in range(n-3,-1,-1):
            dp[j]=cost[j]+min(dp[j+1],dp[j+2])
        return min(dp[0],dp[1])

#This one took me a while, so it uses DP (recursion)
#We let dp[j] denote the minimum cost to reach the top, GIVEN that we start 
#at step j. So remember that if you are on step j, you pay when you do the 
#jump. So I define dp to be of size n+1.
#dp[n]=0 because we are already at the top so no need to take more steps
#dp[n-1]=cost[n-1] because we are at the last step and to get to the top
#we need to make exactly one jump which has cost cost[n-1]
#dp[n-2]=cost[n-2] because we are on the penultima step so we only 
#need to jump over the step n-1, which again has cost cost[n-2] since 
#we are already on step n-2
#Then, recursively, we have
#dp[n-j]=cost[n-j]+min(dp[n-j+1],dp[n-j+2]) until we reach dp[1] and dp[0]
#The formula says. We are already at n-j, so no matter what we do, we need to pay 
#cost[n-j], then we can choose to make a size 1 jump or a size 2 jump, and then the recursion kicks in! 
#As we can choose to start at 0 or 1, we just choose the minimum betwwen dp[0] and dp[1]