class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, target, current):
            if target == 0:
                result.append(current.copy())
                return

            if target < 0:
                return

            for i in range(start, len(candidates)):
                current.append(candidates[i])

                backtrack(i, target - candidates[i], current)

                current.pop()

        backtrack(0, target, [])

        return result
