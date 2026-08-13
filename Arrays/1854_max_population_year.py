from typing import List

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        population = [0] * 101

        for birth, death in logs:
            for year in range(birth, death):
                population[year - 1950] += 1

        max_pop = 0
        answer = 1950

        for i in range(101):
            if population[i] > max_pop:
                max_pop = population[i]
                answer = i + 1950

        return answer
