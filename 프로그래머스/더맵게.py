import heapq

def solution(scoville, K):
    answer = 0
    cnt = 0
    heapq.heapify(scoville)
    while len(scoville) > 1:
        min_1 = heapq.heappop(scoville)
        min_2 = heapq.heappop(scoville)

        mixed = min_1 + min_2 * 2
        heapq.heappush(scoville, mixed)
        cnt += 1
        if scoville[0] >= K:
            return cnt
    
    return -1
