def movable(nx, ny):
    return -6 < nx < 6 and -6 < ny < 6


def solution(dirs):
    DELTAS = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    visited_path = set()
    cur_position = (0, 0)

    for dir in dirs:
        dx, dy = DELTAS[dir]
        nxt_position = (cur_position[0] + dx, cur_position[1] + dy)
        
        if not movable(*nxt_position):
            continue
            
        visited_path.add((cur_position, nxt_position))
        visited_path.add((nxt_position, cur_position))
        cur_position = nxt_position

    return len(visited_path) 
