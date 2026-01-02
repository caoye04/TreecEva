from collections import defaultdict, Counter

# Simulated sensor network data processing with diagnostic analysis
def collect_sensor_readings():
    raw_readings = [
        (0, 'temp', 23.5), (1, 'pressure', 101.3), (0, 'humidity', 45.2),
        (2, 'temp', 25.1), (1, 'temp', 24.8), (3, 'humidity', 52.7),
        (2, 'pressure', 100.9), (3, 'temp', 26.3), (0, 'temp', 22.9)
    ]
    return raw_readings

def filter_anomalies(data, limit=50):
    # Irrelevant filtering function (never used in main logic)
    return [x for x in data if x[2] < limit]

def generate_lookup(keys, default=0):
    # Distractor: creates unused mapping
    lookup = defaultdict(lambda: default)
    for i, key in enumerate(keys):
        lookup[key] = i * 2 + default
    return lookup

def parse_readings(raw_data):
    # Parse and group sensor readings by type and node_id
    grouped = defaultdict(list)
    stats = defaultdict(int)
    temp_count = 0

    for node_id, s_type, value in raw_data:
        grouped[s_type].append((node_id, value))
        stats[s_type] += 1
        if s_type == 'temp':
            temp_count += 1

    # Dead code path: temp_count is never used again
    scaling_factor = 1.0 if temp_count > 5 else 0.5

    return grouped

# Unused recursive function - red herring
def calculate_entropy(values, depth=0):
    if depth >= 3 or len(values) == 0:
        return 0.0
    mid = len(values) // 2
    left = values[:mid]
    right = values[mid+1:]
    return 1 + 0.5 * (calculate_entropy(left, depth+1) + calculate_entropy(right, depth+1))

def compute_baseline(readings_list):
    # Compute median as baseline reference
    sorted_vals = sorted(readings_list)
    n = len(sorted_vals)
    if n % 2 == 0:
        return (sorted_vals[n//2-1] + sorted_vals[n//2]) / 2
    else:
        return sorted_vals[n//2]

def derive_trends(values, base):
    # Determine trend direction relative to baseline
    above = sum(1 for v in values if v > base)
    below = sum(1 for v in values if v < base)
    return 'rising' if above > below else 'falling' if below > above else 'stable'

def build_threshold_map(types, offsets):
    # Create threshold policy per sensor type
    policy = {}
    for t, offset in zip(types, offsets):
        if t == 'temp':
            policy[t] = {'min': 20 + offset, 'max': 30 + offset}
        elif t == 'pressure':
            policy[t] = {'min': 95 + offset, 'max': 105 + offset}
        else:
            policy[t] = {'min': 30 + offset, 'max': 60 + offset}
    return policy

def normalize_readings(grouped_data):
    # Normalize readings per sensor type using z-score (unused later)
    normalized = {}
    for s_type, records in grouped_data.items():
        values = [v for _, v in records]
        mean = sum(values) / len(values)
        variance = sum((x - mean) ** 2 for x in values) / len(values)
        std_dev = variance ** 0.5
        normalized[s_type] = [(node_id, (val - mean) / std_dev) for node_id, val in records]
    return normalized

def process_readings(parsed_data):
    processed = {}
    baselines = {}
    trends = {}

    for s_type, records in parsed_data.items():
        values = [v for _, v in records]
        baseline = compute_baseline(values)
        trend = derive_trends(values, baseline)

        baselines[s_type] = baseline
        trends[s_type] = trend
        processed[s_type] = {
            'baseline': baseline,
            'trend': trend,
            'readings': values,
            'count': len(values)
        }

    # Intermediate diagnostic score (misleading)
    diagnostic_score = 0
    for s_type in processed:
        if processed[s_type]['trend'] == 'rising':
            diagnostic_score += 10
        elif processed[s_type]['trend'] == 'falling':
            diagnostic_score -= 5

    # This variable is irrelevant to final result
    compression_ratio = len(parsed_data) / (sum(len(v['readings']) for v in processed.values()) + 1)

    return processed

def evaluate_stability(trend_map):
    # Another decoy analysis
    weights = {'rising': 1, 'falling': -1, 'stable': 0}
    total = sum(weights[t] for t in trend_map.values())
    return 'unstable' if abs(total) > 1 else 'stable'

def analyze_readings(processed, thresholds):
    alert_count = 0
    for s_type, data in processed.items():
        low_th = thresholds[s_type]['min']
        high_th = thresholds[s_type]['max']
        for val in data['readings']:
            if val < low_th or val > high_th:
                alert_count += 1

    # Secondary metric: deviation magnitude
    total_deviation = 0.0
    for s_type, data in processed.items():
        ref = data['baseline']
        thresh_range = thresholds[s_type]['max'] - thresholds[s_type]['min']
        for val in data['readings']:
            if val < thresholds[s_type]['min']:
                total_deviation += (ref - val) / thresh_range
            elif val > thresholds[s_type]['max']:
                total_deviation += (val - ref) / thresh_range

    # Final diagnostic combines alerts and scaled deviation
    # Only this line determines the final answer
    final_diagnostic = alert_count + int(round(total_deviation * 100))
    return final_diagnostic

# --- Main Execution ---
sensor_data = collect_sensor_readings()
filtered_data = parse_readings(sensor_data)

# Generate unused structures (distractors)
node_index = generate_lookup(['A', 'B', 'C'], default=5)
anomaly_free = filter_anomalies(sensor_data, 1000)  # Not used

# Process real data
processed_data = process_readings(filtered_data)

# Build actual threshold map used in analysis
threshold_map = build_threshold_map(['temp', 'pressure', 'humidity'], [1, 0, 2])

# Perform normalization (dead end - not used)
normalized_data = normalize_readings(filtered_data)

# Evaluate stability (decoy call - result ignored)
stability_status = evaluate_stability({k: v['trend'] for k, v in processed_data.items()})

# Key execution point: this computes the final answer
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Print result as required
print(f"Target result: {final_diagnostic}")