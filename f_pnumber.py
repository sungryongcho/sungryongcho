from itertools import permutations


def solution(numbers):
    prime_set = set()

    for i in range(len(numbers)):
        numbers_permutations = permutations(list(numbers), i + 1)
        numbers_perm_list = map(int, map("".join, numbers_permutations))
        prime_set |= set(numbers_perm_list)

    prime_set = prime_set - set(range(0, 2))
    lim = int(max(prime_set) ** 0.5) + 1
    for i in range(2, lim):
        prime_set = prime_set - set(range(i * 2, max(prime_set) + 1, i))

    return len(prime_set)