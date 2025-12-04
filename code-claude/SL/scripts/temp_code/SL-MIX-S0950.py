import itertools

# Function to filter prime numbers
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

# Generate Fibonacci sequence up to a limit
fib_sequence = [0, 1]
while fib_sequence[-1] + fib_sequence[-2] <= 100:
    fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

# Filter even Fibonacci numbers
even_fibs = list(filter(lambda x: x % 2 == 0, fib_sequence))

# Create a set of prime numbers less than 50
primes = [n for n in range(2, 50) if is_prime(n)]

# Create dictionary with prime numbers as keys and their squares as values
prime_squares = {p: p*p for p in primes}

# Create two sets: even Fibonacci numbers and prime numbers that are less than 35
set1 = set(even_fibs)
set2 = set([p for p in primes if p < 35])

# Find the intersection between the two sets
overlap_count = len(set1.intersection(set2))

# Calculate the sum of all elements in both sets
total_elements = sum(set1) + sum(set2)

print(f"Result: {overlap_count}")