class Solution:
    def isHappy(self, n: int) -> bool:
        s = n
        seen = set()
        seen.add(s)
        
        while s != 1:
            add = 0
            
            while s > 9:
                r = s%10
                s = s//10
                add += r*r
            add += s*s
        
            if add in seen:
                return False
            seen.add(add)
            
            s = add
        return True
            

