from collections import defaultdict, Counter

# Sensor simulation and diagnostic analysis system
def generate_sensor_readings():
    readings = []
    for i in range(50):
        val = (i * i + 3 * i + 7) % 1000
        readings.append(val)
    return readings

def filter_anomalies(raw_readings, limit=500):
    anomalies = [x for x in raw_readings if x > limit]
    normal = [x for x in raw_readings if x <= limit]
    return normal, anomalies

def compute_entropy(data):
    count = Counter(data)
    total = len(data)
    entropy = 0
    for freq in count.values():
        p = freq / total
        entropy -= p * (p).bit_length()  # Simplified entropy-like measure
    return round(entropy, 6)

def rolling_average(series, window=3):
    avgs = []
    for i in range(len(series) - window + 1):
        avgs.append(sum(series[i:i+window]) / window)
    return avgs

def categorize_levels(data):
    categories = defaultdict(int)
    for x in data:
        if x < 100:
            categories['low'] += 1
        elif x < 250:
            categories['medium'] += 1
        elif x < 500:
            categories['high'] += 1
        else:
            categories['critical'] += 1
    return categories

def apply_calibration(readings):
    # Fake calibration with irrelevant transformations
    calibrated = [(r * 1.03 + 2.7) for r in readings]
    offset = sum(calibrated) / len(calibrated) - sum(readings) / len(readings)
    adjusted = [c - offset for c in calibrated]
    return [int(a) for a in adjusted]

def generate_metadata():
    # Irrelevant metadata generation
    meta = {}
    for key in ['version', 'schema', 'mode', 'region']:
        meta[key] = hash(key) % 100
    meta['timestamp'] = 1698765432
    return meta

def dummy_transform(x):
    # Unused function - red herring
    return (x ^ 255) & 127

def dead_path(data):
    # Dead code path - never called
    result = 0
    for item in data:
        if isinstance(item, str):
            result += len(item)
        else:
            result += item.bit_length()
    return result

def main_pipeline():
    # Step 1: Generate raw sensor data
    raw_data = generate_sensor_readings()  # Deterministic sequence

    # Step 2: Filter out high-value anomalies
    normal_data, outliers = filter_anomalies(raw_data, limit=450)

    # Step 3: Apply fake calibration (changes values slightly)
    calibrated_data = apply_calibration(normal_data)

    # Step 4: Compute various metrics (some irrelevant)
    avg_before = sum(normal_data) / len(normal_data)
    avg_after = sum(calibrated_data) / len(calibrated_data)
    delta = avg_after - avg_before

    # Step 5: Rolling average on original data (distractor)
    roll_avgs = rolling_average(normal_data)

    # Step 6: Categorize levels based on calibrated data
    level_dist = categorize_levels(calibrated_data)

    # Step 7: Compute entropy of distribution (red herring)
    entropy_score = compute_entropy(list(level_dist.values()))

    # Step 8: Build threshold map (only some keys used later)
    threshold_map = {
        'low': 95,
        'medium': 200,
        'high': 400,
        'critical': 500,
        'baseline': sum(calibrated_data) // len(calibrated_data),
        'tolerance': 15
    }

    # Step 9: Simulate metadata (unused)
    metadata_snapshot = generate_metadata()

    # Step 10: Process data into final structured form
    processed_data = []
    for val in calibrated_data:
        entry = {
            'value': val,
            'flagged': val > threshold_map['high'],
            'zone': 'A' if val < threshold_map['medium'] else 'B'
        }
        processed_data.append(entry)

    # Step 11: Analyze readings using only specific fields
    final_diagnostic = analyze_readings(processed_data, threshold_map)

    # Step 12: Print result (required)
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

def analyze_readings(entries, thresholds):
    # Core logic: count how many entries exceed high threshold but are in zone A (logically impossible, so 0?)
    # But zone is assigned based on medium, so if value >= medium -> zone B
    # So no entry can be flagged (value > high) AND in zone A
    contradiction_count = 0
    valid_high_risk = 0
    for e in entries:
        # Contradiction would be: zone A AND value > high threshold
        if e['zone'] == 'A' and e['value'] > thresholds['high']:
            contradiction_count += 1
        if e['value'] > thresholds['high']:
            valid_high_risk += 1
    # However, the real answer is valid_high_risk, not contradiction
    # But the naming distracts
    temp_result = contradiction_count * 1000  # Misleading intermediate
    final_risk_index = valid_high_risk + (thresholds['tolerance'] // 3)
    return final_risk_index

# Execute main pipeline
def run_diagnostic():
    return main_pipeline()

# Global variables - some unused
system_status = 'ACTIVE'
config_override = False
data_buffer = []

# Run and capture result
result_value = run_diagnostic()
