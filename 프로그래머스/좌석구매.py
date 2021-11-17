def solution(seat):
    occupied = set(map(tuple, seat))
    answer = len(occupied)
    return answer

