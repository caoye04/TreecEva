import itertools

def preprocess_readings(readings):
    # Irrelevant preprocessing: applies smoothing but result is unused
    smoothed = [sum(readings[i:i+3]) / 3 for i in range(len(readings) - 2)]
    normalized = [x / max(smoothed) for x in smoothed]
    return normalized

def compute_efficiency_index(sequence):
    # Real computation buried among red herrings
    powers = [x ** 2 for x in sequence]
    filtered_powers = [p for p in powers if p > 100]
    return sum(filtered_powers) // len(filtered_powers) if filtered_powers else 0

def detect_anomalies(data_stream):
    # Dead function - never called with valid data
    anomalies = []
    for i, val in enumerate(data_stream):
        if val < 0 or val > 150:
            anomalies.append((i, val))
    return anomalies

def calculate_entropy(values):
    # Distractor function using itertools
    from math import log
    freqs = {}
    for v in values:
        freqs[v] = freqs.get(v, 0) + 1
    total = len(values)
    entropy = -sum((count / total) * log(count / total) for count in freqs.values())
    return round(entropy, 4)

def validate_signal_integrity(signal):
    # Unused validation logic (decoy)
    if len(signal) < 10:
        return False
    checksum = sum(signal[::2]) - sum(signal[1::2])
    return checksum % 7 == 0

def aggregate_metrics(sensor_log, config):
    # Core logic hidden in complexity
    baseline = config['base']
    margin = config['tolerance']
    
    # Extract relevant sensor bands
    primary_band = [entry['output'] for entry in sensor_log if entry['type'] == 'primary']
    secondary_band = [entry['output'] for entry in sensor_log if entry['type'] == 'secondary']
    
    # Compute derived metrics (some irrelevant)
    avg_primary = sum(primary_band) / len(primary_band)
    peak_secondary = max(secondary_band)
    
    # Real signal: efficiency index affects final result
    index_score = compute_efficiency_index(primary_band)
    
    # Distractor: complex itertools usage with no impact
    combinations = list(itertools.combinations_with_replacement([2, 3, 5], 3))
    magic_factor = sum(a * b * c for a, b, c in combinations) % 13
    
    # Conditional path that looks important but is always skipped
    emergency_override = False
    if any(x < 0 for x in primary_band) and peak_secondary > 200:
        emergency_override = True
    
    # Hidden core logic: average of secondary, adjusted by index_score
    raw_diagnostic = (sum(secondary_band) / len(secondary_band)) + index_score
    
    # Final adjustment using baseline and tolerance (key to answer)
    final_diagnostic = int((raw_diagnostic * baseline) / (margin + 1))
    
    # Dead code: entropy not used in final calculation
    _ = calculate_entropy(primary_band)
    
    return final_diagnostic

# Simulated turbine sensor data (real input)
turbine_data = [
    {'type': 'primary', 'output': 12}, {'type': 'secondary', 'output': 45},
    {'type': 'primary', 'output': 14}, {'type': 'secondary', 'output': 50},
    {'type': 'primary', 'output': 10}, {'type': 'secondary', 'output': 40},
    {'type': 'primary', 'output': 16}, {'type': 'secondary', 'output': 55},
    {'type': 'primary', 'output': 18}, {'type': 'secondary', 'output': 60}
]

# Configuration map with misleading keys
thresholds = {
    'base': 7,
    'tolerance': 2,
    'critical': 95,
    'damping': 0.85
}

# Irrelevant data transformation
expanded_data = list(itertools.product([1, 2], ['A', 'B']))
processed = preprocess_readings([x['output'] for x in turbine_data])

# Key execution point
final_diagnostic = aggregate_metrics(turbine_data, thresholds)

# Output result
print(f"Target result: {final_diagnostic}")