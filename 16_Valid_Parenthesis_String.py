class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        
        os = 0
        cs = 0
        
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == '*':
                if stack and stack[-1] == '(':
                    stack.pop()
                    os += 1
                else:
                    cs += 1
                os += 1
            elif c == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                elif os:
                    os -= 1
                else:
                    return False
                
        stars = 0
        
        for c in stack:
            if c == '*':
                stars += 1
            elif c == '(':
                if stars == 0:
                    return False
                else:
                    stars -= 1
                    
        return True
