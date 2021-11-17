def solution(no, works):
    heap = []
    for work in works:
        heapq.heappush(heap, (-work, work))

    while no > 0:
        max_work = heapq.heappop(heap)[1]
        if max_work == 0:
            break
        heapq.heappush(heap, (-(max_work-1), max_work-1))
        no -= 1

    return sum(work**2 for _, work in heap)
