class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        c = 0
        
        for sh in shift:
            d = sh[0]
            pos = sh[1]
            
            if d:
                c -= pos
            else:
                c += pos
                
        c = c % len(s)
            
        ans = s[c:] + s[:c]
        
        return ans
