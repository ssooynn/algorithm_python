def solution(brown, red):
    answer = brown + red
    grid_red = [(red // n, n) for n in range(1, red+1) if red % n == 0]
    for width, height in grid_red:
        if (width + 2) * (height + 2) == answer:
            return [width+2, height+2]
