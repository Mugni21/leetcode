class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i, k in enumerate(prices): 
            for j in range(i+1,len(prices)): 
                if prices[j]<=k:
                    prices[i]=prices[i]-prices[j]
                    break

        return prices
