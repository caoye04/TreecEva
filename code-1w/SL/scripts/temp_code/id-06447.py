import itertools

# Simulated sensor array data from a distributed environmental monitoring system
def collect_sensor_readings():
    raw_readings = [
        [3.2, 3.5, 3.1, 2.9, 3.3],
        [4.1, 4.3, 4.0, 4.2, 4.1],
        [2.8, 2.7, 2.9, 3.0, 2.6],
        [5.5, 5.7, 5.6, 5.8, 5.4]
    ]
    return raw_readings

# Legacy calibration function (partially deprecated)
def apply_legacy_calibration(data):
    calibrated = []
    for row in data:
        adjusted = [x * 0.98 + 0.1 for x in row]
        calibrated.append(adjusted)
    return calibrated

# Current normalization using z-score per sensor cluster
def normalize_cluster(cluster_data):
    normalized = []
    for series in cluster_data:
        mean_val = sum(series) / len(series)
        variance = sum((x - mean_val) ** 2 for x in series) / len(series)
        std_dev = variance ** 0.5
        if std_dev == 0:
            std_dev = 1
        z_scores = [(x - mean_val) / std_dev for x in series]
        normalized.append(z_scores)
    return normalized

# Irrelevant auxiliary transformation - acts as distractor
def frequency_transform(signal):
    result = []
    for s in signal:
        transformed = [s[i] * s[(i+1)%len(s)] for i in range(len(s))]
        result.append(sum(transformed))
    return result

# Unused debugging path - dead code branch
def debug_consistency_check(data_matrix):
    total_elements = sum(len(row) for row in data_matrix)
    avg_length = total_elements / len(data_matrix)
    consistency_flag = all(len(row) == 5 for row in data_matrix)
    return consistency_flag, avg_length

# Misleading intermediate metric with plausible but unused logic
def compute_redundancy_score(readings):
    score = 0
    for i in range(len(readings)):
        for j in range(i+1, len(readings)):
            overlap = len(set(readings[i]) & set(readings[j]))
            score += overlap * 0.5
    return round(score, 3)

# Signal weighting based on sensor reliability index (critical path)
def generate_weight_vector(n_sensors):
    base_weights = [0.8, 1.2, 0.9, 1.1]
    adjustment = [abs((i + 1) * 0.05 * (-1)**i) for i in range(n_sensors)]
    final_weights = [base_weights[i] + adjustment[i] for i in range(n_sensors)]
    return final_weights

# Core aggregation algorithm combining normalized inputs and weights
def aggregate_metrics(norm_signals, weights):
    metrics = []
    for i, signal_group in enumerate(norm_signals):
        # Use only the first window of each normalized group
        primary_window = signal_group[:3]
        signal_power = sum(x**2 for x in primary_window)
        weighted_contribution = signal_power * weights[i]
        metrics.append(weighted_contribution)
    
    # Composite diagnostic index calculation
    composite = sum(metrics)
    penalty_factor = len([m for m in metrics if m < 0.5]) * 0.3
    return round(composite - penalty_factor, 6)

# Spurious string-based analysis - red herring with no effect on output
def analyze_metadata_tags():
    tags = ['SENS_V4', 'CALIB_2023', 'NODE_A7', 'ENV_MON']
    concatenated = ''.join(tags)
    digit_count = len([c for c in concatenated if c.isdigit()])
    char_sum = sum(ord(c) for c in concatenated) % 100
    return digit_count, char_sum

# Distractor: fake validation that looks important but is unused
def validate_aggregation_integrity(value):
    hex_rep = format(int(abs(value) * 1000), 'x')
    checksum = sum(ord(c) for c in hex_rep) % 7
    return checksum == 3

# Main execution flow
if __name__ == '__main__':
    # Step 1: Collect raw sensor data
    readings = collect_sensor_readings()
    
    # Step 2: Apply outdated calibration (not used in final path)
    legacy_calib = apply_legacy_calibration(readings)
    
    # Step 3: Normalize clusters using current standard (used)
    normalized_signals = normalize_cluster(readings)
    
    # Step 4: Generate weights for sensor fusion
    weights = generate_weight_vector(4)
    
    # Step 5: Compute irrelevant redundancy metric (distractor)
    redundancy_metric = compute_redundancy_score(readings)
    
    # Step 6: Perform frequency domain analysis (dead end)
    spectral_analysis = frequency_transform(normalized_signals)
    
    # Step 7: Run unused debug check
    debug_flag, avg_len = debug_consistency_check(readings)
    
    # Step 8: Analyze metadata (string processing red herring)
    tag_stats = analyze_metadata_tags()
    
    # Step 9: Core aggregation - this determines the answer
    final_diagnostic = aggregate_metrics(normalized_signals, weights)
    
    # Step 10: Irrelevant integrity check (not affecting result)
    isValid = validate_aggregation_integrity(final_diagnostic)
    
    # Output target result
    print(f"Result: {final_diagnostic}")