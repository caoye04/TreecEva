import math

# Simulated sensor data from a distributed environmental monitoring system
temperature_readings = [23.5, 24.1, 22.8, 25.6, 26.7, 24.3, 23.9, 25.1]
humidity_readings = [45, 48, 50, 55, 60, 53, 49, 51]
pressure_readings = [1013, 1015, 1012, 1010, 1008, 1009, 1011, 1014]

# Irrelevant calibration constants (distractor)
CALIBRATION_OFFSET_A = 0.037
CALIBRATION_OFFSET_B = -0.012
REFERENCE_VOLTAGE = 5.0

# Misleading preprocessing step with dead-end computation
def preprocess_sensors(raw_temps, raw_humid):
    normalized = []
    for t in raw_temps:
        # Complex but irrelevant normalization
        adj_temp = (t - 20) * (1 + CALIBRATION_OFFSET_A) + CALIBRATION_OFFSET_B
        normalized.append(round(adj_temp, 2))
    
    # Dead code path: unused transformation
    if len(raw_humid) > 5:
        _ = [math.log(h + 1) for h in raw_humid if h > 0]  # Not used
    
    return normalized

# Unused function that looks important (decoy)
def compute_stability_index(data_stream):
    variance = sum([(x - sum(data_stream)/len(data_stream))**2 for x in data_stream]) / len(data_stream)
    return math.exp(-variance)

# Another red herring: energy consumption estimator (never used)
def estimate_power_usage(sensors_active, duration_hours):
    base = 0.5
    per_sensor = 0.15
    return base + sensors_active * per_sensor * duration_hours

# Core processing with relevant logic buried in distractions
def filter_outliers(values, threshold=1.5):
    mean_val = sum(values) / len(values)
    std_dev = (sum((x - mean_val) ** 2 for x in values) / len(values)) ** 0.5
    return [v for v in values if abs(v - mean_val) <= threshold * std_dev]

# Intermediate transformation with multiple steps and noise
def extract_trend_components(filtered_temps, humidity_levels):
    trend_data = {}
    
    # Real computation: temperature slope approximation
    n = len(filtered_temps)
    sum_i, sum_t = 0, 0
    for i in range(n):
        sum_i += i
        sum_t += filtered_temps[i]
    
    sum_it = sum(i * filtered_temps[i] for i in range(n))
    sum_i2 = sum(i * i for i in range(n))
    
    slope = (n * sum_it - sum_i * sum_t) / (n * sum_i2 - sum_i * sum_i) if (n * sum_i2 - sum_i * sum_i) != 0 else 0
    
    trend_data['temp_slope'] = round(slope, 3)
    
    # Distractor: complex humidity clustering (unused result)
    clusters = {}
    for h in humidity_levels:
        key = h // 5
        clusters[key] = clusters.get(key, 0) + 1
    trend_data['humidity_distribution'] = clusters  # Stored but not used later
    
    return trend_data

# Data fusion with dictionary operations and list comprehensions
def integrate_multi_source(temp_proc, hum_proc, press_proc):
    fused = {
        'metrics': [],
        'flags': {},
        'timestamp_offset': 0.0
    }
    
    # Real operation: composite index calculation
    avg_temp = sum(temp_proc) / len(temp_proc)
    avg_hum = sum(hum_proc) / len(hum_proc)
    avg_press = sum(press_proc) / len(press_proc)
    
    # Key intermediate value
    thermal_humidity_index = avg_temp * (1 + avg_hum / 100)
    
    # List comprehension to generate diagnostic codes (some irrelevant)
    codes = [f'D{int(avg_temp)}', f'H{int(avg_hum)}', f'P{avg_press:.0f}']
    priority_codes = [c for c in codes if c.startswith('D') or c.startswith('H')]
    
    fused['metrics'].append(thermal_humidity_index)
    fused['flags']['codes'] = priority_codes
    fused['timestamp_offset'] = math.sin(math.pi / 4)  # Constant distraction
    
    # Dead assignment
    fused['aux'] = {'version': 'legacy', 'active': False}
    
    return fused

# Final analysis with conditional branching and critical logic
processed_temps = preprocess_sensors(temperature_readings, humidity_readings)
clean_temps = filter_outliers(processed_temps)
humidity_subset = [h for h in humidity_readings if h >= 48]  # Conditional filtering

components = extract_trend_components(clean_temps, humidity_subset)
fused_system = integrate_multi_source(clean_temps, humidity_subset, pressure_readings)

# Critical execution point
final_diagnostic = 0

if components['temp_slope'] > 0.1:
    base_score = fused_system['metrics'][0] * 1.2
    
    # Additional logic gate
    if len(fused_system['flags']['codes']) >= 2:
        adjustment = math.sqrt(abs(components['temp_slope'])) * 10
        final_diagnostic = base_score + adjustment
    else:
        final_diagnostic = base_score - 5
else:
    final_diagnostic = 100  # Fallback path (not taken)

# Print final result as required
print(f"Result: {final_diagnostic}")