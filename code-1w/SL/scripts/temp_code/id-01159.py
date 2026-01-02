import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.9, 25.3, 26.0, 24.8, 23.7, 22.5]
humidity_readings = [45, 47, 50, 55, 60, 58, 53, 49]
pressure_readings = [1013, 1015, 1012, 1008, 1005, 1007, 1010, 1014]

# Irrelevant calibration coefficients (distractor)
calib_a, calib_b, calib_c = 1.02, -0.05, 0.98
adjusted_temps = [t * calib_a + calib_b for t in temperature_readings]

# Data preprocessing with red herring transformations
smoothed_humidity = []
for i in range(len(humidity_readings)):
    window = humidity_readings[max(0, i-1):min(i+2, len(humidity_readings))]
    smoothed_humidity.append(sum(window) / len(window))

# Decoy transformation function (never used)
def transform_pressure(p):
    return round(math.log(p) * 100, 2)

# Real processing begins here
processed_data = []
for i in range(len(temperature_readings)):
    entry = {
        'idx': i,
        'temp': temperature_readings[i],
        'humid': smoothed_humidity[i],
        'press': pressure_readings[i],
        'score': 0  # Will be computed based on rules
    }
    # Compute composite score using bitwise and arithmetic ops
    temp_factor = int((entry['temp'] - 20) * 10)
    humid_factor = int(entry['humid'] // 5)
    press_factor = entry['press'] % 100
    
    # Complex scoring with red herrings
    raw_score = (temp_factor << 1) ^ humid_factor
    raw_score = raw_score & 0xFF  # Clamp to 8 bits
    
    # Distractor: unused alternative scoring
    alt_score = (press_factor ** 2) >> 2
    if raw_score > 100:
        raw_score -= alt_score // 3  # Rarely executed dead path
    
    entry['score'] = raw_score
    processed_data.append(entry)

# Threshold configuration map (critical)
threshold_map = {
    'high_risk': 150,
    'elevated': 100,
    'normal': 50
}

# Misleading auxiliary function (not part of main logic)
def compute_stability_index(data):
    diffs = [abs(data[i]['temp'] - data[i-1]['temp']) for i in range(1, len(data))]
    return sum(diffs) / len(diffs)

stability = compute_stability_index(processed_data)  # Unused result

# Another decoy structure
summary_stats = {
    'max_temp': max(t for t in temperature_readings),
    'min_press': min(p for p in pressure_readings),
    'avg_humid': sum(smoothed_humidity) / len(smoothed_humidity)
}

# Core analysis function with conditional logic and list comprehension
def analyze_readings(data, thresholds):
    # Extract high-score entries
    high_impact = [e for e in data if e['score'] >= thresholds['elevated']]
    
    # Compute diagnostic level using complex conditions
    base_level = 0
    for record in high_impact:
        if record['humid'] > 52:
            base_level += record['score'] // 10
        elif record['press'] < 1010:
            base_level += 5
        else:
            base_level += 2
    
    # Apply non-linear adjustment
    adjusted_level = int(math.sqrt(base_level ** 2 + 16))
    
    # Final computation with tuple unpacking distraction
    modifiers = (3, -1, 2)
    m1, m2, m3 = modifiers
    final_value = adjusted_level * m1 + m2
    
    # Critical override based on specific pattern match
    pattern_match = any(
        data[i]['temp'] < data[i+1]['temp'] and 
        data[i+1]['score'] > data[i]['score']
        for i in range(len(data)-1)
    )
    
    if pattern_match:
        final_value += m3 * 4
    else:
        final_value -= 10  # Dead branch due to data
    
    # Additional distractor: unused sorting
    sorted_by_score = sorted(data, key=lambda x: x['score'], reverse=True)
    top_entries = sorted_by_score[:3]
    
    # The real answer computation
    checksum = 0
    for item in top_entries:
        checksum ^= item['score']  # Bitwise accumulation
    
    final_diagnostic = final_value + (checksum % 7)
    return final_diagnostic

# Execute main analysis
final_diagnostic = analyze_readings(processed_data, threshold_map)
print(f"Result: {final_diagnostic}")