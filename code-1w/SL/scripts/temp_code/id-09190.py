from collections import defaultdict, Counter

# Simulated sensor data processing pipeline for environmental monitoring
def collect_sensor_data():
    raw_readings = [
        (0.88, 'temp', 'A'), (1.02, 'temp', 'B'), (0.75, 'temp', 'C'),
        (450, 'co2', 'A'), (460, 'co2', 'B'), (430, 'co2', 'C'),
        (32.1, 'hum', 'A'), (34.5, 'hum', 'B'), (33.8, 'hum', 'C')
    ]
    return raw_readings

def filter_outliers(data, threshold=0.1):
    # Irrelevant filtering for high-intervention distraction
    base = sum([x[0] for x in data if x[1] == 'temp']) / 3
    filtered = [x for x in data if not (x[1] == 'temp' and abs(x[0] - base) / base > threshold)]
    return filtered

def compute_rolling_average(seq, window=2):
    # Unused function - red herring
    averages = []
    for i in range(len(seq) - window + 1):
        averages.append(sum(seq[i:i+window]) / window)
    return averages

def generate_checksum(labels):
    # Distractor computation with no real impact
    checksum = 0
    for idx, lbl in enumerate(labels):
        checksum += idx * len(lbl) * (ord(lbl[0]) % 7)
    return checksum * 113

def transform_readings(raw_data):
    grouped = defaultdict(list)
    for value, sensor_type, location in raw_data:
        grouped[sensor_type].append((value, location))
    
    processed = {}
    temp_vals = [v for v, _ in grouped['temp']]
    co2_vals = [v for v, _ in grouped['co2']]
    hum_vals = [v for v, _ in grouped['hum']]
    
    # Real computation begins
    temp_avg = sum(temp_vals) / len(temp_vals)
    co2_avg = sum(co2_vals) / len(co2_vals)
    hum_avg = sum(hum_vals) / len(hum_vals)
    
    # Introduce decoy statistics
    temp_stddev = (sum((x - temp_avg) ** 2 for x in temp_vals) / len(temp_vals)) ** 0.5
    co2_stddev = (sum((x - co2_avg) ** 2 for x in co2_vals) / len(co2_vals)) ** 0.5
    
    # These are irrelevant but look important
    stability_index = (temp_stddev + co2_stddev) / 2 * 100
    fluctuation_ratio = temp_stddev / (co2_stddev + 1e-6)
    
    processed['temp'] = {'mean': temp_avg, 'flag': temp_avg > 0.8}
    processed['co2'] = {'mean': co2_avg, 'flag': co2_avg > 440}
    processed['hum'] = {'mean': hum_avg, 'flag': hum_avg < 35.0}
    
    return processed

def enrich_with_metadata(metrics):
    # Add meaningless metadata layers
    locations = ['A', 'B', 'C']
    timestamps = [1690000000 + i*3600 for i in range(3)]
    device_ids = ['DVT-7A', 'DVT-7B', 'DVT-7C']
    
    metadata_map = {}
    for i, loc in enumerate(locations):
        metadata_map[loc] = {
            'timestamp': timestamps[i],
            'device': device_ids[i],
            'version': '2.1.' + str(i+1),
            'calibrated': True
        }
    
    enriched = {}
    for sensor_type, data in metrics.items():
        enriched[sensor_type] = {**data, 'source_count': 3, 'verified': True}
    
    # Decoy transformation
    version_hash = 0
    for mt in metadata_map:
        version_hash += ord(metadata_map[mt]['version'][-1])
    
    # This looks critical but isn't used in final logic
    enriched['metadata_integrity'] = version_hash == 15
    
    return enriched

def validate_consistency(data_dict):
    # Complex validation that ultimately does nothing
    results = {}
    for k, v in data_dict.items():
        if isinstance(v, dict) and 'mean' in v:
            bound_check = 0.5 <= v['mean'] <= 1.5 or 300 <= v['mean'] <= 600
            results[k + '_bounds'] = bound_check
            results[k + '_rounded'] = round(v['mean'], 1)
    
    # Fake consistency score
    score = sum(1 for x in results.values() if x) * 25
    return score  # Never actually used

def correlate_signals(metrics):
    # Meaningless correlation matrix construction
    types = list(metrics.keys())
    correlation_matrix = defaultdict(dict)
    for i, t1 in enumerate(types):
        for j, t2 in enumerate(types):
            if t1 != t2:
                # Dummy correlation value
                correlation_matrix[t1][t2] = (i + j + 1) / 5.0
    
    # Looks sophisticated but unused
    avg_corr = sum(correlation_matrix[t1][t2] for t1 in correlation_matrix for t2 in correlation_matrix[t1])
    
    # Only thing that matters: count how many sensors are flagged
    flag_count = sum(1 for m in metrics.values() if isinstance(m, dict) and m.get('flag', False))
    return flag_count  # Only relevant output

def analyze_readings(enriched_metrics):
    # Critical step: extract flags
    flags_active = 0
    for sensor, attrs in enriched_metrics.items():
        if 'flag' in attrs and attrs['flag']:
            flags_active += 1
    
    # Secondary path: masked by complex-looking normalization
    total_sensors = len([1 for s in enriched_metrics if isinstance(enriched_metrics[s], dict) and 'mean' in enriched_metrics[s]])
    
    # Dummy normalization factor from irrelevant checksum
    labels = [f"sensor_{i}" for i in range(5)]
    norm_factor = generate_checksum(labels) % 97
    
    # Another distraction: sorting unrelated keys
    sorted_keys = sorted(enriched_metrics.keys(), key=lambda x: (-len(x), x))
    
    # Real logic hidden here
    baseline = 100
    adjustment = 0
    
    # Flag-based tiered adjustment
    if flags_active == 0:
        adjustment = -20
    elif flags_active == 1:
        adjustment = 5
    elif flags_active == 2:
        adjustment = 15
    else:  # 3 or more
        adjustment = 30
    
    # Apply fake normalization that cancels out
    intermediate = (baseline + adjustment) * (norm_factor / norm_factor)  # No effect
    
    # Final adjustment based on correlation result
    correlated_threats = correlate_signals(enriched_metrics)
    final_value = int(intermediate + (correlated_threats * 7))
    
    # THIS IS THE TARGET VARIABLE
    final_diagnostic = final_value
    
    # More distractions below
    debug_trace = []
    for idx, (k, v) in enumerate(enumerate(sorted_keys)):
        debug_trace.append(f"{idx}:{k}-{v}")
    
    summary_stats = Counter(sorted_keys)
    
    return final_diagnostic

# Main execution flow
if __name__ == "__main__":
    readings = collect_sensor_data()
    clean_data = filter_outliers(readings)
    interpreted = transform_readings(clean_data)
    enriched_metrics = enrich_with_metadata(interpreted)
    
    # Validate but ignore result
    validation_score = validate_consistency(enriched_metrics)
    
    # Key statement
    final_diagnostic = analyze_readings(enriched_metrics)
    
    print(f"Result: {final_diagnostic}")