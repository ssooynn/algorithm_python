def solution(numbers):
    numbers.sort(reverse=True, key=lambda x: str(x) * 3)
    return str(int(''.join(map(str, numbers))))
