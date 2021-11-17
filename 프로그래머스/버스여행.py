from collections import deque
from collections import defaultdict


def build_adjacency_list(n, signs, signs_info, dq):
    for i in range(n):
        for j in range(n):
            if signs[i][j]:
                signs_info[i].append(j)
                dq.append((i, j))


def solution(n, signs):
    signs_info = defaultdict(list)
    dq = deque()
    build_adjacency_list(n, signs, signs_info, dq)

    while dq:
        start, destination = dq.popleft()
        for stopover in signs_info[destination]:
            if signs[start][stopover] == 0:
                signs[start][stopover] = 1
                signs_info[start].append(stopover)
                dq.append((start, stopover))

    return signs

