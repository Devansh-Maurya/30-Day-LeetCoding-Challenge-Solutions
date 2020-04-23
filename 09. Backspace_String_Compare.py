class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        ss = []
        st = []
        
        for c in S:
            if c != '#':
                ss.append(c)
            elif ss:
                ss.pop()
        
        for c in T:
            if c != '#':
                st.append(c)
            elif st:
                st.pop()
                
        return ss == st

