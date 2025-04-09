class Solution:
    def nthUglyNumber(self, n: int) -> int:
        import heapq


        heap = [1]
        seen = {1}
        for _ in range(n):
            current_ugly = heapq.heappop(heap)
        
            for factor in [2, 3, 5]:
                new_ugly = current_ugly * factor
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)

        return current_ugly


        