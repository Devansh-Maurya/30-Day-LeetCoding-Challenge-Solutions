import math

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        
        if m == 0:
            return 0
        
        m_log = math.floor(math.log2(m))
        n_log = math.floor(math.log2(n))
        
        if n_log > m_log:
            return 0
        else:
            ans = 2**(n_log+1) - 1
            
            for num in range(m, n+1):
                ans = ans & num
            return ans
