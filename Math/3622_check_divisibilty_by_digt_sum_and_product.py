class Solution:
    def checkDivisibility(self, n: int) -> bool:

        digit_sum= 0
        digit_product = 1
        original_num = n

        while n > 0:
            digit = n % 10
            digit_sum += digit
            digit_product *= digit
            n //= 10

        return original_num % (digit_product + digit_sum)== 0