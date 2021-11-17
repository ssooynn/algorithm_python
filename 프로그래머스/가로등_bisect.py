def is_possible(l, v, d):
    cur_light_index = 0
    
    for index in v:
        if cur_light_index < index - d:
            return False
        cur_light_index = index + d
    
    if cur_light_index < l:
        return False
    
    return True 
        

def solution(l, v):
    lower = 1
    upper = l + 1 
    v.sort()
    
    while lower <= upper:
        mid = (lower + upper) // 2
        if is_possible(l, v, mid):
            upper = mid - 1 
        else:
            lower = mid + 1
    
    return upper + 1
