import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 27.1, 25.8, 24.7, 23.9]
humidity_readings = [45, 47, 50, 55, 60, 62, 58, 53, 49]
pressure_readings = [1013, 1012, 1014, 1015, 1016, 1018, 1017, 1015, 1014]

# Irrelevant auxiliary data (distractor)
legacy_codes = ['A7', 'B2', 'C9', 'D4', 'E1', 'F8', 'G3', 'H6', 'I5']
lookup_matrix = [[i * j + 2 for j in range(4)] for i in range(4)]

# Mapping sensor zones to sensitivity thresholds (relevant)
zone_specs = {
    'core': {'temp': 25.0, 'humidity': 55},
    'perimeter': {'temp': 24.0, 'humidity': 50},
    'auxiliary': {'temp': 26.0, 'humidity': 60}
}

# Decoy function - never called (dead code path)
def legacy_transform(data):
    return [round(x ** 0.5 * 1.2, 2) for x in data if x > 0]

# Real preprocessing function with slicing and filtering
def preprocess_sensors(raw_temps, raw_humid):
    # Normalize using sliding window average (centered)
    smoothed_temps = []
    window_size = 3
    for i in range(len(raw_temps)):
        start = max(0, i - window_size // 2)
        end = min(len(raw_temps), i + window_size // 2 + 1)
        smoothed_temps.append(sum(raw_temps[start:end]) / (end - start))
    
    # Humidity correction via polynomial adjustment (irrelevant to final answer but looks important)
    adjusted_humid = [h * (1 + 0.002 * h) for h in raw_humid]
    
    # Return only temperature processing result (humid ignored)
    return smoothed_temps[:len(smoothed_temps) - 1]  # slice off last element for alignment

# Secondary transformation with set operations (partial red herring)
def generate_anomaly_flags(data_slice):
    high_vals = {i for i, x in enumerate(data_slice) if x > 25.0}
    low_vals = {i for i, x in enumerate(data_slice) if x < 24.0}
    fluctuation_indices = high_vals ^ low_vals  # XOR: either high or low but not both
    
    # Create decoy flag map (never used later)
    flag_map = {}
    for idx in range(len(data_slice)):
        if idx in high_vals & low_vals:
            flag_map[idx] = 'ERR_DOUBLE'
        elif idx in high_vals:
            flag_map[idx] = 'HIGH_TEMP'
        elif idx in low_vals:
            flag_map[idx] = 'LOW_TEMP'
        else:
            flag_map[idx] = 'NORMAL'
    
    return list(fluctuation_indices)

# Core analysis logic depending on dictionary lookups and comparisons
def analyze_readings(cleaned_temps, thresholds):
    core_limit = thresholds['core']['temp']
    perimeter_limit = thresholds['perimeter']['temp']
    aux_limit = thresholds['auxiliary']['temp']
    
    counts = {'critical': 0, 'elevated': 0, 'normal': 0}
    
    for val in cleaned_temps:
        if val > aux_limit:
            counts['critical'] += 1
        elif val > core_limit:
            counts['elevated'] += 1
        else:
            counts['normal'] += 1
    
    # Final diagnostic computed from imbalance ratio
    critical_count = counts['critical']
    elevated_count = counts['elevated']
    
    if critical_count == 0 and elevated_count == 0:
        base_score = 100
    elif critical_count == 0:
        base_score = 75 - (elevated_count * 2)
    else:
        base_score = 50 - (critical_count * 5) - (elevated_count * 2)
    
    # Apply non-linear penalty for volatility (uses string method on dummy id)
    site_id = "ENV-STA-001"
    checksum_weight = len(site_id.split('-'))  # evaluates to 3
    
    final_risk = base_score - (len(generate_anomaly_flags(cleaned_temps)) * 1.5)
    
    # This is the actual answer variable
    return round(final_risk, 4)

# Misleading intermediate pipeline stage (partially unused)
filtered_pairs = [(t, h) for t, h in zip(temperature_readings, humidity_readings) if t > 23.0]
extracted_temps = [pair[0] for pair in filtered_pairs]

# Real execution flow begins here
processed_data = preprocess_sensors(extracted_temps, humidity_readings)

# Build threshold map (only this matters)
threshold_map = zone_specs  # direct assignment

# Dead code: builds unused structure
compliance_registry = set()
for zone in threshold_map:
    compliance_registry.add(f"{zone.upper()}_THRESH_APPLIED")

# Key statement that produces the target variable
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")