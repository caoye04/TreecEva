def fibonacci_primes(limit):
    fib = [0, 1]
    while len(fib) < limit:
        fib.append(fib[-1] + fib[-2])
    
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
    
    prime_fibs = []
    for i in range(2, len(fib)):
        if is_prime(fib[i]):
            prime_fibs.append(fib[i])
    return prime_fibs[:8]  # Get first 8 prime Fibonacci numbers

# Get prime Fibonacci numbers
prime_fib_sequence = fibonacci_primes(20)

# Convert to frozenset for immutable operations
prime_set = frozenset(prime_fib_sequence)

# Bitwise operations using lambda
xor_operation = lambda x, y: x ^ y
and_operation = lambda x, y: x & y
or_operation = lambda x, y: x | y

# Initialize key components
key_a = 0
key_b = 0

# Process prime set with bitwise operations
for p in sorted(prime_set)[:4]:
    key_a = xor_operation(key_a, p << 2)  # Left shift by 2
    
for p in sorted(prime_set)[4:]:
    key_b = or_operation(key_b, p >> 1)   # Right shift by 1

# Apply modular arithmetic
modulus = 1024
key_a = key_a % modulus
key_b = key_b % modulus

# Combine keys using AND operation
combined_key = and_operation(key_a, key_b)

# Greedy selection of maximum contributing prime
max_prime = max(prime_set)

# Final master key computation
master_key = (combined_key ^ max_prime) % 512

print(f"Result: {master_key}")