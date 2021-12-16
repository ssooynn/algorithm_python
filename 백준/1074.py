n, r, c = map(int, input().split())
n = 2**n

def solution(x, y, number):
    global r, c
    delta = [(0, 0), (0, 1), (1, -1), (0, 1)]
    while True:
        print(x, y, number)
        x1, y1 = x, y
        for dx, dy in delta:
            x1 += dx
            y1 += dy
            if x1 == r and y1 == c:
                print(number)
                return
            number += 1
        if number%16 == 0:
            if y+4 < n:
                x, y = x-4, y+4
            elif x+2 < n:
                x, y = x+2, 0
        else:
            if y+2 < n:
                y = 2+y
            elif x+2 < n:
                x, y = 2+x, 0

    return


solution(0, 0, 0)


