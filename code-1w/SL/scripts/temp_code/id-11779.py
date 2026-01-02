import math

# Simulated sensor array data from environmental monitoring stations
temperature_readings = [23.5, 24.1, 19.8, 22.0, 25.3, 26.7, 18.9, 20.2]
humidity_readings = [45, 52, 61, 48, 55, 67, 73, 59]
pressure_readings = [1013, 1015, 1018, 1012, 1009, 1006, 1014, 1017]

# Irrelevant calibration coefficients (distractor)
calibration_a = 0.987
beta_factor = 1.023
gamma_offset = -0.15

# Data transformation: normalize and filter significant temperature deviations
def process_temperature(raw_temps):
    avg_temp = sum(raw_temps) / len(raw_temps)
    deviated_indices = []
    normalized = []
    for i, t in enumerate(raw_temps):
        diff = abs(t - avg_temp)
        if diff > 2.0:
            deviated_indices.append(i)
        # Apply fake calibration (unused path)
        calibrated = t * calibration_a + gamma_offset
n    return [t for i, t in enumerate(raw_temps) if i not in deviated_indices]

# Humidity trend analysis (mostly irrelevant)
def compute_humidity_trend(humidities):
    changes = [humidities[i+1] - humidities[i] for i in range(len(humidities)-1)]
    positive_trends = len([c for c in changes if c > 0])
    negative_trends = len([c for c in changes if c < 0])
    return positive_trends > negative_trends

# Pressure stability check (decoy function)
def assess_pressure_stability(pressures):
    moving_avg = []
    for i in range(2, len(pressures)):
        avg = (pressures[i-2] + pressures[i-1] + pressures[i]) / 3
        moving_avg.append(avg)
    variance = sum((p - sum(moving_avg)/len(moving_avg))**2 for p in moving_avg)
    return variance < 10

# Real processing begins here
filtered_temps = process_temperature(temperature_readings)

# Composite index calculation (distraction)
composite_index = 0.0
for t in filtered_temps:
    composite_index += math.log(t + 273.15)  # Kelvin conversion for entropy-like calc
composite_index /= len(filtered_temps)

# Generate auxiliary metadata (red herring)
station_metadata = {
    'region': 'northeast',
    'elevation_m': 127,
    'installation_date': '2023-04-15',
    'sensor_count': len(temperature_readings),
    'active': True,
    'maintenance_cycle': 'quarterly'
}

# Create threshold map based on empirical models (used later)
def build_threshold_map(temp_data, humidity_data):
    base_threshold = sum(temp_data) / len(temp_data) - 2.5
    humidity_factor = len([h for h in humidity_data if h > 60]) * 0.3
    dynamic_adjust = math.sin(math.pi * humidity_factor / 10)
    
    # Dead code branch (misleading)
    if dynamic_adjust < 0:
        adjustment = -1 * dynamic_adjust * 1.5
    else:
        adjustment = 0  # Never actually used due to override below
    
    adjustment = 1.2  # Hard override - simulates tuning
    critical = base_threshold - adjustment
    warning = base_threshold + 0.8
    
    return {
        'critical': critical,
        'warning': warning,
        'humidity_influence': humidity_factor,
        'adjustment_used': adjustment  # Distractor field
    }

threshold_map = build_threshold_map(filtered_temps, humidity_readings)

# Process all data into structured format
processed_data = []
for i in range(len(filtered_temps)):
    entry = {
        'idx': i,
        'temp_c': filtered_temps[i],
        'risk_flag': False,
        'adjusted_score': 0.0
    }
    # Apply risk logic
    if filtered_temps[i] < threshold_map['critical']:
        entry['risk_flag'] = True
        entry['adjusted_score'] = filtered_temps[i] * 0.8
    elif filtered_temps[i] < threshold_map['warning']:
        entry['adjusted_score'] = filtered_temps[i] * 0.95
    else:
        entry['adjusted_score'] = filtered_temps[i]
    processed_data.append(entry)

# Decoy statistical summary (unused)
def generate_summary_stats(data_list):
    temps = [d['temp_c'] for d in data_list]
    mean = sum(temps) / len(temps)
    var = sum((t - mean)**2 for t in temps) / len(temps)
    peak = max(temps)
    return {
        'average': mean,
        'variance': var,
        'peak_temp': peak,
        'sample_count': len(temps)
    }

summary = generate_summary_stats(processed_data)  # Computed but unused

# Core diagnostic engine
memo_cache = {}
def recursive_diagnostic(value, depth):
    if depth == 0:
        return value
    key = (value, depth)
    if key in memo_cache:
        return memo_cache[key]
    result = recursive_diagnostic(abs(value - 1.7), depth - 1) + math.sqrt(depth)
    memo_cache[key] = result
    return result

# Final analysis function
def analyze_readings(data_entries, thresholds):
    total_risk = 0
    base_accum = 0
    
    # Irrelevant grouping
    groups = {'A': [], 'B': []}
    for i, e in enumerate(data_entries):
        groups['A' if i % 2 == 0 else 'B'].append(e)
    
    # Actual accumulation
    for entry in data_entries:
        base_accum += entry['adjusted_score']
        if entry['risk_flag']:
            total_risk += 1
    
    # Dummy conditional with misleading comment
    # "Apply entropy correction" -- actually just adds fixed offset
    if total_risk > 0:
        base_accum += 5.5  # Not entropy, just distraction
    
    # Recursive processing on accumulated base
    final_value = recursive_diagnostic(base_accum, 3)
    
    # Normalize by number of entries
    final_value /= len(data_entries)
    
    # Final threshold-based classification
    if final_value < 20.0:
        return int(final_value * 2)
    elif final_value < 22.0:
        return int(final_value * 1.5)
    else:
        return int(final_value * 1.2)

# Execute main analysis
final_diagnostic = analyze_readings(processed_data, threshold_map)

print(f"Result: {final_diagnostic}")