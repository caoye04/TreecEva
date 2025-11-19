from itertools import permutations
from functools import lru_cache

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
    return True

@lru_cache(maxsize=None)
def check_consecutive_sum_prime(a, b):
    return is_prime(a + b)

def count_resonance_sequences(n):
    count = 0
    nums = list(range(1, n+1))
    for perm in permutations(nums):
        if perm[0] != 1:
            continue
        valid = True
        for i in range(len(perm)-1):
            if not check_consecutive_sum_prime(perm[i], perm[i+1]):
                valid = False
                break
        if valid:
            count += 1
    return count

signal_count = count_resonance_sequences(6)
print(f"Result: {signal_count}")