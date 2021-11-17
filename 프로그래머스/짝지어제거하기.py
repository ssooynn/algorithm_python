def solution(s):
    stack = []
    
    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
            continue
        stack.append(ch)
        
    return 0 if stack else 1
   
