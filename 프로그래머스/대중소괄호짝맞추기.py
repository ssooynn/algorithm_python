def solution(s):
    pairs = {'(': ')', '{': '}', '[': ']'}
    stack = []
    
    for bracket in s:
        if bracket in pairs:
            stack.append(pairs[bracket])
        elif not stack:
            return False
        else:
            if bracket != stack.pop():
                return False
    if stack:
        return False
    return True
