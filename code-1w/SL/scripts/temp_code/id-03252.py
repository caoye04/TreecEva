import itertools

# Simulated sensor data from multiple environmental monitoring stations
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9, 24.4, 26.0, 23.2]
humidity_readings = [45, 47, 50, 44, 48, 52, 43, 46]
pressure_readings = [1013, 1015, 1012, 1016, 1014, 1011, 1017, 1013]

# Irrelevant auxiliary data (distractor)
legacy_codes = ['A7', 'B2', 'C9', 'D4', 'E1', 'F8', 'G5', 'H3']
user_preferences = { 'theme': 'dark', 'refresh_rate': 60, 'units': 'metric' }

# Misleading intermediate processing (red herring)
def calculate_stability_index(data):
    return sum(d ** 0.5 for d in data if d > 0) / len(data)

stability_proxy = calculate_stability_index(pressure_readings)  # Not used later

# Data alignment via zip (relevant)
synchronized_data = list(zip(temperature_readings, humidity_readings, pressure_readings))

def extract_anomalies(dataset):
    anomalies = []
    for i, (temp, hum, pres) in enumerate(dataset):
        if temp > 24.0 and hum < 46:
            anomalies.append((i, temp, hum))
    return anomalies

# Anomaly detection (partially relevant)
detected_outliers = extract_anomalies(synchronized_data)

# Decoy function with unused logic (dead code path)
def deprecated_normalization(arr):
    min_val, max_val = min(arr), max(arr)
    return [(x - min_val) / (max_val - min_val) for x in arr]

# Complex transformation chain (core logic)
def generate_processing_layers(data_sequence):
    layers = []
    for idx, (t, h, p) in enumerate(data_sequence):
        phase_shift = (t * h) % 7
        encoded = (p + t) ^ int(phase_shift)  # Bitwise mix
        layers.append({
            'node_id': idx,
            'encoded_value': encoded,
            'quality_flag': p > 1013,
            'aux': (t, h)
        })
    return layers

processing_chain = generate_processing_layers(synchronized_data)

# Distractor: fake reduction operation (misleading)
compressed_snapshot = [sum(x) for x in itertools.combinations(humidity_readings, 2)][:8]

# Real metric aggregator (key computation)
def aggregate_metrics(layers, log_entries=None):
    total_score = 0
    adjustment_factor = 0.87

    # Accumulate based on encoded values and flags
    for item in layers:
        if item['quality_flag']:
            total_score += item['encoded_value'] * 1.1
        else:
            total_score += item['encoded_value'] * 0.9
    
    # Apply recursive refinement (actual dependency)
    def refine_accumulator(value, depth=2):
        if depth == 0:
            return value
        refined = sum(int(c) for c in str(abs(int(value))) if c.isdigit())
        return refine_accumulator(value + refined, depth - 1)
    
    final_refined = refine_accumulator(total_score)
    
    # Slicing-based correction using enumerate (idiomatic python)
    correction_pool = [i for i, layer in enumerate(layers) if layer['node_id'] % 2 == 0]
    slice_offset = sum(correction_pool[::2]) if len(correction_pool) > 2 else 0
    
    return int(final_refined + slice_offset)

# Dummy diagnostic log (distractor)
diagnostics = {
    'timestamp': '2023-11-05T10:30:00Z',
    'station_count': 8,
    'version': '2.1.0'
}

# Critical execution point
final_diagnostic = aggregate_metrics(processing_chain, diagnostics)

# Unused bit manipulation sequence (decoy)
rolling_hash = 0
for code in legacy_codes:
    rolling_hash ^= hash(code) >> 4  # Dead end

Result: final_diagnostic