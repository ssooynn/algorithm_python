from itertools import combinations

def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False

    for candidate in range(2, n + 1):
        if not is_prime[candidate]:
            continue
        for multiple in range(candidate * candidate, n + 1, candidate):
            is_prime[multiple] = False
    return [idx for idx, val in enumerate(is_prime) if val]


def solution(n):
    answer = 0
    prime_lst = sieve(n)
    combi_lst = combinations(prime_lst, 3)
    for prime_set in combi_lst:
        if sum(prime_set) == n:
            answer += 1

    return answer
