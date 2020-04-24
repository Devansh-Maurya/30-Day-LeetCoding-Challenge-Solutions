class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        ns = [-stone for stone in stones]
        
        heapq.heapify(ns)
        
        while len(ns) > 1:
            w1 = heapq.heappop(ns)
            w2 = heapq.heappop(ns)
            
            new_weight = w1 - w2
            
            heapq.heappush(ns, new_weight)
            
        return -ns[0]
