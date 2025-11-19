from functools import reduce

def modified_fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a ^ b
    return b

# Generate first 12 terms of the modified Fibonacci sequence
fib_sequence = [modified_fibonacci(i) for i in range(12)]

# Apply divide-and-conquer reduction with custom operation
signal_chunks = [fib_sequence[i:i+3] for i in range(0, len(fib_sequence), 3)]
reduced_chunks = [reduce(lambda x, y: (x + y) & 0xFF, chunk, 0) for chunk in signal_chunks]

# Merge chunks using dictionary comprehension mapping
chunk_map = {i: val for i, val in enumerate(reduced_chunks)}
merged_signal = {k: v ^ (k * 3) for k, v in chunk_map.items()}

# Final processing step
processed_signal = sum(merged_signal.values()) >> 2
print(f"Result: {processed_signal}")