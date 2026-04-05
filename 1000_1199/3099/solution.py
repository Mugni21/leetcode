class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        digit_sum = 0
        for digit in str(x):
            digit_sum += int(digit)
        
        if x % digit_sum == 0:
            return digit_sum
        else:
            return -1