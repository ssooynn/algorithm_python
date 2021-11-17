def organizingContainers(container):
    n = len(container)
    cnt_balls = [0] * n
    cnt_set = set()
    
    for i in range(n):
        for j in range(n):
            cnt_balls[j] += container[i][j]
    
    for i in range(n):
        if cnt_balls[i] != 0:
            cnt_set.add(cnt_balls[i])
    
    for i in range(n):
        if sum(container[i]) not in cnt_set:
            return "Impossible"
    
    return "Possible"
