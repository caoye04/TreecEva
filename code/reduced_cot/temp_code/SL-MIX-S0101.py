from functools import reduce
from collections import deque

def modified_fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def phase_shift(index):
    return 1 if index % 2 == 0 else -1

# Initialize processing pipeline
signal_buffer = deque(maxlen=5)
processed_terms = []

# Generate and process first 12 terms
for idx in range(12):
    raw_value = modified_fibonacci(idx)
    phase = phase_shift(idx)
    adjusted_term = raw_value + phase * (idx // 2)
    signal_buffer.append(adjusted_term)
    processed_terms.append(adjusted_term)

# Apply filtering and accumulation
filtered_values = [x for x in processed_terms if x > 0]
energy_components = list(map(lambda x: x**2, filtered_values))
signal_energy = reduce(lambda acc, val: acc + val if val % 2 == 0 else acc, energy_components, 0)

print(f"Result: {signal_energy}")