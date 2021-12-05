import sys
import heapq

def get_parents(parents, v1):
    if parents[v1] != v1:
        return get_parents(parents, parents[v1])
    return v1

def get_union(parents, v1, v2):
    v1 = get_parents(parents, v1)
    v2 = get_parents(parents, v2)

    if v1 < v2:
        parents[v2] = v1

    else:
        parents[v1] = v2

v, e = map(int, input().split())
parents = [i for i in range(v+1)]

hq = []
for _ in range(e):
    v1, v2, cost = map(int, sys.stdin.readline().split())
    heapq.heappush(hq, (cost, v1, v2))

answer = 0
while hq:
    cost, v1, v2 = heapq.heappop(hq)
    if get_parents(parents, v1) != get_parents(parents, v2):
        get_union(parents, v1, v2)
        answer += cost

print(answer)