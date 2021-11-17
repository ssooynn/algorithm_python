import heapq
from collections import deque
def solution(healths, items):
    answer = []
    healths.sort()
    for i in range(1, len(items)+1):
        items[i-1].append(i)

    items.sort(key=lambda x: x[1])
    items = deque(items)
    heap = []

    for health in healths:
        gap = health - 100
        while items and items[0][1] <= gap:
            attack, hp, index = items.popleft()
            heapq.heappush(heap,(-attack, hp, index))

        if heap:
            answer.append(heapq.heappop(heap)[2])

    return sorted(answer)
