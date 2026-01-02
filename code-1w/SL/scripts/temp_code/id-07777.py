def analyze_component_health(sensor_readings, thresholds):
    healthy_count = 0
    stress_factors = []
    for i, reading in enumerate(sensor_readings):
        if reading < thresholds[i]:
            healthy_count += 1
        deviation = abs(reading - thresholds[i])
        stress_factors.append(deviation * 1.5 if deviation > 0 else 0)
    return healthy_count, stress_factors


def transform_coordinates(locations):
    # Irrelevant geometric transformation (decoy)
    transformed = []
    for x, y in locations:
        new_x = x * 0.9 + y * 0.1
        new_y = y * 0.9 - x * 0.1
        transformed.append((new_x, new_y))
    return transformed

def calculate_entropy(data):
    # Dead path: never used entropy calculation
    from math import log2
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    total = len(data)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return entropy

def generate_synthetic_metrics(n):
    # Generates decoy metrics
    return [i * 0.7 + (i % 3) for i in range(n)]

def validate_system_integrity(checksums, expected):
    # Misleading validation routine
    mismatches = 0
    for c, e in zip(checksums, expected):
        if c != e:
            mismatches += 1
    status_flag = 1 if mismatches == 0 else -1
    temp_result = sum(checksums) * status_flag
    return temp_result  # Unused downstream

def compute_aggregate_risk(exposure_levels, weights):
    # Complex but irrelevant risk model
    risk_score = 0
    for idx, (level, w) in enumerate(zip(exposure_levels, weights)):
        adjustment = 1.1 if level > 50 else 0.9
        risk_score += level * w * adjustment
    normalized_risk = risk_score / sum(weights)
    return int(normalized_risk)

def evaluate_performance(metrics, reference_data):
    base_score = 0
    bonus = 0
    penalty = 0

    # Core logic hidden among distractors
    for idx, (m, ref) in enumerate(zip(metrics, reference_data)):
        if m >= ref:
            base_score += 3
            if idx % 2 == 0:
                bonus += 1  # Hidden conditional bonus
        else:
            penalty += 2

    # Real answer depends on this conditional expression
    final_modifier = 1.25 if base_score > penalty * 2 else 0.8

    # Critical computation
    intermediate = (base_score + bonus - penalty) * final_modifier

    # Decoy operations
    dummy_calc = sum([i**2 for i in range(len(metrics))]) / 100
    debug_trace = [f"step_{i}" for i in range(5)]
    metadata_log = {'version': '2.1', 'active': True}

    # Actual result
    result = int(intermediate * 2 + 17)  # Final deterministic answer

    return result

# Main execution
if __name__ == "__main__":
    # Input data
    sensor_data = [85, 90, 76, 88, 92]
    threshold_limits = [80, 87, 75, 85, 90]
    coords = [(1.0, 2.0), (3.5, 4.2), (5.1, 6.8)]
    checksum_values = [101, 205, 303, 407, 509]
    expected_checksums = [100, 200, 300, 400, 500]
    exposure = [60, 45, 70, 55]
    weights = [0.2, 0.3, 0.4, 0.1]

    # Execute irrelevant functions (distractors)
    health_count, stresses = analyze_component_health(sensor_data, threshold_limits)
    transformed_coords = transform_coordinates(coords)
    synthetic_metrics = generate_synthetic_metrics(5)
    integrity_check = validate_system_integrity(checksum_values, expected_checksums)
    aggregate_risk = compute_aggregate_risk(exposure, weights)

    # Core data for actual computation
    metrics = [4, 5, 4, 6, 5]  # Performance points
    benchmark_data = [3, 5, 4, 5, 4]  # Reference standards

    # Key execution point
    final_score = evaluate_performance(metrics, benchmark_data)

    print(f"Result: {final_score}")