import heapq

class Solution:
    def assignTasks(self, servers, tasks):

        available = []
        busy = []

        n = len(servers)
        m = len(tasks)

        ans = [0] * m

        for i in range(n):
            heapq.heappush(available, (servers[i], i))

        for j in range(m):

            current_time = max(current_time if j > 0 else 0, j)

            while busy and busy[0][0] <= current_time:
                free_time, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))

            if not available:

                current_time = busy[0][0]

                while busy and busy[0][0] <= current_time:
                    free_time, weight, index = heapq.heappop(busy)
                    heapq.heappush(available, (weight, index))

            weight, index = heapq.heappop(available)

            ans[j] = index

            heapq.heappush(
                busy,
                (current_time + tasks[j], weight, index)
            )

        return ans