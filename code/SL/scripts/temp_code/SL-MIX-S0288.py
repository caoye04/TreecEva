def derive_key(current_key, depth):
    if depth == 0:
        return current_key
    return derive_key((current_key << 1) ^ 3, depth - 1)

sequence = [15, 23, 9, 42]
initial_key = 7
transformed_values = []

for i, num in enumerate(sequence):
    key = derive_key(initial_key, i)
    transformed_values.append(num ^ key)

sorted_events = sorted(transformed_values)
decoded_event = sorted_events[2]  # Third element (0-indexed)
print(f"Result: {decoded_event}")