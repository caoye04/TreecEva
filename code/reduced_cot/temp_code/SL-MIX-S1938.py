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

# Generate primes up to 50
primes = [i for i in range(2, 51) if is_prime(i)]

# Initialize variables
seed_value = 17
encryption_key = 0

# Nested loop processing
for idx, p in enumerate(primes):
    temp_accumulator = seed_value
    for j in range(idx + 1):
        # Bitwise XOR and left shift
        temp_accumulator ^= (p << (j % 4))
    # Combine into encryption key using XOR
    encryption_key ^= temp_accumulator

print(f"Result: {encryption_key}")