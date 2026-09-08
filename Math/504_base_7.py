class Solution:
    def convertToBase7(self, num: int) -> str:

        if num == 0:
            return "0"

        neg = num < 0
        num = abs(num)
        result = []

        while num > 0:
            remainder = num % 7
            result.append(str(remainder))
            num //= 7

        result.reverse()
        if neg:
            return "-" + "".join(result)

        return "".join(result)