class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        count = {}

        for num in nums:
            if num % 2 == 0:
                count[num] = count.get(num, 0) + 1

        for num in nums:
            if num % 2 == 0 and count[num] == 1:
                return num

        return -1

