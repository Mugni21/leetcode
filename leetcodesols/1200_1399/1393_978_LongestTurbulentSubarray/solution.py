class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 1

        max_len = 1
        curr_len = 1
        prev_sign = None  

        for i in range(1, n):
            if arr[i-1] < arr[i]:
                curr_sign = '<'
            elif arr[i-1] > arr[i]:
                curr_sign = '>'
            else:
                curr_sign = '='

            if curr_sign == '=':
                curr_len = 1
            elif prev_sign is None or prev_sign == '=':
                curr_len = 2
            elif curr_sign != prev_sign:
                curr_len += 1
            else:
                curr_len = 2

            max_len = max(max_len, curr_len)
            prev_sign = curr_sign

        return max_len