import heapq
from sortedcontainers import SortedList
from typing import List

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        request_counts = [0] * k

        busy_heap = []

        available = SortedList(range(k))

        for i, start_time in enumerate(arrival):

            while busy_heap and busy_heap[0][0] <= start_time:
                _, server_id = heapq.heappop(busy_heap)
                available.add(server_id)

            if not available:
                continue

            preferred = i % k
            idx = available.bisect_left(preferred)

            if idx == len(available):
                idx = 0

            chosen_server = available.pop(idx)

            request_counts[chosen_server] += 1
            heapq.heappush(busy_heap, (start_time + load[i], chosen_server))

        max_requests = max(request_counts)
        return [server_id for server_id, count in enumerate(request_counts) if count == max_requests]
