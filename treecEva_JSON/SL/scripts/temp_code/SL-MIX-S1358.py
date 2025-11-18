from functools import reduce
from itertools import compress

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

distances = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
prime_flags = list(map(is_prime, distances))
filtered_distances = list(compress(distances, prime_flags))
valid_distances = [d for d in filtered_distances if d > 10 and (d % 7) < 4]
treasure_coordinate_sum = reduce(lambda x, y: x + y, valid_distances, 0)
print(f"Result: {treasure_coordinate_sum}")