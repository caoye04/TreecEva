from functools import reduce

# Sensor signal strengths encoded as frozensets
encoded_signals = [frozenset({3, 7, 11}), frozenset({2, 5, 9}), frozenset({4, 6, 8})]
mod_base = 13
decoded_accumulator = 0

for signal_set in encoded_signals:
    # Apply modular transformation to each element
    transformed_elements = map(lambda x: (x * 3 + 1) % mod_base, signal_set)
    # Filter out elements less than 5 after transformation
    filtered_elements = filter(lambda x: x >= 5, transformed_elements)
    # Sum the remaining elements using reduce
    subset_sum = reduce(lambda a, b: a + b, filtered_elements, 0)
    # Add to accumulator with modular adjustment
    decoded_accumulator = (decoded_accumulator + subset_sum) % mod_base

print(f"Result: {decoded_accumulator}")