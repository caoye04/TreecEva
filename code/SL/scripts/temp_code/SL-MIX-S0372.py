from collections import defaultdict
import math

def fibonacci_mod(n, mod):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, (a + b) % mod
    return b

def calculate_geometric_key(base_points, multiplier):
    # Calculate area of polygon formed by base_points
    n = len(base_points)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += base_points[i][0] * base_points[j][1]
        area -= base_points[j][0] * base_points[i][1]
    area = abs(area) // 2
    return (area * multiplier) % 256

# Initial seed value
seed_value = 42

# Generate Fibonacci sequence with modular arithmetic
fib_mod_result = fibonacci_mod(15, 100)

# Apply bitwise operations
bitwise_stage_1 = (seed_value << 2) & 255  # Left shift by 2 and mask to 8 bits
bitwise_stage_2 = bitwise_stage_1 ^ fib_mod_result  # XOR with Fibonacci result
bitwise_stage_3 = (~bitwise_stage_2) & 255  # Bitwise NOT and mask to 8 bits

# Geometry calculation for key component
key_points = [(0, 0), (bitwise_stage_3 % 10, 5), (8, bitwise_stage_3 % 12), (2, 7)]
geometric_factor = calculate_geometric_key(key_points, 3)

# Final key derivation using modular arithmetic
derived_key_component = (geometric_factor * 17 + (bitwise_stage_2 >> 1)) % 128

# Apply ternary operation for final adjustment
adjustment = 10 if derived_key_component > 64 else 5
derived_key_component = (derived_key_component + adjustment) % 128

print(f"Result: {derived_key_component}")