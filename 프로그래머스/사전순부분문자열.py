def solution(s):
    stack = []
    
    # 아래코드는 현재 char보다 큰 값만 stack에 남게하므로 max_char을 설정해주지않아도 자연스럽게 
    # 가장 큰 값이 나오면 stack에 있는 모든값이 pop됩니다.
    for ch in s:
        while stack and stack[-1] < ch:
            stack.pop()          
        stack.append(ch)
    
    return ''.join(stack)
