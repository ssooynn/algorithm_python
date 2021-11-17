from itertools import combinations
def solution(m, weights):
    answer = 0
    for num_candies in range(1, len(weights) + 1):
        combi_list = combinations(weights, num_candies)
        for combi_set in combi_list:
            if sum(combi_set) == m:
                answer += 1
    
    return answer
