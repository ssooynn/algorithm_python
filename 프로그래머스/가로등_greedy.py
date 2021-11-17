def solution(l, v):
    v.sort()
    answer = max(v[0], l - v[-1])
    for i in range(len(v) - 1):
        d_val = math.ceil((v[i + 1] - v[i]) / 2)
        if d_val > answer:
            answer = d_val

    return answer
