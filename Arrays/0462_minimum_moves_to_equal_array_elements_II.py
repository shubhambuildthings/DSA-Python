class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        mid = nums[len(nums) // 2]

        moves = 0

        for num in nums:
            moves += abs(num - mid)

        return moves

print(Solution().minMoves2([1, 10, 2, 9]))