def is_palindrome(s, e_index, cur):
    return True if s[cur - e_index: cur + 1] == s[cur - e_index: cur + 1][::-1] else False


def solution(s):
    if len(s) <= 1:
        return 1

    s_index, e_index = 0, 0  # start_index, end_index

    for cur in range(len(s)):
        if is_palindrome(s, e_index, cur):
            s_index, e_index = cur - e_index, e_index + 1

        elif cur - e_index > 0 and is_palindrome(s, e_index + 1, cur):
            s_index, e_index = cur - e_index - 1, e_index + 2

    return len(s[s_index: s_index + e_index])
