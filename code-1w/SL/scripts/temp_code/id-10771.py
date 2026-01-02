def preprocess_signal(raw_samples):
    # Irrelevant normalization (dead path)
    normalized = [x / max(raw_samples) for x in raw_samples if x > 0]
    offset = sum(1 for x in raw_samples if x < -50)  # Distractor count

    # Actual relevant transformation
    processed = []
    for idx, val in enumerate(raw_samples):
        if idx % 3 == 0:
            processed.append(abs(val) // 2)
        elif val > 0:
            processed.append(val % 7)
    return processed


def generate_checksum(sequence):
    # Complex but ultimately irrelevant computation
    checksum = 0
    for i, num in enumerate(sequence):
        checksum ^= (num + i) * 3
    return checksum % 1000  # Never used in final result


def filter_anomalies(data_stream):
    anomalies = []
    for i in range(1, len(data_stream)):
        if data_stream[i] - data_stream[i-1] > 10:
            anomalies.append(i)
    # Return original data — anomalies list unused
    return data_stream  # No filtering actually applied


def compute_entropy(values):
    from math import log2
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    total = len(values)
    entropy = sum(-(count/total) * log2(count/total) for count in freq.values())
    return round(entropy, 4)


def build_index_map(segments):
    # Use of enumerate and zip (required Python feature)
    indices = list(range(len(segments)))
    index_map = dict(zip(segments, indices))
    return index_map


def analyze_readings(readings, config):
    base_level = config['base']
    scaling = config.get('scale', 1)
    aggregate = 0
    
    for i, reading in enumerate(readings):
        if i % 2 == 0:
            temp = (reading + base_level) * scaling
n            if temp > 100:
                temp = 100
            aggregate += temp
        else:
            adjustment = config['adjustments'][i % len(config['adjustments'])]
            adjusted = reading - adjustment
            aggregate -= abs(adjusted) // 3
    
    # Key logic: modular arithmetic and integer division
    intermediate = (aggregate // 4) % 857
    final_score = (intermediate * 2) - 34
    
    # Critical answer variable
    final_diagnostic = final_score
    return final_diagnostic

# Main execution sequence
if __name__ == '__main__':
    # Initial sensor data
    sensor_log = [120, -30, 45, 60, 180, -200, 75, 90, 130]
    
    # Irrelevant data structures (distractors)
    device_caps = {'gain': 2.1, 'offset_limit': 40, 'temp_range': (-20, 85)}
    calibration_matrix = [[1, 0], [0, 1], [2, -1]]  # Unused
    metadata_trace = [{'id': 'A', 'ts': 100}, {'id': 'B', 'ts': 105}]
    
    # Step 1: Preprocess signal (only uses part of the logic)
    cleaned_samples = preprocess_signal(sensor_log)
    
    # Step 2: Generate checksum (never used)
    chksum = generate_checksum(cleaned_samples)
    
    # Step 3: Attempt to filter anomalies (returns original)
    filtered_data = filter_anomalies(cleaned_samples)
    
    # Step 4: Compute entropy (distraction metric)
    entropy_value = compute_entropy(filtered_data)
    
    # Step 5: Build index map using enumerate and zip (required)
    segment_keys = ['low', 'mid', 'high', 'ultra']
    key_index_map = build_index_map(segment_keys)
    
    # Step 6: Create configuration map (used in analysis)
    threshold_map = {
        'base': 10,
        'scale': 2,
        'adjustments': [5, 8, 3]
    }
    
    # Step 7: Analyze readings — critical statement
    final_diagnostic = analyze_readings(filtered_data, threshold_map)
    
    # Output target result
    print(f"Target result: {final_diagnostic}")