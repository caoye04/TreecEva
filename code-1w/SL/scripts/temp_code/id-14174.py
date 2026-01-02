import math

# Simulated sensor data processing with diagnostic analysis
def collect_readings():
    raw_signals = [0.7, 1.2, 0.9, 2.3, 1.8, 0.5, 3.1, 2.7]
    calibrated = [x * 1.05 for x in raw_signals]
    return calibrated

# Irrelevant auxiliary function (decoy)
def compute_efficiency(index, factor):
    if index < 2:
        return factor * 0.8
    else:
        return factor * 1.1 + index % 3

# Signal transformation with noise filtering
def filter_noise(data, limit=2.5):
    cleaned = []
    temp_store = []
    for val in data:
        adjusted = round(val - 0.1, 2)
        if adjusted > limit:
            temp_store.append(adjusted * 0.9)
        else:
            cleaned.append(adjusted)
    # Dead code path - never used
    if len(temp_store) > 5:
        fallback = sum(temp_store) / 5
    return cleaned

# Transform data using sliding window (key preprocessing)
def transform_signal(readings, window_size=3):
    transformed = []
    weights = [0.5, 0.3, 0.2]
    for i in range(len(readings) - window_size + 1):
        window = readings[i:i+window_size]
        weighted_sum = sum(w * v for w, v in zip(weights, window))
        transformed.append(weighted_sum)
    # Distractor: irrelevant calculation
    baseline_avg = sum(readings) / len(readings) if readings else 0
    offset_correction = baseline_avg * 0.05
    return transformed

# Pattern analyzer with conditional logic chain
def matches_anomaly_pattern(seq, thresh):
    if len(seq) < 4:
        return False
    count_rising = 0
    for i in range(1, len(seq)):
        if seq[i] > seq[i-1] + 0.1:
            count_rising += 1
    # Complex condition with short-circuiting and red herring
    spike_exists = any(x > thresh * 1.3 for x in seq)
    is_stable = all(abs(seq[i] - seq[i-1]) < 0.5 for i in range(1, len(seq)))
    false_indicator = is_stable and not spike_exists  # Misleading but unused
    return count_rising >= 3 and spike_exists

# Diagnostic engine with multiple abstraction layers
def analyze_pattern(data, threshold):
    # Nested list comprehension with filtering (core concept)
    candidates = [x for x in data if x > threshold - 0.5]
    
    # Bit manipulation red herring (irrelevant to final result)
    signature = 0
    for val in data[:4]:
        shifted = int(val * 10) << 1
        signature ^= shifted & 0xFF
    
    # Linear search for pattern match (critical path)
    found_index = -1
    for idx in range(len(data) - 5):
        segment = data[idx:idx+5]
        if matches_anomaly_pattern(segment, threshold):
            found_index = idx
            break
    
    # Final decision logic with distractor variables
    base_score = sum(candidates) * 100 if candidates else 0
    penalty = 0
    if found_index > 0:
        adjustment_factor = math.log(found_index + 2)
        penalty = int(adjustment_factor * 50)
    
    # Key computation - only this affects answer
    anomaly_multiplier = 2 if found_index != -1 else 1
    final_score = int(base_score - penalty) * anomaly_multiplier
    
    # Unused complex expression (misleading intermediate)
    theoretical_max = len(data) * int(threshold * 100) // 2
    efficiency_ratio = final_score / theoretical_max if theoretical_max > 0 else 0
    
    # Critical assignment
    final_diagnostic = final_score + 1337  # Base offset
    
    # Redundant print for distraction (not part of logic)
    # print(f'Debug: signature={signature}, ratio={efficiency_ratio:.3f}')
    
    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    # Step 1: Collect sensor data
    signal_data = collect_readings()
    
    # Step 2: Filter out high-amplitude noise (some values removed)
    filtered_data = filter_noise(signal_data, limit=2.5)
    
    # Step 3: Apply transformation using weighted windows
    transformed_data = transform_signal(filtered_data, window_size=3)
    
    # Step 4: Set diagnostic threshold based on statistical property
    mean_val = sum(transformed_data) / len(transformed_data)
    threshold = mean_val * 1.15
    
    # Step 5: Run diagnostic analysis (contains key statement)
    final_diagnostic = analyze_pattern(transformed_data, threshold)
    
    # Output result
    print(f'Target result: {final_diagnostic}')