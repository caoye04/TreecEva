from functools import reduce

def weighted_recursive_sum(signal_segment, weights, depth=0):
    if not signal_segment or depth >= 3:
        return 0.0
    head, *tail = signal_segment
    weight = weights[depth] if depth < len(weights) else 1.0
    return (head * weight) + weighted_recursive_sum(tail, weights, depth + 1)

signal_data = [2.5, -1.0, 3.14, 0.0, -2.7]
filter_weights = [0.5, -0.3, 0.2]
valid_indices = [i for i in range(len(signal_data)) if signal_data[i] > -2.0 and signal_data[i] < 3.0]
segment_values = [signal_data[i] for i in valid_indices]
filtered_output = weighted_recursive_sum(segment_values, filter_weights)
print(f"Result: {filtered_output}")