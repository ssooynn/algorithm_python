from collections import deque
import math
def solution(progresses, speeds):
    answer = []
    dq = deque()
    for progress, speed in zip(progresses, speeds):
        dq.append(math.ceil((100-progress)/speed))
        
    val = dq.popleft()
    cnt = 1
    
    while dq:
        days = dq.popleft()
        if days <= val:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            val = days
            
    answer.append(cnt)    
    return answer
