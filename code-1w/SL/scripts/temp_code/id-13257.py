import math

# Simulated sensor data processing with diagnostic analysis
def collect_diagnostics(raw_samples):
    normalized = [round(math.sin(x / 10) * 100, 2) for x in raw_samples]
    filtered = [val for val in normalized if val > -50]
    return filtered

# Irrelevant helper: computes statistical dispersion (not used in final result)
def compute_dispersion(data):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    return round(variance ** 0.5, 4)

# Core transformation function with slicing and conditional logic
def transform_signal(signal, mode='adaptive'):
    shifted = [(val * 1.1 + 7) % 100 for val in signal]
    reversed_chunk = shifted[::-1]
    # Apply windowing based on length
    windowed = reversed_chunk[1:-1] if len(reversed_chunk) > 4 else reversed_chunk
    return [round(x, 2) for x in windowed]

# Data masking with XOR-based obfuscation (partially relevant)
def apply_mask(sequence, seed=13):
    masked = []
    for i, val in enumerate(sequence):
        noise = (i ^ seed) % 25
        masked.append(int(val) ^ noise)  # bitwise XOR
    return masked

# Main pattern analyzer: determines stability index from processed data
def analyze_pattern(dataset, threshold):
    # Distractor block: unused branching
    if len(dataset) == 0:
        return -999
    elif len(dataset) == 1:
        return dataset[0] * 2

    # Relevant computation path
    squared_sum = sum(x ** 2 for x in dataset)
    avg_square = squared_sum / len(dataset)
    root_mean = math.sqrt(avg_square)

    adjustment_factor = 1.0
    # Conditional expression based on modular condition
    adjustment_factor = 0.8 if len(dataset) % 3 == 0 else (1.2 if len(dataset) % 5 == 0 else 1.0)

    # Use lambda to dynamically weight values above threshold
    weigh_high = lambda x: x * 1.5 if x > threshold else x * 0.9
    weighted_vals = [weigh_high(x) for x in dataset]
    weighted_avg = sum(weighted_vals) / len(weighted_vals)

    # Final combination using multiple concepts
    result = (root_mean + weighted_avg) * adjustment_factor
    return int(round(result))

# --- Entry point ---
if __name__ == '__main__':
    # Initial data stream (simulated input)
    sensor_readings = list(range(15, 36))  # 15 to 35 inclusive

    # Step 1: Collect diagnostics
    preliminary_data = collect_diagnostics(sensor_readings)

    # Step 2: Transform signal
    transformed_data = transform_signal(preliminary_data, mode='adaptive')

    # Distractor variables (dead code paths)
    dispersion_score = compute_dispersion(transformed_data)  # Computed but unused
    outlier_count = len([x for x in transformed_data if x > 90])  # Unused metric
    max_value_hint = max(transformed_data) if transformed_data else 0  # Misleading hint

    # Step 3: Masking step (output not used in final chain)
    masked_sequence = apply_mask(transformed_data, seed=13)
    masked_mean = sum(masked_sequence) / len(masked_sequence)  # Dead-end calculation

    # Key execution point
    key_threshold = 42
    final_diagnostic = analyze_pattern(transformed_data, key_threshold)

    # Output target result
    print(f"Result: {final_diagnostic}")