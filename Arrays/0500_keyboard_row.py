from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        result = []

        for word in words:
            lower_word = word.lower()

            if word[0] in row1:
                chosen_row = row1

            elif word[0] in row2:
                chosen_row = row2

            else:
                chosen_row = row3

            valid = True

            for char in word:
                if char not in chosen_row:
                    valid = False
                    break

            if valid:
                result.append(word)

        return result
