class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            new_s = ""
            total = 0
            for i in range(0, len(s), k):
                slicing = s[i:i+k]
                for c in slicing:
                     total += int(c)
                new_s += str(total)
                total = 0
            s = new_s
        return s