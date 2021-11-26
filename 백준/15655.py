def solution(target_num, index, target_arr, tmp_arr):
    if len(tmp_arr) > target_num:
        return
    if len(tmp_arr) == target_num:
        for num in tmp_arr:
            print(num, end=' ')
        return

    for i in range(index, len(target_arr)):
        if target_arr[i] not in tmp_arr:
            tmp_arr.append(target_arr[i])
            solution(target_num, i+1, target_arr, tmp_arr)
            tmp_arr.pop()
    return


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    solution(m, 0, arr, [])