from collections import defaultdict, Counter

# Simulated sensor network data with metadata
def collect_diagnostics():
    raw_readings = [
        (102, 'temp', 'sensor_A'), (155, 'pressure', 'sensor_B'),
        (102, 'temp', 'sensor_A'), (98, 'temp', 'sensor_C'),
        (201, 'vibration', 'sensor_D'), (155, 'pressure', 'sensor_B'),
        (98, 'temp', 'sensor_C'), (305, 'current', 'sensor_E'),
        (201, 'vibration', 'sensor_D'), (102, 'temp', 'sensor_A')
    ]

    # Irrelevant aggregation: counts all labels but only temp matters later
    label_counter = Counter(label for _, label, _ in raw_readings)
    
    # Misleading transformation: creates a normalized map across all values
    total_sum = sum(value for value, _, _ in raw_readings)
    normalized_weights = {label: count * 100 / len(raw_readings) 
                          for label, count in label_counter.items()}

    # Distractor function - never called
    def analyze_anomaly_pattern(seq):
        return [x for x in seq if x > 200]

    # Key preprocessing: extract only temperature readings
    temp_data = [(val, sid) for val, lbl, sid in raw_readings if lbl == 'temp']

    # Dead code path: simulates calibration that isn't used
    calibration_offsets = defaultdict(int)
    for sensor_id in set(sid for _, sid in temp_data):
        calibration_offsets[sensor_id] = hash(sensor_id) % 5

    # Decoy computation: builds unused summary stats
    decoy_stats = {}
    for sensor_id in set(s for _, s in temp_data):
        decoy_stats[sensor_id] = {
            'count': len([v for v, s in temp_data if s == sensor_id]),
            'apparent_range': (min([v for v, s in temp_data if s == sensor_id]),
                             max([v for v, s in temp_data if s == sensor_id]))
        }

    # Real logic begins: filter duplicates using enumerated uniqueness
    unique_temp_readings = []
    seen = set()
    for idx, (value, sensor_id) in enumerate(temp_data):
        key = (value, sensor_id, idx % 2)  # artificial uniqueness via index parity
        if value not in seen:
            seen.add(value)
            unique_temp_readings.append((value, sensor_id))

    # Secondary filtering based on frequency (using enumerate to track order)
    freq_map = Counter(v for v, _ in unique_temp_readings)
    filtered_data = []
    for i, (value, sensor) in enumerate(unique_temp_readings):
        # Only include if value appears at least twice in original and index is even
        if freq_map[value] >= 2 and i % 2 == 0:
            filtered_data.append({'reading': value, 'node': sensor, 'seq_id': i})

    # Build threshold map — only one entry will be used later
    threshold_map = defaultdict(lambda: 100)
    threshold_map['temp'] = 100
    threshold_map['pressure'] = 200  # irrelevant
    threshold_map['vibration'] = 300  # irrelevant
    threshold_map['current'] = 400   # irrelevant

    # Unused complex structure: simulates configuration cascade
    config_tree = {}
    for t in ['A', 'B', 'C']:
        config_tree[t] = []
        for level in range(3):
            inner = {}
            for prop in ['gain', 'offset', 'active']:
                inner[prop] = (hash(t + prop) + level) % 100
            config_tree[t].append(inner)

    # Actual processing function
    def process_readings(data_list, thresholds):
        result = 0
        temp_threshold = thresholds['temp']
        
        # Use zip to pair readings with pseudo-timestamps
        timestamps = list(range(1000, 1000 + len(data_list)))
        for entry, ts in zip(data_list, timestamps):
            base_val = entry['reading']
            node_char = entry['node'][-1]
            # Character counting affects weight
            char_code = ord(node_char.lower()) - ord('a')
            
            # Weighted contribution: only entries above threshold contribute
            if base_val > temp_threshold:
                weight = char_code * (ts % 7)
                result += (base_val * weight) // (ts % 9 + 1)
            else:
                # Below threshold: add fixed offset unrelated to final answer
                result += base_val % 17
                
            # Red herring: modify result based on unused property
            if 'seq_id' in entry and entry['seq_id'] > 5:
                result -= 50  # never reached due to filtering

        # Final adjustment: bitwise manipulation with constant
        result ^= 0xABCD
        result &= 0xFFFF
        if result > 32767:
            result -= 65536
        return result

    final_diagnostic = process_readings(filtered_data, threshold_map)
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

if __name__ == "__main__":
    collect_diagnostics()