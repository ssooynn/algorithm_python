def solution(skill, skill_trees):
    answer = 0
    for order in skill_trees:
        word = ''.join(filter(lambda x: x in skill, order))
        if skill.startswith(word):
            answer += 1
            
    return answer
