class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        even_count = {}
        max = 0
        result = -1

        for num in nums:
            if num % 2 == 0:
                even_count[num] = even_count.get(num, 0) + 1
                if even_count[num] > max:
                    max = even_count[num]
                    result = num
                elif even_count[num] == max and num < result:
                    result = num

        return result
