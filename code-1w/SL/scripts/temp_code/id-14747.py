def preprocess_sensor(stream, cutoff):
    processed = []
    temp_accum = 0
    count = 0
    
    for val in stream:
        if val < 0:
            continue
        if val > cutoff:
            temp_accum += val * 0.85
        else:
            temp_accum += val
        count += 1
        if count % 3 == 0:
            processed.append(round(temp_accum / count, 2))
            temp_accum = 0  # Reset accumulator every 3 valid entries
    return processed if processed else [0]


def validate_checksum(data):
    # Irrelevant validation function (dead logic path)
    total = 0
    for d in data:
        total ^= int(d * 100) % 255
    return total % 16 == 0


def extract_features(signal):
    # Distractor: feature extraction not used in final path
    magnitude = sum(abs(x) for x in signal)
    peaks = [i for i in range(1, len(signal)-1) if signal[i-1] < signal[i] > signal[i+1]]
    smooth = [sum(signal[i:i+3])/3 for i in range(len(signal)-2)]
    return {
        'energy': magnitude,
        'peak_count': len(peaks),
        'stability': round(smooth[-1] if smooth else 0, 2)
    }


def filter_outliers(seq, factor=1.5):
    if len(seq) < 2:
        return seq
    sorted_vals = sorted(seq)
    q1 = sorted_vals[len(sorted_vals)//4]
    q3 = sorted_vals[3*len(sorted_vals)//4]
    iqr = q3 - q1
    lower, upper = q1 - factor * iqr, q3 + factor * iqr
    return [x for x in seq if lower <= x <= upper]


def compute_entropy(values):
    # Misleading intermediate calculation
    from math import log2
    if not values:
        return 0.0
    freqs = {}
    total = len(values)
    for v in values:
        freqs[v] = freqs.get(v, 0) + 1
    entropy = -sum((count/total) * log2(count/total) for count in freqs.values())
    return round(entropy, 4)


def analyze_readings(data_list, config_map):
    base_score = 0
    adjustment = config_map['alpha']
    
    for entry in data_list:
        if 'value' not in entry or 'mode' not in entry:
            continue
        raw_val = entry['value']
        mode = entry['mode']
        
        if mode == 'A':
            base_score += raw_val * adjustment
        elif mode == 'B':
            base_score += raw_val * (adjustment / 2)
        else:
            base_score -= raw_val * 0.1
    
    # Critical manipulation using slicing to derive result
    history_log = [base_score * 0.9, base_score, base_score * 1.1, base_score * 1.2, base_score * 1.3]
    recent_trend = history_log[-3:]  # Use last 3 elements
    trend_growth = recent_trend[2] - recent_trend[0]
    
    # Final computation
    diagnostic_weight = config_map['beta'] * len(data_list)
    final_diagnostic = int(round(base_score + trend_growth - diagnostic_weight))
    
    return final_diagnostic

# --- Main Execution with High Interference ---
sensor_input = [12.5, -3.2, 18.0, 9.7, 25.4, 14.3, -1.8, 30.1, 11.9, 8.8]

# Irrelevant transformations
normalized = [max(0, x) for x in sensor_input]
delta_seq = [round(normalized[i+1] - normalized[i], 2) for i in range(len(normalized)-1)]
smoothed = [sum(normalized[i:i+3])/3 for i in range(len(normalized)-2)]

# Apply preprocessing with side effects
primary_cycle = preprocess_sensor(sensor_input, cutoff=20.0)

# Dead code branch: checksum not actually used
is_valid = validate_checksum(primary_cycle)

# Feature extraction (distractor)
features = extract_features(primary_cycle)

# Real pipeline begins
raw_segments = [
    {'value': 42, 'mode': 'A'},
    {'value': 38, 'mode': 'B'},
    {'value': 44, 'mode': 'A'},
    {'value': 40, 'mode': 'C'},
    {'value': 36, 'mode': 'B'}
]

# Filtering with slicing distraction
segment_values = [seg['value'] for seg in raw_segments]
filtered_values = filter_outliers(segment_values, factor=1.2)

# Reconstruct filtered segments
filtered_data = []
for v in filtered_values:
    match = next((s for s in raw_segments if s['value'] == v), None)
    if match:
        filtered_data.append(match)

# Entropy computed but unused (red herring)
entropy_metric = compute_entropy(filtered_values)

# Configuration map with relevant and irrelevant keys
threshold_map = {
    'alpha': 1.75,
    'beta': 2.3,
    'gamma': 0.88,  # Unused parameter
    'debug_mode': False  # Unused flag
}

# Key statement
final_diagnostic = analyze_readings(filtered_data, threshold_map)

# Output result
print(f"Result: {final_diagnostic}")