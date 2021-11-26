answer_set = set()

def solution(target_num, target_arr, tmp_arr, tmp_index):
    global answer_set
    if len(tmp_arr) == target_num:
        tmp = ''.join(map(str, tmp_arr))
        if tmp not in answer_set:
            answer_set.add(tmp)
            for num in tmp_arr:
                print(num, end=' ')
        return

    for i in range(len(target_arr)):
        if i not in tmp_index:
            tmp_arr.append(target_arr[i])
            tmp_index.append(i)
            solution(target_num, i, target_arr, tmp_arr, tmp_index)
            tmp_arr.pop()
            tmp_index.pop()
    return


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    solution(m, arr, [], [])