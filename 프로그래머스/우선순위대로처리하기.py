import heapq
from collections import deque
def solution(reqs):
    answer = []
    heap = []
    reqs = deque(reqs)
    total_time = 0
    reset_time = 0
    index = 1
    while reqs:
        if total_time % 3 == 0:
            order, time = reqs.popleft()
            heapq.heappush(heap, (-order, time, index))
            index += 1

        if heap and total_time == reset_time:
            _order, _time, _index = heapq.heappop(heap)
            reset_time += _time
            answer.append(_index)

        total_time += 1

    while heap:
        answer.append(heapq.heappop(heap)[2])
    return answer