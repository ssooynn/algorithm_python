def solution(target_num, target_arr, tmp_arr):
    if len(tmp_arr) > target_num:
        return
    if len(tmp_arr) == target_num:
        for num in tmp_arr:
            print(num, end=' ')
        return

    for i in range(len(target_arr)):
        tmp_arr.append(target_arr[i])
        solution(target_num, target_arr, tmp_arr)
        tmp_arr.pop()
    return


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr  = [i for i in range(1, n+1)]
    solution(m, arr, [])


