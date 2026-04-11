class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        universe=set()
        loser_counter={}

        for winner,loser in matches:
            universe.add(winner)
            universe.add(loser)
            loser_counter[loser]=loser_counter.get(loser,0)+1

        neverlost=sorted(universe-loser_counter.keys())
        loser_once_list=sorted([loser for loser in loser_counter if loser_counter[loser]==1])
        return [neverlost,loser_once_list]


        

        