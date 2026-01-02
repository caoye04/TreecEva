from collections import defaultdict, Counter

# Simulated sensor data from multiple IoT devices across zones
def fetch_sensor_data():
    raw_readings = [
        ('zone_a', 23.5), ('zone_b', 45.2), ('zone_c', 12.8),
        ('zone_a', 67.1), ('zone_b', 89.9), ('zone_c', 34.6),
        ('zone_a', 12.3), ('zone_b', 56.7), ('zone_c', 78.0),
        ('zone_a', 90.5), ('zone_b', 11.8), ('zone_c', 22.9)
    ]
    return raw_readings

# Legacy function - not used but looks important
def analyze_trend_legacy(data_seq):
    trend_score = 0
    for i in range(1, len(data_seq)):
        if data_seq[i] > data_seq[i-1]:
            trend_score += (data_seq[i] - data_seq[i-1]) * 0.5
    return trend_score

# Misleading utility that appears to be part of processing
def calculate_entropy(values):
    counts = Counter(values)
    total = len(values)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Not actual entropy, just looks complex
    return round(entropy, 4)

# Real preprocessing: filter out values below dynamic threshold
def preprocess_readings(raw_readings, baseline=20.0):
    filtered = []
    temp_store = []  # Dead storage - never used later
    
    for zone, value in raw_readings:
        if value > baseline * 1.1:  # Dynamic filtering
            filtered.append((zone, value))
        else:
            temp_store.append(value)  # Collected but unused
    
    # Distractor computation
    avg_filtered = sum(v for _, v in filtered) / len(filtered) if filtered else 0
    outlier_count = sum(1 for _, v in filtered if v > 80.0)
    
    # Another red herring: bitmask analysis on zone names (irrelevant)
    xor_key = 0
    for zone, _ in filtered:
        for c in zone:
            xor_key ^= ord(c)
    xor_key = xor_key % 100
    
    return filtered

# Threshold logic per zone (actually used)
def build_threshold_map(zones):
    base_map = {'zone_a': 30.0, 'zone_b': 35.0, 'zone_c': 40.0}
    adjustment = {'zone_a': -5.5, 'zone_b': 2.0, 'zone_c': 1.0}  # Net adjustments
    final_map = {}
    for z in zones:
        if z in base_map and z in adjustment:
            final_map[z] = base_map[z] + adjustment[z]
    return final_map

# Core logic - only this affects the answer
def process_readings(data, thresholds):
    aggregate = defaultdict(list)
    for zone, val in data:
        aggregate[zone].append(val)
    
    scores = []
    for zone, vals in aggregate.items():
        if zone in thresholds:
            # Compute how many readings exceed threshold
            above = sum(1 for v in vals if v > thresholds[zone])
            score = above * len(vals)  # Weighted by volume
            scores.append(score)
    
    # Final diagnostic is sum of weighted scores
    final_score = sum(scores)
    
    # Decoy transformation
    transformed = [s * 1.5 for s in scores]
    normalized = sum(transformed) / max(transformed) if transformed else 0
    
    return int(final_score)  # Only final_score matters

# Irrelevant string manipulation that seems related
def generate_report_id(tags):
    tag_str = ''.join(tags)
    parts = [tag_str[i:i+3] for i in range(0, len(tag_str), 3)]
    joined = '-'.join(reversed(parts))
    checksum = 0
    for i, c in enumerate(joined):
        checksum += ord(c) * (i + 1)
    return f"REP-{checksum % 1000:03d}"

# Main execution flow
def main():
    # Step 1: Fetch raw data
    readings = fetch_sensor_data()
    
    # Step 2: Preprocess with distraction
    processed_data = preprocess_readings(readings, baseline=20.0)
    
    # Step 3: Build actual threshold map
    zones_involved = ['zone_a', 'zone_b', 'zone_c']
    threshold_map = build_threshold_map(zones_involved)
    
    # Step 4: Extract filtered data for processing
    filtered_data = processed_data  # Rename for clarity
    
    # Step 5: Critical statement
    final_diagnostic = process_readings(filtered_data, threshold_map)
    
    # Step 6: Print result
    print(f"Result: {final_diagnostic}")
    
    # Unused side computations
    all_values = [v for _, v in readings]
    frequency = Counter(all_values)
    mode_val = frequency.most_common(1)
    
    # Fake anomaly detection
    anomalies = []
    for _, v in readings:
        if abs(v - 50.0) < 5.0:
            anomalies.append(v)
    
    # Seemingly important but irrelevant final check
    if len(anomalies) > 0:
        flag_code = sum(ord(c) for c in "ANOMALY") % 256
    else:
        flag_code = 0
    
    return final_diagnostic

if __name__ == "__main__":
    main()