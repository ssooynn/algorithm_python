import math
n = int(input())
nums = list(map(int, input().split()))
opers = list(map(int, input().split()))
arr = ["+", "-", "*", "//"]
global max_val
global min_val
max_val, min_val = -1e9, 1e9

def calculate(n, nums, operations, tmp_opers):
    global max_val
    global min_val
    if len(tmp_opers) == n-1:
        answer = nums[0]
        for i in range(1, n):
            if tmp_opers[i-1] == "+":
                answer += nums[i]
            elif tmp_opers[i-1] == '-':
                answer -= nums[i]
            elif tmp_opers[i - 1] == '*':
                answer *= nums[i]
            elif tmp_opers[i - 1] == '//':
                if answer < 0:
                    answer = -(-answer//nums[i])
                else:
                    answer = answer//nums[i]
        max_val = max(answer, max_val)
        min_val = min(answer, min_val)
        return

    for i in range(4):
        if operations[i] > 0:
            tmp_opers.append(arr[i])
            operations[i] -= 1
            calculate(n, nums, operations, tmp_opers)
            operations[i] += 1
            tmp_opers.pop()
    return

calculate(n, nums, opers, [])
print(max_val)
print(min_val)