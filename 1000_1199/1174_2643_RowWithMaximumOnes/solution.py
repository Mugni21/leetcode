class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        m=len(mat)
        max_ones=sum(mat[0])
        best_row=0
        for i in range(m):
            count=sum(mat[i])
            if count>max_ones:
                max_ones=count
                best_row=i
        return [best_row,max_ones]

#Just bruteforce lol