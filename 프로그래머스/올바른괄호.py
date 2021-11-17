def solution(s):
    answer = True
    left = 0
    right = 0 
    for bracket in s:
        if bracket == '(':
            left += 1
        else:
            right += 1
        
        if left < right:
            answer = False
            break
    
    if left != right:
        answer = False
    
    return answer
