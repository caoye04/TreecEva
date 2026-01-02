from collections import defaultdict, Counter

# Simulated sensor network data analysis with diagnostic inference

def collect_readings():
    # Real data source
    raw_readings = [
        (102, 'temp'), (155, 'pressure'), (102, 'temp'), 
        (98, 'humidity'), (155, 'pressure'), (102, 'temp')
    ]
    return raw_readings

# Irrelevant helper - distractor
def smooth_signal(data):
    smoothed = []
    for i in range(len(data)):
        window = data[max(0, i-2):min(i+3, len(data))]
        avg = sum(window) / len(window)
        smoothed.append(avg)
    return smoothed

# Unused transformation - dead code path
def normalize_readings(readings):
    max_val = max([r[0] for r in readings])
    return [(r[0]/max_val, r[1]) for r in readings]

# Core processing function
def process_readings(raw_readings):
    grouped = defaultdict(list)
    counts = Counter()

    for value, sensor_type in raw_readings:
        grouped[sensor_type].append(value)
        counts[sensor_type] += 1

    stats = {}
    for stype, values in grouped.items():
        mean = sum(values) / len(values)
        peak = max(values)
        # Store multiple metrics, only one will be used
        stats[stype] = {
            'mean': mean,
            'peak': peak,
            'count': counts[stype],
            'range': peak - min(values)
        }
    
    # Secondary computation - mostly irrelevant
    entropy = 0
    total = sum(counts.values())
    for count in counts.values():
        if count > 0:
            p = count / total
            entropy -= p * __import__('math').log2(p)
    
    # This is the actual processed data needed downstream
    condensed = {t: round(d['mean']) for t, d in stats.items()}
    return condensed, entropy, stats  # Only first returned value matters

# Decoy analysis function - looks important but unused
def evaluate_anomaly_score(data):
    score = 0
    for val in data.values():
        if val > 100:
            score += val * 0.1
        else:
            score += val * 0.05
    return round(score, 3)

# Another red herring - complex but unused logic
def detect_pattern(sequence):
    if len(sequence) < 3:
        return False
    diffs = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
    return all(d == diffs[0] for d in diffs)

# Threshold configuration - some values are distractions
threshold_map = {
    'temp': {'warn': 95, 'crit': 110},
    'pressure': {'warn': 140, 'crit': 160},
    'humidity': {'warn': 90, 'crit': 100},
    'flow': {'warn': 50, 'crit': 75}  # flow never appears in data
}

# Critical diagnostic engine
def analyze_readings(processed_data, thresholds):
    diagnostic = 0
    
    # Key logic: sum of ceiling(mean_value / 10) for sensors exceeding warning
    for sensor_type, mean_val in processed_data.items():
        if sensor_type in thresholds:
            warn_level = thresholds[sensor_type]['warn']
            if mean_val > warn_level:
                contribution = __import__('math').ceil(mean_val / 10)
                diagnostic += contribution
    
    # Complex-looking but irrelevant adjustment
    adjustment = 0
    if 'temp' in processed_data and processed_data['temp'] > 100:
        temp_ratio = processed_data['temp'] / thresholds['temp']['crit']
        if temp_ratio > 0.9:
            adjustment += 2
        elif temp_ratio > 0.7:
            adjustment += 1
    
    # Only base diagnostic matters, adjustment not applied
    final_result = diagnostic  # Final answer derived here
    
    # Dead comparison - misleading
    if final_result > 10:
        status = 'CRITICAL'
    elif final_result > 5:
        status = 'WARNING'
    else:
        status = 'NORMAL'
    
    return final_result

# Entry point
if __name__ == '__main__':
    # Step 1: Collect raw data
    readings = collect_readings()
    
    # Step 2: Process through pipeline
    processed_data, entropy_metric, detailed_stats = process_readings(readings)
    
    # Step 3: These variables look important but aren't part of final answer
    anomaly_score = evaluate_anomaly_score(processed_data)
    data_keys = list(processed_data.keys())
    key_count = len(data_keys)
    
    # Step 4: Main analysis
    final_diagnostic = analyze_readings(processed_data, threshold_map)
    
    # Step 5: Print result as required
    print(f"Result: {final_diagnostic}")
