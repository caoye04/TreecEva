import itertools

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 19.8, 22.0, 25.3, 26.7, 20.4, 21.9, 24.8, 23.0]
humidity_readings = [45, 48, 55, 60, 52, 47, 58, 62, 50, 49]
pressure_readings = [1013, 1015, 1012, 1018, 1010, 1008, 1014, 1016, 1011, 1009]

# Irrelevant auxiliary arrays (distractors)
sound_levels = [32, 35, 40, 38, 45, 33, 30, 42, 39, 41]  # Unused in final calculation
light_intensity = [800, 850, 700, 900, 600, 750, 880, 820, 760, 890]  # Dead code path

# Complex preprocessing with red herrings
def apply_calibration(data, factor=1.0, offset=0.0):
    return [(x * factor) + offset for x in data]

def slice_window(data, start, end):
    return data[start:end]

# Misleading transformation chain (partially unused)
calibrated_temp = apply_calibration(temperature_readings, 1.02, -0.5)
calibrated_humid = apply_translation(humidity_readings, 0.95, 2.0)  # Calls undefined function → fallback below
calibrated_humid = [x * 0.95 + 2 for x in humidity_readings]  # Actual execution due to NameError fallback logic

# Dead function — looks important but unused
def analyze_trend(sequence):
    differences = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
    return sum(differences) / len(differences)

# Real processing begins here — filtering relevant data
valid_indices = [i for i in range(len(temperature_readings)) if 20 <= temperature_readings[i] <= 25]
filtered_data = {
    'temp': [calibrated_temp[i] for i in valid_indices],
    'humid': [calibrated_humid[i] for i in valid_indices],
    'press': [pressure_readings[i] for i in valid_indices]
}

# Decoy dictionary operations (irrelevant)
stats_snapshot = {
    'max_temp': max(calibrated_temp),
    'min_humid': min(calibrated_humid),
    'avg_press': sum(pressure_readings) / len(pressure_readings),
    'timestamp': '2023-11-05T14:30:00Z',
    'location_id': 7,
    'version': 'v2.3'
}

# Bit manipulation decoy — simulates error checking but unused
checksum = 0
for val in humidity_readings[:5]:
    checksum ^= int(val)
    checksum = (checksum << 1) & 0xFF | (checksum >> 7)

# Threshold logic with dictionary mapping (key part)
threshold_map = {
    'temp_warn': 24.5,
    'temp_crit': 26.0,
    'humid_low': 46,
    'humid_high': 54
}

# Conditional slicing based on dynamic keys (relevant)
dynamic_slice = lambda d, k: d['temp'][k:] if threshold_map['temp_warn'] > 24.0 else d['temp'][:k]

# Core logic hidden among distractions
def evaluate_stability(temp_list, humid_list):
    score = 0
    for t, h in zip(temp_list, humid_list):
        if t < 24.5 and h > 50:
            score += t * (h / 10)
        elif t >= 24.5 and h < 50:
            score -= t * 0.5
    return round(score, 4)

# Higher-order function with itertools (actual usage)
def process_readings(data, thresholds):
    temp_slice = dynamic_slice(data, 2)
    paired_stream = list(itertools.zip_longest(temp_slice, data['humid'], fillvalue=0))
    
    # Spurious intermediate calculation (red herring)
    aggregate_pressure = sum(data['press']) * 0.01
    dummy_mask = [int(x) & 3 for x in data['press']]  # Bitwise distraction
    
    # Actual scoring logic
    stability_score = evaluate_stability(data['temp'], data['humid'])
    
    # Final diagnostic uses XOR on rounded components (bitwise + arithmetic)
    base_value = int(abs(stability_score))
    modifier = len(temp_slice) ^ 5  # XOR operation
    final_diagnostic = base_value * modifier - aggregate_pressure
    
    return final_diagnostic

# Execute main logic
final_diagnostic = process_readings(filtered_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")