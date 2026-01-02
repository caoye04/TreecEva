import math

# Simulated sensor data and calibration constants
temperature_readings = [23.5, 24.1, 22.9, 25.6, 26.0, 24.8]
pressure_readings = [101.3, 102.1, 100.9, 103.5, 104.0, 101.8]
humidity_readings = [45.2, 47.8, 44.1, 50.3, 52.0, 48.6]

# Irrelevant auxiliary data (distraction)
color_spectrum = ['red', 'green', 'blue', 'infrared']
sample_ids = {1001, 1002, 1003, 1004}
metadata_log = {'version': '2.1', 'mode': 'diagnostic'}

# Calibration offset (unused red herring)
calibration_matrix = [[1.02, -0.01], [0.03, 0.99]]

# Signal preprocessing functions
def normalize(values):
    mean_val = sum(values) / len(values)
    return [(v - mean_val) * 1.05 for v in values]

def amplify_outliers(values, threshold=1.5):
    normalized = normalize(values)
    amplified = []
    for v in normalized:
        if abs(v) > threshold:
            amplified.append(v * 1.8)
        else:
            amplified.append(v)
    return amplified

# Unused decoy function (dead path)
def deprecated_filter(data):
    return [x for x in data if x > 0.5]

# Complex transformation chain
baseline_shift = sum(temperature_readings[:3]) / 3 * 0.01
adjusted_pressure = [p + baseline_shift for p in pressure_readings]

# Apply multiple transformations with distractor logic
transformed_humidity = [
    (h + 10) ** 0.5 if h < 48 else (h - 40) * 0.9
    for h in humidity_readings
]

# Create composite index using lambda and set operations (required features)
index_mapper = lambda x: int((x * 2.1) % 7)
humidity_indices = set(map(index_mapper, humidity_readings))
pressure_indices = set([index_mapper(p) for p in adjusted_pressure])
overlap_count = len(humidity_indices & pressure_indices)  # Red herring usage

# Intermediate diagnostic with misleading relevance
interim_score = overlap_count * 1000  # Looks important but unused

# Core signal processing (hidden among distractions)
processed_data = [
    temperature_readings[i] * 0.3 + \
    adjusted_pressure[i] * 0.5 + \
    transformed_humidity[i] * 0.2
    for i in range(len(temperature_readings))
]

# Conditional scaling based on case conversion logic (suggested paradigm)
system_mode = 'ACTIVE'
scaling_factor = 1.2 if system_mode.lower() == 'active' else 0.8

processed_data = [x * scaling_factor for x in processed_data]

# Analysis function with nested logic and distractors
def analyze_signal(signal):
    if not signal:
        return 0
    
    # Distractor: complex unused calculation
    peak = max(signal)
    trough = min(signal)
    volatility = (peak - trough) / ((peak + trough) / 2) if peak + trough != 0 else 0
    
    # Decoy conditional expression
    fallback = 42 if len(signal) > 10 else 84
    
    # Real computation buried in noise
    valid_samples = [s for s in signal if s > 25.0]  # Filtering condition
    if len(valid_samples) == 0:
        correction = -5.5
    else:
        correction = sum(valid_samples) / len(valid_samples) * 0.1
    
    # Key accumulation logic
    accumulator = 0
    for val in signal:
        if val > 24.5:
            accumulator += math.sin(val * 0.1)  # Nonlinear transformation
        else:
            accumulator += math.cos(val * 0.1)
    
    # Final composition (answer depends on this)
    base_result = sum(signal) / len(signal)
    final_value = base_result + accumulator + correction
    
    # Dead code path
    if False:
        final_value = final_value * 0.9 + 10
    
    return final_value

# Critical execution point
final_diagnostic = analyze_signal(processed_data)

# Print result as required
print(f"Target result: {final_diagnostic}")