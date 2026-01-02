from collections import defaultdict, Counter

# Simulated sensor network data analysis with diagnostic logic
def collect_sensor_data():
    raw_readings = [
        (0, 'temp', 23.5), (1, 'pressure', 101.3), (2, 'temp', 24.1),
        (3, 'humidity', 45.2), (4, 'temp', 22.9), (5, 'pressure', 102.1),
        (6, 'humidity', 47.8), (7, 'temp', 25.0), (8, 'pressure', 99.7)
    ]
    return raw_readings

def filter_anomalies(data):
    # Irrelevant filtering (distractor)
    anomalies = [entry for entry in data if 'temp' in entry and (entry[2] < 20 or entry[2] > 30)]
    return [entry for entry in data if entry not in anomalies]

def group_by_type(entries):
    grouped = defaultdict(list)
    for idx, typ, val in entries:
        grouped[typ].append(val)
    return grouped

def compute_averages(groups):
    averages = {}
    for t in groups:
        averages[t] = sum(groups[t]) / len(groups[t])
    return averages

def detect_drift(signal):
    # Dead function - never called (red herring)
    return max(signal) - min(signal) > 5

def reconstruct_timeline(entries):
    timeline = {}
    for idx, typ, val in entries:
        timeline[idx] = {'type': typ, 'value': val}
    return timeline

def calculate_entropy(data_list):
    count = Counter(data_list)
    total = len(data_list)
    entropy = 0
    for freq in count.values():
        p = freq / total
        entropy -= p * (p).log2() if p > 0 else 0
    return round(entropy, 4)

def normalize_readings(avg_dict):
    base = avg_dict.get('temp', 20)
    factors = {k: round(v / base, 3) for k, v in avg_dict.items()}
    return factors

def evaluate_stability(metrics):
    # Unused evaluation path (dead code)
    stable = True
    for key, val in metrics.items():
        if val > 1.2 or val < 0.8:
            stable = False
    return stable

def generate_report(snapshot, config):
    # Decoy reporting function
    report = {
        'version': '2.1',
        'entries': len(snapshot),
        'generated': '2023-12-05',
        'config_hash': hash(str(config))
    }
    return report

def analyze_readings(data_map, thresholds):
    temp_vals = data_map.get('temp', [])
    pressure_vals = data_map.get('pressure', [])
    
    temp_avg = sum(temp_vals) / len(temp_vals)
    pressure_avg = sum(pressure_vals) / len(pressure_vals)
    
    temp_deviation = abs(temp_avg - thresholds['temp_baseline'])
    pressure_deviation = abs(pressure_avg - thresholds['pressure_baseline'])
    
    # Complex conditional logic chain (key inference path)
    if temp_deviation > thresholds['tolerance']:
        level = 3
    elif pressure_deviation > thresholds['tolerance'] * 1.5:
        level = 2
    else:
        consistency_check = all(abs(v - temp_avg) < 0.5 for v in temp_vals)
        if consistency_check:
            level = 1
        else:
            level = 0
    
    penalty = 0
    if len(temp_vals) > 3:
        penalty += 1
    if 'humidity' in data_map:
        humidity_change = max(data_map['humidity']) - min(data_map['humidity'])
        if humidity_change > 3:
            penalty += 2
    
    score = (level * 10) - penalty
    
    # Final computation - deterministic
    adjustment = thresholds['base_adjust'] * (penalty + 1)
    final_score = score * adjustment
    
    return int(final_score)

# Main execution flow
if __name__ == '__main__':
    # Step 1: Collect raw data
    raw_data = collect_sensor_data()
    
    # Step 2: Filter out extreme anomalies (within normal range here)
    clean_data = filter_anomalies(raw_data)
    
    # Step 3: Group by sensor type
    grouped_readings = group_by_type(clean_data)
    
    # Step 4: Compute average per type
    avg_readings = compute_averages(grouped_readings)
    
    # Step 5: Normalize based on temperature baseline
    normalized_factors = normalize_readings(avg_readings)
    
    # Step 6: Reconstruct timeline (unused result - distractor)
    timeline = reconstruct_timeline(clean_data)
    
    # Step 7: Calculate entropy of temperature readings (irrelevant to final result)
    temp_entropy = calculate_entropy(grouped_readings['temp'])
    
    # Step 8: Prepare threshold configuration
    threshold_map = {
        'temp_baseline': 23.0,
        'pressure_baseline': 100.0,
        'tolerance': 1.5,
        'base_adjust': 7.5
    }
    
    # Step 9: Analyze processed data for diagnostic level
    processed_data = grouped_readings  # Key input
    final_diagnostic = analyze_readings(processed_data, threshold_map)
    
    # Output result
    print(f"Result: {final_diagnostic}")