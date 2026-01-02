def analyze_telemetry(data, threshold=100):
    filtered = [x for x in data if x > threshold]
    stats = {
        'count': len(filtered),
        'sum': sum(filtered),
        'max': max(filtered) if filtered else 0
    }
    return stats


def transform_sequence(seq):
    # Irrelevant transformation (dead code path)
    shifted = [seq[i] ^ seq[(i+1)%len(seq)] for i in range(len(seq))]
    return [s << 1 for s in shifted]


def compute_checksum(arr):
    # Distractor function: looks important but unused
    checksum = 0
    for val in arr:
        checksum = (checksum + val * 3) % 97
    return checksum


def normalize_values(raw):
    min_val, max_val = min(raw), max(raw)
    if min_val == max_val:
        return [0.5 for _ in raw]
    return [(x - min_val) / (max_val - min_val) for x in raw]


def evaluate_performance(metrics, base):
    adjusted = []
    for i, val in enumerate(metrics):
        if i % 2 == 0:
            adjusted.append(val * 1.1)
        else:
            adjusted.append(val * 0.9)
    
    # Key processing step
    offset = sum(base) % 5
    
    # Bit manipulation red herring
    masked = [int(a) & 0xFF for a in adjusted]
    
    # Actual logic embedded in noise
    pivot = len(adjusted) // 2
    left_half = masked[:pivot]
    right_half = masked[pivot:]
    
    # Real computation
    contribution = 0
    for j, v in enumerate(right_half):
        contribution += v - left_half[j] if j < len(left_half) else v
    
    # Misleading complex expression
    decoy_result = (contribution ^ 54321) & 0xFFFF
    final_score = contribution * 2  # This is the real assignment
    
    # Unused variables to distract
    scaling_factor = 1.75
    temp_buffer = [decoy_result >> i for i in range(4)]
    
    return final_score

# Main execution flow
raw_telemetry = [88, 105, 92, 110, 95, 115, 120, 90]
processed_stats = analyze_telemetry(raw_telemetry, threshold=95)

baseline_metrics = [10, 20, 30, 40]

# Normalize irrelevant data
normalized_data = normalize_values(raw_telemetry)

# Generate unused transformed sequence
sequence_key = [7, 13, 19, 23]
transformed_key = transform_sequence(sequence_key)

# Another distractor: slicing with no impact
window_slice = normalized_data[2:6:2]

# Core metrics used in evaluation
performance_vector = [
    processed_stats['count'] * 5,
    processed_stats['sum'] // 10,
    processed_stats['max'],
    len(raw_telemetry) * 3
]

# Critical statement
final_score = evaluate_performance(performance_vector, baseline_metrics)

print(f"Result: {final_score}")