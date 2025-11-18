import math
from collections import deque

def sieve_of_eratosthenes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    for i in range(2, limit + 1):
        if is_prime[i]:
            primes.append(i)
    return primes

prime_numbers = sieve_of_eratosthenes(30)
op_stack = deque()
for idx, p in enumerate(prime_numbers[:10]):
    op_code = (p * 17 + idx) % 256
    op_stack.append(op_code)

verification_checksum = 0
while op_stack:
    current_op = op_stack.pop()
    if current_op % 3 == 0:
        verification_checksum = (verification_checksum + current_op * 2) % 1000
    elif current_op % 3 == 1:
        verification_checksum = (verification_checksum ^ current_op) % 1000
    else:
        verification_checksum = (verification_checksum - current_op) % 1000

print(f"Result: {verification_checksum}")