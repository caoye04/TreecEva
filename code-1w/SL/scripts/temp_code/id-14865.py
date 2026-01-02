from collections import defaultdict, Counter
import math

def analyze_readings(readings):
    # Irrelevant aggregation
    stats = defaultdict(float)
    for r in readings:
        if r > 50:
            stats['high'] += 1
        elif r < 30:
            stats['low'] += 1
        else:
            stats['normal'] += 1

    # Distractor transformation
    normalized = [math.log(abs(r) + 1) for r in readings]
    return sum(normalized) // len(normalized) if normalized else 0

def validate_sequence(seq):
    # Unused validation logic (dead code path)
    if len(seq) < 3:
        return False
    for i in range(1, len(seq)):
        if seq[i] <= seq[i-1]:
            return False
    return True

def compute_checksum(data):
    # Misleading checksum calculation
    chk = 0
    for i, v in enumerate(data):
        chk ^= (v + i) * 3
    return chk % 1000  # Never used later

def filter_outliers(values, limit=2.5):
    mean_val = sum(values) / len(values)
    std_dev = (sum((x - mean_val) ** 2 for x in values) / len(values)) ** 0.5
    # Returns filtered list but only side effect matters
    return [v for v in values if abs(v - mean_val) / std_dev < limit]

def evaluate_stability(indices):
    trend = 0
    for i in range(1, len(indices)):
        if indices[i] > indices[i-1]:
            trend += 1
        elif indices[i] < indices[i-1]:
            trend -= 1
    return abs(trend) < 2

def process_metrics(data, config):
    # Core logic embedded in distractions
    stage_one = []
    for k, v in data.items():
        if len(k) % 2 == 0:
            stage_one.append(sum(v) // len(v))
        else:
            stage_one.append(max(v))

    # Red herring: complex string-based key analysis
    key_pattern_score = sum(len(key) * (1 if key[0].lower() in 'aeiou' else -1) for key in data.keys())

    # Decoy sorting and search
    sorted_stage = sorted(stage_one)
    pivot = sorted_stage[len(sorted_stage)//2] if sorted_stage else 0

    # Real computation hidden among noise
    base_score = 0
    for idx, val in enumerate(stage_one):
        if val > config.get('critical', 75):
            base_score += val * 0.3
        elif val < config.get('minimal', 20):
            base_score -= 15
        else:
            base_score += idx + 2  # Key accumulation

    # Another distraction: bit manipulation on irrelevant metric
    magic_flag = 0
    for s in stage_one:
        magic_flag |= (s & 7) << 2

    # Actual answer derivation
    adjustment = len([x for x in stage_one if x % 4 == 0]) * 2.5
    final_score = base_score + adjustment

    # Final red herring: unused conditional branch with early return
    if magic_flag > 1000:
        return -999  # Dead code (never reached)

    # Critical statement
    final_diagnostic = int(final_score * 1.75) % 100000

    return final_diagnostic

# Simulated health monitoring data
health_data = {
    'sensor_A1': [23, 88, 67, 92],
    'temp_B2': [19, 21, 18],
    'log_X7': [76, 77, 81, 83],
    'status_M': [33, 31, 35]
}

# Configuration thresholds (some irrelevant)
thresholds = {
    'critical': 75,
    'minimal': 20,
    'tolerance': 5,
    'damping': 0.85
}

# Irrelevant preprocessing steps
readings_list = [item for sublist in health_data.values() for item in sublist]
analyze_readings(readings_list)
compute_checksum(readings_list)

# Data filtering with no side effects
filtered_data = filter_outliers(readings_list)
evaluate_stability(filtered_data)

# Key execution point
final_diagnostic = process_metrics(health_data, thresholds)

# Output result as required
print(f"Result: {final_diagnostic}")