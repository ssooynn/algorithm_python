def solution(arr):
<<<<<<< HEAD
    arr.sort(key=lambda x: (x[1], x[0]))
    end = arr[0][1]
    ans = 1
    for s, e in arr[1:]:
        if end <= s:
            ans += 1
            end = e
=======
    arr.sort(key = lambda x: (x[1], x[0]))
    cur_time = arr[0][1]
    ans = 1
    for start_time, end_time in arr[1:]:
        if cur_time <= start_time:
            ans += 1
            cur_time = end_time
>>>>>>> 5038c3f7063ece8300e9af89087d51ee81eaad04
    return ans
