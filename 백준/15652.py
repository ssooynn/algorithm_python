def solution(target_num, index, target_arr, tmp_arr):
    if index > len(target_arr):
        return
    if len(tmp_arr) == target_num:
        for num in tmp_arr:
            print(num, end=' ')
        print(" ")
        return

    for i in range(index, len(target_arr)):
        tmp_arr.append(target_arr[i])
        solution(target_num, i, target_arr, tmp_arr)
        tmp_arr.pop()
    return


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [i for i in range(1, n+1)]
    solution(m, 0, arr, [])
