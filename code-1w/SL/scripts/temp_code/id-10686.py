def preprocess_readings(readings):
    # Irrelevant transformation: normalizes to z-scores (not used in final path)
    mean_val = sum(readings) / len(readings)
    std_dev = (sum((x - mean_val) ** 2 for x in readings) / len(readings)) ** 0.5
    z_scores = [(x - mean_val) / std_dev for x in readings]
    return [x for x in readings if x > mean_val]  # Only above-mean values kept


def compute_entropy(data):
    # Dead-end calculation: computes Shannon entropy (unused)
    from math import log2
    freq = {}
    for x in data:
        freq[x] = freq.get(x, 0) + 1
    total = len(data)
    entropy = -sum((count / total) * log2(count / total) for count in freq.values())
    return round(entropy, 4)


def validate_consistency(logs):
    # Distractor function: checks temporal consistency (never called)
    for i in range(1, len(logs)):
        if logs[i] < logs[i-1]:
            return False
    return True


def filter_anomalies(dataset, limit):
    # Misleading filtering: removes outliers beyond limit (partially distractive)
    anomalies = {x for x in dataset if abs(x - sum(dataset)/len(dataset)) > 2 * limit}
    cleaned = [x for x in dataset if x not in anomalies]
    return cleaned if len(cleaned) > 0 else list(dataset)


def calculate_robustness_score(arr):
    # Decoy metric computation (not part of main logic)
    sorted_arr = sorted(arr)
    q1 = sorted_arr[len(sorted_arr)//4]
    q3 = sorted_arr[3*len(sorted_arr)//4]
    iqr = q3 - q1
    return round((q3 + q1) / (iqr + 1), 3)


def analyze_metrics(data, config):
    # Core logic begins
    baseline = config['base']
    tolerance = config['tolerance']
    
    # Step 1: Extract vital indices
    indices = [i for i, x in enumerate(data) if x > baseline]
    
    # Step 2: Compute moving average over window size 3
    moving_avgs = []
    for i in range(2, len(data)):
        avg = (data[i-2] + data[i-1] + data[i]) / 3
        moving_avgs.append(avg)
    
    # Step 3: Flag deviations
    deviation_flags = []
    for m in moving_avgs:
        if abs(m - baseline) > tolerance:
            deviation_flags.append(1)
        else:
            deviation_flags.append(0)
    
    # Step 4: Count sustained deviations (window of 2 consecutive flags)
    sustained_count = 0
    for i in range(1, len(deviation_flags)):
        if deviation_flags[i] == 1 and deviation_flags[i-1] == 1:
            sustained_count += 1
    
    # Step 5: Apply decay factor based on index positions
    decay_factor = 0.95
    weighted_score = 0
    for idx in indices:
        weighted_score += (idx + 1) * decay_factor ** idx  # Higher early indices contribute more
    
    # Step 6: Combine with set-based uniqueness check on high-readings
    high_readings = {data[i] for i in indices}
    unique_penalty = len(high_readings) - len(indices) // 3
    
    # Step 7: Final diagnostic formula
    raw_diagnostic = weighted_score * (sustained_count + 1) - abs(unique_penalty)
    final_diagnostic = int(round(raw_diagnostic, 0))
    
    # Irrelevant print for distraction
    # print(f'Debug: {len(high_readings)} unique high values')
    
    return final_diagnostic

# Main execution block
if __name__ == '__main__':
    # Simulated sensor readings over time
    sensor_log = [88, 92, 95, 87, 105, 110, 108, 94, 90, 115, 113, 117, 109]
    
    # Unused auxiliary data (distractor)
    calibration_sequence = [1.01, 0.99, 1.02, 1.00, 0.98]
    audit_trail = {'init': 'A1', 'phase2': 'B4', 'final': 'C9'}
    metadata_flags = [False, True, False, True, True]
    
    # Preprocessing chain with branching paths (only one matters)
    processed = preprocess_readings(sensor_log)
    entropy_value = compute_entropy(sensor_log)
    filtered_data = filter_anomalies(processed, limit=10)
    robustness = calculate_robustness_score(filtered_data)
    
    # Configuration map for analysis
    thresholds = {
        'base': 95,
        'tolerance': 8
    }
    
    # Key statement
    final_diagnostic = analyze_metrics(sensor_log, thresholds)
    
    # Output result
    print(f"Result: {final_diagnostic}")