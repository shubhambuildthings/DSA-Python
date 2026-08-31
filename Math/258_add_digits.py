class Solution:
    def addDigits(self, num: int) -> int:

        if num == 0:
            return 0
        elif num == 1:
            return 1
        else:
            return 1 + (num - 1) % 9