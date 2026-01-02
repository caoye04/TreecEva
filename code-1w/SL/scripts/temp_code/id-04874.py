import itertools

# Simulated sensor array diagnostics with noise filtering and pattern analysis
def collect_sensor_data():
    raw_readings = [127, 255, 64, 192, 32, 168, 96, 224]
    noise_floor = 30
    filtered = [x for x in raw_readings if x > noise_floor]
    return filtered

# Irrelevant helper - simulates temperature scaling (not used in final path)
def scale_by_temperature(data, temp=22.5):
    scaled = [int(x * (1 + (temp - 20) / 100)) for x in data]
    return scaled  # Dead code path — never called in execution flow

# Signal processor with bit manipulation and thresholding
def process_signal(raw): 
    shifted = [(x >> 2) & 63 for x in raw]  # Normalize via bit shift and mask
    enhanced = []
    for val in shifted:
        if val % 2 == 0:
            enhanced.append(val + 5)
        else:
            enhanced.append(val * 2)
    return enhanced

# Red herring function: performs set operations but returns unused result
def detect_anomalies(readings):
    high_vals = {x for x in readings if x > 50}
    mid_vals = {x for x in readings if 25 <= x <= 50}
    anomalies = high_vals - mid_vals
    backup_copy = readings.copy()  # Unused distraction
    return sorted(list(anomalies), reverse=True)  # Computed but ignored later

# Core logic chain — recursive frequency counter (relevant)
def count_frequency_recursive(data, index=0, freq=None):
    if freq is None:
        freq = {}
    if index >= len(data):
        return freq
    key = data[index]
    freq[key] = freq.get(key, 0) + 1
    return count_frequency_recursive(data, index + 1, freq)

# Higher-order transformation using itertools (used in critical path)
def generate_patterns(seq):
    permutations = list(itertools.permutations(seq[:3]))  # Only use first 3 elements
    sums = []
    for p in permutations:
        sums.append(sum(p))
    unique_sums = list(set(sums))  # Remove duplicates
    return sorted(unique_sums)

# Decoy dictionary aggregation — looks important but unused
def aggregate_metrics(results):
    report = {}
    report['total'] = sum(results)
    report['max'] = max(results)
    report['min'] = min(results)
    report['range'] = report['max'] - report['min']
    report['midpoint'] = (report['min'] + report['max']) / 2
    return report  # Calculated but not used

# Primary analysis pipeline
processed_signals = []
def analyze_readings(signals):
    global processed_signals
    processed_signals = process_signal(signals)
    
    # Recursive frequency map (key dependency)
    freq_map = count_frequency_recursive(processed_signals)
    
    # Extract keys that appear more than once
    repeated_values = [k for k, v in freq_map.items() if v > 1]
    
    # Generate combinatorial patterns from repeated values (if any)
    if len(repeated_values) >= 3:
        pattern_sums = generate_patterns(repeated_values)
        base_score = sum(pattern_sums) // len(pattern_sums)
    else:
        # Inject decoy logic with misleading intermediate
        dummy_set = {x**2 for x in range(8)}  # Distractor computation
        temp_dict = {'a': 100, 'b': 200}; temp_dict.update({'c': 300})  # Noise
        base_score = 42 * len(repeated_values) + 17
    
    # Final diagnostic uses length of processed signals and base score
    adjustment = len(processed_signals) % 7
    final_diagnostic = base_score * 3 + adjustment
    
    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Execution flow
sensor_data = collect_sensor_data()
_ = detect_anomalies(sensor_data)  # Runs but result discarded
_ = aggregate_metrics(sensor_data)  # Another unused metric aggregation

final_diagnostic = analyze_readings(processed_signals)