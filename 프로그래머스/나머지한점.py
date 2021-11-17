import collections
def get_ans(a):
    return collections.Counter(a).most_common()[-1][0]

def solution(v):
    x = [vertex[0] for vertex in v]
    y = [vertex[1] for vertex in v]
    return [get_ans(x), get_ans(y)]
