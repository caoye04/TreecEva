from collections import defaultdict, Counter
import math

# Simulated sensor data processing pipeline for environmental anomaly detection
def fetch_sensor_readings():
    return [14, 17, 14, 23, 17, 14, 19, 23, 27, 19, 14, 30, 33, 27, 19]

def apply_calibration(offset, readings):
    calibrated = []
    for val in readings:
        adjusted = val + offset
        if adjusted > 25:
            adjusted = 25  # saturation limit
        calibrated.append(adjusted)
    return calibrated

def compute_entropy(values):
    count_map = defaultdict(int)
    for v in values:
        count_map[v] += 1
    total = len(values)
    entropy = 0.0
    for count in count_map.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 6)

def generate_frequency_matrix(data):
    matrix = defaultdict(lambda: defaultdict(int))
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            diff = abs(data[i] - data[j])
            matrix[data[i]][diff] += 1
    return matrix  # Unused red herring

def detect_outlier_clusters(seq):
    clusters = []
    current = []
    threshold = sum(seq) / len(seq) + 2
    for x in seq:
        if x > threshold:
            current.append(x)
        else:
            if len(current) > 1:
                clusters.append(current[:])
            current = []
    if len(current) > 1:
        clusters.append(current)
    return clusters  # Dead end function

def transform_sequence(raw):
    shifted = [x % 10 for x in raw]
    reversed_seq = shifted[::-1]
    doubled = [x * 2 for x in reversed_seq]
    filtered = [x for x in doubled if x % 3 == 0]
    return filtered

def recursive_condense(nums, depth=0):
    if depth >= 3 or len(nums) <= 1:
        return nums[0] if nums else 0
    reduced = []
    for i in range(0, len(nums) - 1, 2):
        reduced.append((nums[i] + nums[i+1]) // 2)
    return recursive_condense(reduced, depth + 1)

def analyze_pattern(processed, reference):
    c1 = Counter(processed)
    c2 = Counter(reference)
    
    # Irrelevant aggregation
    total_disparity = 0
    for k in set(c1.keys()) | set(c2.keys()):
        total_disparity += abs(c1.get(k, 0) - c2.get(k, 0))
    
    # Core logic buried in noise
    match_points = 0
    for k in c1:
        if k in c2 and k % 2 == 1:
            match_points += min(c1[k], c2[k])
    
    # Secondary analysis (distractor)
    max_overlap = max(min(c1[k], c2[k]) for k in c1 if k in c2) if c1 and c2 else 0
    
    # Actual answer contribution
    base_score = match_points * 13
    adjustment = len([x for x in processed if x > 10]) - len([x for x in reference if x > 10])
    return base_score + adjustment

# Main execution flow
raw_signal = fetch_sensor_readings()

calibrated_signal = apply_calibration(offset=-3, readings=raw_signal)

# Distractor: frequency analysis with no downstream use
diagnostic_matrix = generate_frequency_matrix(calibrated_signal)

# Distractor: outlier cluster detection (unused)
outlier_groups = detect_outlier_clusters(calibrated_signal)

# Transform signal for pattern recognition
transformed_data = transform_sequence(calibrated_signal)

# Baseline for comparison
baseline_reference = [8, 4, 8, 6, 4, 8, 8, 6, 4, 8, 8, 0, 6, 4, 8]

# Recursive condensation (side computation)
condensed_value = recursive_condense(calibrated_signal)

# Key statement containing target variable
final_diagnostic = analyze_pattern(transformed_data, baseline_reference)

# Print result for evaluation
print(f"Result: {final_diagnostic}")