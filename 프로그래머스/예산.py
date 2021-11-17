def solution(d, budget):
    answer = 0
    total_cost = 0
    for cost in sorted(d):
        total_cost += cost
        if total_cost > budget:
            break
        answer += 1
        
    return answer

