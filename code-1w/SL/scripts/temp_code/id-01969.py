from itertools import combinations

# Simulate sensor data aggregation and performance evaluation
def collect_metrics(raw_readings):
    processed = {}
    temp_store = []
    cumulative = 0

    for reading in raw_readings:
        if reading < 0:
            continue
        cumulative += reading
        if reading % 2 == 0:
            temp_store.append(reading * 1.5)

    processed['average'] = cumulative / len(raw_readings) if raw_readings else 0
    processed['peaks'] = [x for x in raw_readings if x > 80]
    processed['flags'] = len(temp_store) > 5
    return processed

def generate_thresholds(base_value):
    # Irrelevant helper that computes unused thresholds
    thresholds = {}
    for i in range(3, 6):
        key = f"level_{i}"
        thresholds[key] = base_value * (1.1 ** i)
    return thresholds

def analyze_variability(data_list):
    # Dead code path - never actually used in final computation
    variance_proxy = 0
    for i in range(len(data_list)):
        for j in range(i + 1, len(data_list)):
            variance_proxy += abs(data_list[i] - data_list[j])
    return variance_proxy

def filter_outliers(seq, limit=75):
    # Semi-relevant: called but only indirectly influences flags
    return [x for x in seq if x <= limit]

def compute_weighted_sum(vals, weights):
    # Distractor function: defined but not used
    return sum(v * w for v, w in zip(vals, weights))

def evaluate_performance(metrics, config):
    score = 0
    
    # Core logic begins
    avg = metrics.get('average', 0)
    high_vals = metrics.get('peaks', [])
    flag_state = metrics.get('flags', False)
    
    # Real impact on result
    if avg > config['threshold_1']:
        score += 15
        if len(high_vals) >= 3:
            score += 10
    else:
        score -= 5
    
    # Misleading dependency
    filtered_peaks = filter_outliers(high_vals, limit=90)
    if len(filtered_peaks) != len(high_vals):
        score -= 2  # Minor penalty, semi-relevant

    # Red herring branch
    debug_mode = False
    log_entries = 0
    if debug_mode:
        log_entries = len([x for x in high_vals if x % 5 == 0])  # Dead code

    # Critical conditional using bitwise and logical mix
    if flag_state and (score & 1 == 1):
        score *= 2
    elif flag_state and (score > 10):
        score += 7

    # Use of itertools: check for any duplicate magnitude pairs
    mag_pairs = list(combinations([int(x) for x in high_vals], 2))
    if any(abs(a - b) == 0 for a, b in mag_pairs):  # No duplicates expected
        score += 3

    return score

# Main execution
sensor_readings = [85, 45, 76, 88, 53, 90, 74, 82, 68, 91]
metric_data = collect_metrics(sensor_readings)

# Generate unused auxiliary data
unused_thresholds = generate_thresholds(20)
irrelevant_combinations = list(combinations([1, 2, 3], 2))

# Define actual config
threshold_map = {
    'threshold_1': 65.0,
    'threshold_2': 80.0
}

# Final evaluation
final_score = evaluate_performance(metric_data, threshold_map)
print(f"Target result: {final_score}")