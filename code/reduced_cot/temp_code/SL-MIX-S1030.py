def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

def fibonacci_mod(n, mod):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, (a + b) % mod
    return b

# Generate prime-based keys using sieve
primes = [i for i in range(2, 50) if all(i % j != 0 for j in range(2, int(i**0.5) + 1))][:10]
key_sequence = {i: p for i, p in enumerate(primes)}

# Compute Fibonacci-modular values for each prime key
fib_mod_values = {k: fibonacci_mod(v, 1000) for k, v in key_sequence.items()}

# Apply modular exponentiation to combine keys
combined_keys = {k: mod_exp(v, k+1, 997) for k, v in fib_mod_values.items()}

# Dynamic programming table for checksum calculation
checksum_dp = [0] * len(combined_keys)
checksum_dp[0] = list(combined_keys.values())[0]
for i in range(1, len(checksum_dp)):
    current_val = list(combined_keys.values())[i]
    checksum_dp[i] = (checksum_dp[i-1] + current_val * (i+1)) % 1000000

# Final security checksum combines all DP values with LCM adjustment
security_checksum = sum(checksum_dp)
for i in range(len(key_sequence)):
    for j in range(i+1, len(key_sequence)):
        security_checksum = (security_checksum * lcm(key_sequence[i], key_sequence[j])) % 1000000007

print(f"Result: {security_checksum}")