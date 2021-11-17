def solution(max_weight, specs, names):
    answer = 1
    weight = 0
    weight_info = {name: int(weight) for name, weight in specs}
    
    for name in names:
        cur_weight = weight_info[name]
        weight += cur_weight
        if weight > max_weight:
            answer += 1
            weight = cur_weight
    
    return answer
