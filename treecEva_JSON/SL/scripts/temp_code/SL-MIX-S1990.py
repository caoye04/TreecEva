from functools import reduce

def mod_inverse(a, m):
    # Extended Euclidean Algorithm to find modular inverse
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = egcd(b % a, a)
            return (g, x - (b // a) * y, y)
    g, x, _ = egcd(a % m, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

# Initialize resonance sequence with first term
resonance_sequence = [3]

# Calculate next terms using modular arithmetic
for idx in range(1, 12):
    prev_term = resonance_sequence[-1]
    fib_idx = fibonacci(idx)
    if fib_idx % 17 != 0:  # Check if modular inverse exists
        mod_inv = mod_inverse(fib_idx, 17)
        new_term = (prev_term + mod_inv) % 17
    else:
        # When modular inverse doesn't exist, use 0
        new_term = prev_term % 17
    resonance_sequence.append(new_term)

# Apply a transformation using map and reduce
transformed_values = list(map(lambda x: (x**2 + 3*x + 1) % 19, resonance_sequence))
cumulative_product = reduce(lambda acc, val: (acc * val) % 23, transformed_values, 1)

# Final calculation for the 12th term
final_adjustment = (cumulative_product * mod_inverse(5, 23)) % 23
resonance_12th_term = (resonance_sequence[11] + final_adjustment) % 17

print(f"Result: {resonance_12th_term}")