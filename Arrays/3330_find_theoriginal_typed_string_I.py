class Solution:
    def possibleStringCount(self, word: str) -> int:
        count = 1
        i = 0

        while i < len(word):
            current_char = word[i]
            j = i

            while j < len(word) and word[j] == current_char:
                j += 1

            group_length = j - i

            if group_length > 1:
                count += group_length - 1

            i = j

        return count
