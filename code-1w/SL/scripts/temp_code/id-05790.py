def transform_signal(raw_values, factor):
    """ Apply non-linear transformation to sensor signal (distractor function) """
    return [abs(x) ** 0.5 * factor for x in raw_values if x != 0]


def validate_checksum(data):
    """ Compute XOR checksum for data integrity (partially relevant) """
    result = 0
    for item in data:
        result ^= int(item * 100) % 256
    return result == 42  # Magic number check (red herring)


def filter_outliers(readings, limit=3):
    """ Remove statistical outliers using IQR method """
    sorted_vals = sorted(readings)
    q1 = sorted_vals[len(sorted_vals)//4]
    q3 = sorted_vals[3*len(sorted_vals)//4]
    iqr = q3 - q1
    lower, upper = q1 - limit * iqr, q3 + limit * iqr
    return [v for v in readings if lower <= v <= upper]


def decode_bitstream(bits):
    """ Convert bit array to integer (unused decoy) """
    return sum(bit * (2 ** i) for i, bit in enumerate(reversed(bits)))


def aggregate_metrics(records):
    """ Group records by type and compute averages """
    groups = {}
    for r in records:
        t = r['type']
        if t not in groups:
            groups[t] = []
        groups[t].append(r['value'])
    
    averages = {}
    for k, vals in groups.items():
        averages[k] = sum(vals) / len(vals)
    return averages


def analyze_readings(data, config):
    """ Core analysis logic: apply thresholds and count anomalies """
    anomaly_count = 0
    mode_threshold = config['mode_a']
    safety_margin = config.get('margin', 0.1)
    
    for entry in data:
        reading = entry['signal']
        category = entry['class']
        
        # Determine dynamic threshold based on class
        if category == 'X':
            limit = mode_threshold * 1.2
        elif category == 'Y':
            limit = mode_threshold * 0.8
        else:
            limit = mode_threshold
            
        adjusted_limit = limit * (1 + safety_margin)
        
        if reading > adjusted_limit:
            anomaly_count += 1
        
        # Nested condition with bit flag (misleading path)
        if reading > limit * 2:
            flag = int(reading) & 0xF
            if flag & 1:
                anomaly_count += 1  # Double penalty?

    # Secondary processing: weight by inverse frequency
    types = [e['class'] for e in data]
    freq_map = {t: types.count(t) for t in set(types)}
    weighted_score = 0
    for e in data:
        weight = 1 / freq_map[e['class']]
        if e['signal'] > config['mode_a'] * weight:
            weighted_score += weight

    final_diagnostic = anomaly_count * 100 + int(weighted_score)
    return final_diagnostic

# --- Main execution with heavy interference ---
import math

# Simulated raw sensor inputs (some irrelevant)
raw_sensor_data = [-2.3, 1.7, 4.5, 0.0, -1.2, 8.8, 3.3]
scaled_signal = transform_signal(raw_sensor_data, 1.8)

# Decoy bitstream (unused)
bit_flags = [1, 0, 1, 1, 0, 0, 1]
encoded_id = decode_bitstream(bit_flags)

# Actual operational data
readings_log = [
    {'timestamp': '2023-01-01T00:00:01', 'sensor': 'A', 'value': 12.1, 'quality': 95},
    {'timestamp': '2023-01-01T00:00:02', 'sensor': 'B', 'value': 14.3, 'quality': 87},
    {'timestamp': '2023-01-01T00:00:03', 'sensor': 'A', 'value': 11.8, 'quality': 91}
]

# Extract and filter relevant values
extracted_values = [r['value'] for r in readings_log]
cleaned_readings = filter_outliers(extracted_values, limit=2.5)

# Build main dataset for analysis
primary_data = [
    {'signal': 23.1, 'class': 'X'},
    {'signal': 19.5, 'class': 'Y'},
    {'signal': 21.0, 'class': 'X'},
    {'signal': 25.3, 'class': 'Z'},
    {'signal': 18.7, 'class': 'Y'},
    {'signal': 22.4, 'class': 'Z'}
]

# Auxiliary map with red herring entries
threshold_map = {
    'mode_a': 20.0,
    'mode_b': 15.0,
    'mode_c': 10.0,
    'margin': 0.05,
    'debug_flag': 1,
    'version': '2.1'
}

# Irrelevant aggregation (distraction)
data_types = [
    {'type': 'X', 'value': 23.1},
    {'type': 'Y', 'value': 19.5},
    {'type': 'X', 'value': 21.0}
]
type_averages = aggregate_metrics(data_types)

# Validate dummy checksum (dead end)
valid = validate_checksum(cleaned_readings)

# Key computation path
processed_data = primary_data  # Final input preparation
final_diagnostic = analyze_readings(processed_data, threshold_map)

print(f"Target result: {final_diagnostic}")