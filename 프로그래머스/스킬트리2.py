def solution(skills_order, skill_tree):
    index = 0
    N = len(skills_order)
    skill_lst = list(range(N))
    dict_order = {order: index for index, order in enumerate(skills_order)}
    
    for skill in skill_tree:
        if skill in dict_order:
            if dict_order[skill] != index:
                return False
            else:
                index += 1
    
    return True
