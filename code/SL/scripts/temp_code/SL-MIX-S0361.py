from collections import defaultdict

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci_sequence(length):
    fib = [0, 1]
    for _ in range(2, length):
        fib.append(fib[-1] + fib[-2])
    return fib[:length]

# Calculate base sequences
celestial_frequencies = 12
fib_numbers = fibonacci_sequence(celestial_frequencies)
prime_flags = [1 if is_prime(i) else 0 for i in range(celestial_frequencies)]

# Process stellar signatures using XOR and aggregation
stellarsign = 0
for idx in range(celestial_frequencies):
    fib_component = fib_numbers[idx] & 0xFF  # Mask to byte size
    prime_component = prime_flags[idx] << 3  # Shift prime flag
    signature = fib_component ^ prime_component
    stellarsign = (stellarsign + signature) & 0xFFFF  # Add with overflow protection

print(f"Result: {stellarsign}")