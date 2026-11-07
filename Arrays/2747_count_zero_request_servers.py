from typing import List
from collections import defaultdict

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        sorted_queries = sorted(enumerate(queries), key=lambda item: item[1])
        logs.sort(key=lambda log: log[1])

        ans = [0] * len(queries)
        server_counts = defaultdict(int)

        left = 0
        right = 0
        num_logs = len(logs)

        for original_idx, q_time in sorted_queries:
            while right < num_logs and logs[right][1] <= q_time:
                server_id = logs[right][0]
                server_counts[server_id] += 1
                right += 1

            while left < num_logs and logs[left][1] < q_time - x:
                server_id = logs[left][0]
                server_counts[server_id] -= 1
                if server_counts[server_id] == 0:
                    del server_counts[server_id]
                left += 1

            ans[original_idx] = n - len(server_counts)

        return ans