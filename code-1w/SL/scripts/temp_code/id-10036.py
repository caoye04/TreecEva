from itertools import combinations, cycle

# Simulated sensor data processing pipeline with red herrings
def collect_readings():
    raw_values = [12, 45, 23, 67, 34, 89, 21]
    noise_floor = 15
    filtered = [x for x in raw_values if x > noise_floor]
    return filtered

# Irrelevant transformation - decoy function
def transform_coordinates(data):
    shifted = [(x % 10, x // 10) for x in data]
    return sorted(shifted, key=lambda p: p[1])

# Unused signal normalization (dead code path)
def normalize_signal(x, min_val=0, max_val=100):
    return (x - min_val) / (max_val - min_val)

# Misleading statistical summary - looks important but unused later
def get_summary_stats(data):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    peak_to_peak = max(data) - min(data)
    return {'mean': mean, 'variance': variance, 'p2p': peak_to_peak}

# Core logic disguised among distractions
def generate_metrics(base_data):
    doubled = [x * 2 for x in base_data]
    offset_data = [x - 10 for x in doubled if x > 50]  # Only large values processed
    paired = list(combinations(offset_data, 2))
    metric_sum = sum((a - b) for a, b in paired if a > b)  # Conditional contribution
    return metric_sum

# Decoy pattern matching using cycle (irrelevant)
def detect_pattern(values):
    pattern = cycle([1, 0, 1])
    matched = 0
    for v, p in zip(values[:10], pattern):
        if v % 2 == p:
            matched += 1
    return matched

# Primary evaluation function that uses generated metrics
def evaluate_performance(data_list):
    temp_result = 0
    for i in range(len(data_list)):
        if i % 2 == 0:
            temp_result += data_list[i] * (i + 1)
        else:
            temp_result -= data_list[i] // (i + 1)
    
    # Critical intermediate computation
    adjustment_factor = len(data_list) * 3
    temp_result += adjustment_factor
    
    # Final nonlinear scaling based on sum characteristics
    total = sum(data_list)
    if total > 100:
        temp_result = int(temp_result * 1.5)
    else:
        temp_result = int(temp_result * 0.8)
    
    return temp_result

# --- Main execution with distractions ---
if __name__ == "__main__":
    # Step 1: Collect real data
    sensor_output = collect_readings()  # [45, 23, 67, 34, 89, 21]

    # Step 2: Apply irrelevant transformations (distractors)
    coordinates = transform_coordinates(sensor_output)
    signal_norms = [normalize_signal(x) for x in sensor_output[:3]]  # Computed but unused
    pattern_match_count = detect_pattern(sensor_output)  # Looks diagnostic but ignored

    # Step 3: Generate actual metrics (used later)
    metric_data = []
    metric_data.append(generate_metrics(sensor_output))  # First component

    # Add dummy filler values that look meaningful
    metric_data.append(999)  # Red herring value
    metric_data.append(sum(x * x for x in sensor_output[:2]))  # Fake correlation term

    # Step 4: Real processing begins here — linear search for threshold breach
    threshold_index = -1
    for idx, val in enumerate(sensor_output):
        if val >= 85:
            threshold_index = idx
            break  # Only first matters

    # Modify metric_data based on control flow outcome
    if threshold_index != -1:
        metric_data[0] += sensor_output[threshold_index]

    # Step 5: Evaluate final score using only part of metric_data
    final_score = evaluate_performance(metric_data)

    # Print result as required
    print(f"Result: {final_score}")