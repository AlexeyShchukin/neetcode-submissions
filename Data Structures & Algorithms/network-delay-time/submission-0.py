class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        heap = [(0, k)]
        visited = set()
        max_time = 0 

        while heap:
            time, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            max_time = time

            for neighbor, weight in edges[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (time + weight, neighbor))
        return max_time if len(visited) == n else -1