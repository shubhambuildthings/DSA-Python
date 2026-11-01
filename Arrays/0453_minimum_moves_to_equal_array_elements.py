class Solution:
    def minMoves(self, nums: list[int]) -> int:

        smallest = min(nums)
        moves = 0

        for num in nums:
            small = smallest - num
            moves += abs(small)

        return moves