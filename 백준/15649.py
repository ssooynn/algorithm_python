def solution(target_num, tmp_num, arr, tmp_arr):
    if target_num == tmp_num:
        for num in tmp_arr:
            print(num, end=' ')
        return

    for i in range(len(arr)):
        if arr[i] not in tmp_arr:
            tmp_arr.append(arr[i])
            solution(target_num, tmp_num + 1, arr, tmp_arr)
            tmp_arr.pop()


if __name__ == "__main__":

    n, m = map(int, input().split())
    arr = [i for i in range(1, n + 1)]
    solution(m, 0, arr, [])