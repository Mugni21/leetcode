class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        numTask=len(tasks)
        tasks.sort(reverse=True)
        processorTime.sort()
        return max([tasks[i*4]+processorTime[i] for i in range(numTask//4)])
        

        