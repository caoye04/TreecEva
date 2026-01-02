import math

# Simulated sensor data processing with diagnostic analysis
def collect_diagnostics(raw_readings, baseline):
    processed = []
    anomalies = []
    cumulative_shift = 0

    for idx, reading in enumerate(raw_readings):
        adjusted = reading - baseline + (idx % 7)
        if adjusted > 100:
            anomalies.append((idx, adjusted))
        processed.append(adjusted)

    return processed, anomalies


def apply_filter(sequence, mode='soft'):
    filtered = []
    temp_buffer = []
    for val in sequence:
        if mode == 'aggressive' and val < 10:
            continue
        elif mode == 'soft' and val < 5:
            continue
        filtered.append(val)
        temp_buffer.append(val * 0.9)  # unused distraction

    # Dummy transformation
    inverted = [1 / (x + 1) for x in filtered if x != 0]
    return filtered


def generate_thresholds(count):
    # Complex but irrelevant threshold generation with red herrings
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    fibonacci = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    mixed = []
    for i in range(count):
        mixed.append((primes[i % len(primes)] + fibonacci[i % len(fibonacci)]) / 2)
    return [round(m, 2) for m in mixed]


def compute_entropy(values):
    # Distractor function - not used in final calculation
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log2(p) for p in probs if p > 0)


def transform_sequence(data_list):
    # Apply multiple transformations, some irrelevant
    shifted = [x * 2 + 3 for x in data_list]
    paired = list(zip(shifted[:-1], shifted[1:]))
    diffs = [a - b for a, b in paired]
    indexed = [i * val for i, val in enumerate(diffs, start=1)]
    return shifted[:len(indexed)]  # mismatched length, subtle distraction


def analyze_patterns(data, limits):
    score = 0
    for i, (val, lim) in enumerate(zip(data, limits)):
        if val > lim:
            score += int(val // lim)
        elif val < lim / 2:
            score -= 1
    # Critical logic step buried in noise
    for j in range(len(limits)):
        if j % 3 == 0 and data[j % len(data)] > 20:
            score += 2
    return score * 3


# Main execution flow
if __name__ == "__main__":
    raw_sensor_data = [45, 67, 89, 23, 56, 78, 91, 12, 67, 88, 34, 50, 72, 81, 93]
    base_reference = 22
    
    # Step 1: Collect diagnostics
    cleaned_data, detected_outliers = collect_diagnostics(raw_sensor_data, base_reference)
    
    # Step 2: Apply filtering (soft mode)
    filtered_stream = apply_filter(cleaned_data, mode='soft')
    
    # Step 3: Generate thresholds using complex pattern
    threshold_values = generate_thresholds(len(filtered_stream))
    
    # Step 4: Transform sequence with zip and enumerate
    transformed_data = transform_sequence(filtered_stream)
    
    # Irrelevant entropy computation (dead path)
    _ = compute_entropy(transformed_data)
    
    # Key statement: Analyze patterns to get final diagnostic score
    final_diagnostic = analyze_patterns(transformed_data, threshold_values)
    
    # Unused intermediate variables (distractors)
    snapshot = {i: v for i, v in enumerate(transformed_data)}
    summary_stats = {
        'peak': max(transformed_data),
        'trough': min(transformed_data),
        'range': max(transformed_data) - min(transformed_data)
    }
    
    # Correct output format
    print(f"Result: {final_diagnostic}")