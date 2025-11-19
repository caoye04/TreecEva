from functools import reduce

def modified_fibonacci_signal(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(2, n+1):
        next_val = a + b + (i-2) ^ (i-1)
        a, b = b, next_val
    return b

# Calculate energy using functional approach
indices = range(10)
terms = [modified_fibonacci_signal(i) for i in indices]
energy_components = list(map(lambda idx, term: idx * term, indices, terms))
total_energy = reduce(lambda x, y: x + y, energy_components, 0)

print(f"Result: {total_energy}")