from math import gcd

def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit + 1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Generate first 10 Fibonacci numbers
fib = [1, 1]
for i in range(2, 12):
    fib.append(fib[-1] + fib[-2])

# Get first 10 primes
primes = sieve_of_eratosthenes(30)[:10]

# Compute harmonic scores
harmonic_scores = {}
for i in range(10):
    fn = fib[i]
    fn1 = fib[i+1]
    g = gcd(fn, fn1)
    p = primes[i]
    harmonic_scores[i] = g * p

# Build linked list
head = None
for i in reversed(range(10)):
    head = ListNode(harmonic_scores[i], head)

# Apply transformation with lambda
transform = lambda node: sum(node.val for i, node in enumerate(iter(lambda: (yield node) or node := node.next if node else None, None)) if i % 2 == 0)

# Since the above lambda approach is complex, we use a simpler traversal
node = head
index = 0
harmonic_sum = 0
while node:
    if index % 2 == 0:
        harmonic_sum += node.val
    node = node.next
    index += 1

print(f"Result: {harmonic_sum}")