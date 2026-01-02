def analyze_signal(samples, threshold):
    filtered = [s for s in samples if abs(s) > threshold]
    magnitude = sum(abs(x) for x in filtered)
    peak_noise = max(filtered, default=0)
    return magnitude if magnitude > 0 else 1


def compute_checksum(data):
    checksum = 0
    for item in data:
        checksum ^= int(item * 10) % 256
    return checksum


def evaluate_stability(readings):
    baseline = sum(readings) / len(readings)
    variance = sum((r - baseline) ** 2 for r in readings) / len(readings)
    return variance < 0.5


def transform_dataset(raw):
    temp_result = []
    for i, val in enumerate(raw):
        if i % 3 == 0:
            temp_result.append(val * 1.5)
        elif i % 3 == 1:
            temp_result.append(val + 2.0)
        else:
            temp_result.append(abs(val - 1.0))
    return [t for t in temp_result if t != 0]


def process_metrics(data, limit):
    # Key logic path
    adjusted = [x * 2 for x in data if x < limit]
    clipped = [min(a, 15.0) for a in adjusted]
    
    # Irrelevant transformation chain (distractor)
    shadow_copy = [x for x in data]
    for _ in range(2):
        shadow_copy = [y / 2 for y in shadow_copy if y > 5]
    dummy_agg = sum(shadow_copy) * 0.1  # Dead-end computation
    
    # More distractions: unused conditionals and variables
    mode_flag = 'high' if sum(clipped) > 20 else 'low'
    temp_offset = 0.0
    if mode_flag == 'high':
        temp_offset = 5.5
        intermediate = [c + temp_offset for c in clipped]
    else:
        intermediate = [c * 0.8 for c in clipped]
    
    # Decoy function call with no effect
    def decoy_normalization(vec):
        total = sum(vec)
        return [v / total for v in vec] if total > 0 else vec
    
    # Actual critical path continues independently
    active_elements = [c for c in clipped if c > 3.0]
    weight_factor = 1.75 if len(active_elements) >= 3 else 0.9
    scored = sum(active_elements) * weight_factor
    
    # Final red herring: conditional expression that looks important but isn't used
    fallback_value = 42.0 if scored <= 0 or len(active_elements) == 0 else -1.0
    
    final_score = scored if scored > 0 else fallback_value
    
    # Critical assignment point
    final_diagnostic = int(round(final_score * 2))

    # Unused but plausible-looking diagnostic block
    diagnostics_log = []
    if final_diagnostic > 50:
        diagnostics_log.append('CRITICAL')
    elif final_diagnostic > 25:
        diagnostics_log.append('ELEVATED')
    else:
        diagnostics_log.append('NORMAL')
    # Log never used

    return final_diagnostic

# Main execution flow
raw_sensor_data = [1.2, 4.5, 0.8, 6.1, 3.3, 2.7, 5.9]
system_threshold = 5.0

# Irrelevant preprocessing steps (distraction)
data_mean = sum(raw_sensor_data) / len(raw_sensor_data)
data_set = set(int(x) for x in raw_sensor_data)
data_set.add(99)
data_set.discard(99)  # No effect

# Chain of transformations with only one being relevant
filtered_stream = [x for x in raw_sensor_data if x > data_mean]
scaled_stream = [x * 1.1 for x in raw_sensor_data]
aggregate_data = transform_dataset(filtered_stream)  # Only this matters indirectly

# Additional distraction: unused signal analysis
signal_strength = analyze_signal(raw_sensor_data, 2.0)
checksum_valid = compute_checksum(raw_sensor_data) > 30
data_stable = evaluate_stability([1.1, 1.2, 1.15, 1.18])

# Key statement
final_diagnostic = process_metrics(aggregate_data, system_threshold)

print(f"Result: {final_diagnostic}")