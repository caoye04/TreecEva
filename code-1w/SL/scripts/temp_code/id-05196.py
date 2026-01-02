import math

# Simulated sensor array diagnostics with noise filtering and health scoring
def analyze_sensor_array(raw_readings):
    filtered = [x for x in raw_readings if 0.1 <= abs(x) <= 100.0]
    if len(filtered) == 0:
        return 0.0

    # Irrelevant transformation (distractor)
    squared_devs = [(x - sum(filtered)/len(filtered))**2 for x in filtered]
    variance = sum(squared_devs) / len(squared_devs) if squared_devs else 0

    # Real signal: count valid oscillations above threshold
    oscillation_count = 0
    for i in range(1, len(filtered)):
        if filtered[i] * filtered[i-1] < 0:  # Sign change
            oscillation_count += 1

    return oscillation_count

# Data transformation pipeline
def transform_signal(sequence, factor):
    shifted = [(x * 1.5 + factor) % 64 for x in sequence]
    # Bit manipulation for noise injection (mostly irrelevant)
    processed = []
    for val in shifted:
        bits = int(val)
        bits = bits ^ 27  # XOR with prime
        bits = (bits << 1) | (bits >> 7)  # Rotate left by 1
        processed.append(bits % 50)
    return processed

# Main data processing workflow
def process_metrics(data, threshold_fn):
    # Destructuring assignment (relevant)
    primary_chunk, secondary_chunk = data[:len(data)//2], data[len(data)//2:]

    # Decoy calculations with sets (distractor)
    unique_primary = set(primary_chunk)
    unique_secondary = set(secondary_chunk)
    overlap = unique_primary & unique_secondary
    decoy_score = len(overlap) * 0.7

    # Real logic: conditional aggregation
    active_signals = 0
    for val in primary_chunk:
        if threshold_fn(val):
            active_signals += 1
            if active_signals > 3:
                break  # Early exit pattern

    # Secondary verification chain
    verification_flag = False
    if len(secondary_chunk) >= 5:
        sorted_vals = sorted(secondary_chunk, reverse=True)
        top_avg = sum(sorted_vals[:3]) / 3
        verification_flag = top_avg > 25

    # Final computation
    base_metric = active_signals * 17
    final_adjustment = 5 if verification_flag else -2
    return base_metric + final_adjustment

# Unused helper (dead code path)
def deprecated_normalization(vec):
    max_val = max(vec)
    return [x / max_val for x in vec] if max_val != 0 else vec

# Lambda function usage (required feature)
threshold_func = lambda x: x > 18 and x % 4 != 0

# Irrelevant mathematical pre-processing (distractor)
def compute_harmonic_weight(n):
    if n <= 1:
        return 1
    return 1/n + compute_harmonic_weight(n-1)

# Dummy variables and red herrings
baseline_offset = 3.14159
scaling_matrix = [[1, 0], [0, 1]]
correction_factor = sum([i * 0.01 for i in range(10)])  # evaluates to 0.45

# Core data initialization
raw_sensor_data = [2.3, -4.7, 8.1, 15.6, -3.2, 9.4, 22.8, -6.1, 11.3, 4.8]

# Signal transformation (relevant)
transformed_data = transform_signal(raw_sensor_data, 7)

# Diagnostic analysis (partially relevant)
diagnostic_1 = analyze_sensor_array(raw_sensor_data)
diagnostic_2 = sum(transformed_data) / len(transformed_data)

# Final processing step (key statement)
final_diagnostic = process_metrics(transformed_data, threshold_func)

print(f"Result: {final_diagnostic}")