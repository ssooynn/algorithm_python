answer_set = set()

def solution(target_num, target_arr, tmp_arr, tmp_index):
    global answer_set
    if len(tmp_arr) == target_num:
        tmp = tuple(tmp_arr)
        if tmp not in answer_set:
            answer_set.add(tmp)
            for num in tmp_arr:
                print(num, end=' ')
        return

    for i in range(tmp_index, len(target_arr)):
        tmp_arr.append(target_arr[i])
        solution(target_num, target_arr, tmp_arr, i)
        tmp_arr.pop()
    return


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    solution(m, arr, [], 0)