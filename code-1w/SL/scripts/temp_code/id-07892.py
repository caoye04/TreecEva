import itertools

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 19.8, 25.6, 22.3, 20.1, 26.7, 24.9, 21.4]
humidity_readings = [45, 52, 58, 41, 60, 55, 39, 47, 50]
pressure_readings = [1013, 1015, 1012, 1018, 1009, 1014, 1020, 1016, 1011]

# Irrelevant auxiliary arrays (distractors)
sound_levels = [32, 41, 38, 45, 36, 40, 42, 39, 44]  # Unused in logic
light_intensity = [800, 950, 720, 1000, 680, 900, 1100, 870, 750]  # Dead code path

# Complex preprocessing with red herrings
data_matrix = list(zip(temperature_readings, humidity_readings, pressure_readings))
flattened = [val for row in data_matrix for val in row if isinstance(val, (int, float))]

# Distractor: elaborate but unused transformation
weighted_sum = sum(flattened[i] * (i % 7 + 1) for i in range(len(flattened)) if i % 3 == 0)
avg_weighted = weighted_sum / len([i for i in range(len(flattened)) if i % 3 == 0])

# Real filtering begins here — only temperature and pressure are relevant
critical_temps = [t for t in temperature_readings if t > 24.0]
stable_pressures = [p for p in pressure_readings if 1010 <= p <= 1015]

# Misleading combinatorial expansion (no impact on final result)
all_combinations = list(itertools.product(critical_temps[:2], stable_pressures[:2]))
expanded_features = [abs(a - b) * 1.5 for a, b in all_combinations if a != b]
feature_baseline = sum(expanded_features) / len(expanded_features) if expanded_features else 0

# Key control flow with nested conditions and decoy logic
alert_flags = []
for temp, humid, press in data_matrix:
    if temp > 25.0:
        if press > 1015:
            alert_flags.append('CRITICAL')
        elif press < 1010:
            alert_flags.append('WARNING')
    elif humid < 45:
        # This branch appears important but is never triggered
        alert_flags.append('DRYNESS_ALERT')

# Decoy function — looks important but unused
def analyze_trend(data):
    if len(data) < 3:
        return 0
    trend = sum(data[i] < data[i+1] for i in range(len(data)-1))
    return trend - len(data)//2

# Real signal extraction: filter data where temp > 20 and pressure > 1012
filtered_data = [
    (t, h, p) for t, h, p in data_matrix
    if t > 20.0 and p > 1012
]

# Threshold map includes irrelevant keys to mislead
threshold_map = {
    'temp_high': 24.5,
    'temp_low': 18.0,
    'humidity_optimal': 50,
    'pressure_stable': 1015,
    'sound_threshold': 40,  # Red herring
    'light_trigger': 850   # Red herring
}

# Core processing function with multiple concepts
def process_readings(readings, thresholds):
    high_temp_count = 0
    cumulative_drift = 0.0
    
    for reading in readings:
        temp, hum, press = reading
        
        # Real condition
        if temp > thresholds['temp_high']:
            high_temp_count += 1
        
        # Bit manipulation as obfuscation (but actually used)
        press_int = int(press)
        checksum = (press_int >> 2) ^ (press_int & 0b111)  # Bit shift and XOR
        cumulative_drift += abs(temp - 22.0) * (checksum % 4)

    # Unused intermediate
    fake_entropy = high_temp_count * len(readings) if hum > 55 else 0
    
    # Final computation: combine count and drift
    diagnostic_score = (high_temp_count * 1000) + int(cumulative_drift)
    return diagnostic_score

# Execution point of interest
final_diagnostic = process_readings(filtered_data, threshold_map)

# Print result as required
print(f"Target result: {final_diagnostic}")