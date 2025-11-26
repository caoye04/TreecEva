import itertools

# Generate sequence using itertools
sequence_gen = itertools.count(start=2, step=3)
sequence = [next(sequence_gen) for _ in range(6)]

# Filter elements that are multiples of 4
filtered_sequence = [x for x in sequence if x % 4 == 0]

# Calculate final result
final_output = sum(filtered_sequence)
print(f"Result: {final_output}")