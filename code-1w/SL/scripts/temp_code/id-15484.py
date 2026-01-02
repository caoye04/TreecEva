import math

# Simulated sensor data with noise and metadata
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9]
humidity_readings = [45, 47, 50, 44, 46]
pressure_readings = [1013, 1012, 1015, 1011, 1014]

# Irrelevant auxiliary data (distractor)
legacy_codes = ['A7', 'B2', 'C9', 'D4', 'E1']
checksum_lookup = {code: sum(ord(c) for c in code) % 100 for code in legacy_codes}

# Weight configuration (only some are actually used)
weights = {
    'temp': 0.4,
    'humidity': 0.3,
    'pressure': 0.2,
    'altitude_bias': 0.1,  # unused weight (red herring)
    'noise_factor': 0.05   # unused
}

# Preprocessing functions (some are decoys)
def normalize(values):
    min_val, max_val = min(values), max(values)
    return [(v - min_val) / (max_val - min_val) for v in values]

def apply_window_filter(data):
    # Hamming window (not actually applied in final path)
    window = [0.54 - 0.46 * math.cos(2 * math.pi * n / (len(data) - 1)) for n in range(len(data))]
    return [data[i] * window[i] for i in range(len(data))]

def compute_entropy(values):
    """Irrelevant computation for distraction"""
    normalized = normalize(values)
    return -sum(p * math.log2(p) for p in normalized if p > 0)

# Core transformation pipeline
def preprocess_sensor_data(raw_data):
    avg = sum(raw_data) / len(raw_data)
    centered = [x - avg for x in raw_data]
    squared_devs = [x**2 for x in centered]
    variance = sum(squared_devs) / len(squared_devs)
    std_dev = math.sqrt(variance)
    return [x / std_dev for x in centered] if std_dev != 0 else centered

# Higher-order function with lambda (used)
data_transformer = lambda func, dataset: [func(x) for x in dataset]

# Main processing workflow
def calculate_composite_index(temp, hum, pres):
    norm_temp = normalize(temp)
    norm_hum = normalize(hum)
    norm_pres = normalize(pres)
    
    # Element-wise combination using list comprehension (key step)
    index_components = [
        nt * weights['temp'] + nh * weights['humidity'] + np * weights['pressure']
        for nt, nh, np in zip(norm_temp, norm_hum, norm_pres)
    ]
    
    # Apply non-linear boost (logarithmic amplification)
    boosted = [math.log(1 + x) if x > 0 else 0 for x in index_components]
    return sum(boosted) / len(boosted)

# Dead function - looks important but unused (distractor)
def validate_calibration_sequence(seq):
    cumulative = 0
    for i, val in enumerate(seq):
        cumulative = (cumulative * 31 + hash(str(val))) % 10007
    return cumulative > 5000

# Complex nested function with multiple concepts
def calculate_final_score(data, config):
    temp_data = data['temperature']
    hum_data = data['humidity']
    pres_data = data['pressure']
    
    # Multiple preprocessing layers (only one ultimately matters)
    processed_temp = preprocess_sensor_data(temp_data)
    processed_hum = [x / 100 for x in hum_data]  # simple scaling
    processed_pres = [p / 1000 for p in pres_data]
    
    # Set operations to filter outliers (meaningful use)
    valid_indices = set(range(len(temp_data))) - {i for i, t in enumerate(temp_data) if abs(t - 25.0) > 2}
    
    # Use of set filtering in list comprehension
    filtered_temp = [processed_temp[i] for i in range(len(processed_temp)) if i in valid_indices]
    filtered_hum = [processed_hum[i] for i in range(len(processed_hum)) if i in valid_indices]
    filtered_pres = [processed_pres[i] for i in range(len(processed_pres)) if i in valid_indices]
    
    # Secondary validation (looks complex but deterministic)
    if len(filtered_temp) < 3:
        fallback_weights = {k: v * 0.5 for k, v in config.items()}
        primary_index = 0.5
    else:
        # This is the actual execution path
        primary_index = calculate_composite_index(
            [temp_data[i] for i in valid_indices],
            [hum_data[i] for i in valid_indices],
            [pres_data[i] for i in valid_indices]
        )
        
        # Red herring: entropy calculation not used in output
        temp_entropy = compute_entropy([t for i, t in enumerate(temp_data) if i in valid_indices])
        hum_entropy = compute_entropy([h for i, h in enumerate(hum_data) if i in valid_indices])
        total_entropy = (temp_entropy + hum_entropy) / 2
        
        # Dummy adjustment that doesn't affect final score
        adjustment_factor = math.sin(total_entropy) if total_entropy > 0 else 0
        
    # Final aggregation with hidden offset
    base_score = primary_index * 100
    quality_bonus = len(valid_indices) * 2  # bonus for sample retention
    stability_penalty = math.exp(-len(filtered_temp)) * 10
    
    # Critical final computation
    final_raw = base_score + quality_bonus - stability_penalty
    
    # Normalize through sigmoid-like clamp
    final_clamped = 100 / (1 + math.exp(-final_raw / 50))
    
    # Decoy rounding (not used)
    precise_result = round(final_clamped, 4)
    rough_estimate = int(round(final_clamped))
    
    # ACTUAL RETURN VALUE
    return final_clamped  # This becomes final_score

# Unused diagnostic function (distractor)
def generate_diagnostic_report():
    report = {}
    report['sample_count'] = len(temperature_readings)
    report['data_integrity'] = all(t > -40 and t < 80 for t in temperature_readings)
    report['consistency_check'] = checksum_lookup.get('A7') == 34
    return report

# Data packaging
sensor_data = {
    'temperature': temperature_readings,
    'humidity': humidity_readings,
    'pressure': pressure_readings,
    'timestamp': '2023-11-15T10:30:00Z',
    'location_id': 4201
}

# Execute main logic
intermediate_entropy = compute_entropy(pressure_readings)  # distractor call

# Key execution point
final_score = calculate_final_score(sensor_data, weights)

# Print result as required
print(f"Result: {final_score}")