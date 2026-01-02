import math

# Simulated sensor data from environmental monitoring stations
temperature_readings = [23.5, 24.1, 19.8, 22.0, 25.3, 26.7, 20.4, 21.9, 24.8, 23.0]
humidity_readings = [45, 48, 52, 58, 43, 39, 60, 55, 47, 50]
pressure_readings = [1013, 1015, 1012, 1018, 1009, 1020, 1014, 1016, 1011, 1017]

# Irrelevant auxiliary data (distractor)
sound_levels = [65, 70, 60, 80, 75, 68, 72, 69, 74, 71]
luminosity_values = [800, 900, 850, 950, 1000, 870, 930, 880, 910, 860]

# Preprocessing: normalize and filter relevant sensor data
def normalize(data):
    mean_val = sum(data) / len(data)
    return [round(x - mean_val, 2) for x in data]

def filter_outliers(data, threshold=2.0):
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    return [x for x in data if abs(x - mean_val) / std_dev <= threshold]

# Misleading function that looks important but is unused (dead code path)
def compute_air_quality_index(temp, hum, press):
    return int((temp * 1.5) + (hum * 0.8) + (press * 0.01))

# Another decoy function with plausible logic
def calculate_stability_score(readings):
    diffs = [abs(readings[i] - readings[i-1]) for i in range(1, len(readings))]
    return round(sum(diffs) / len(diffs), 2)

# Signal processing simulation (irrelevant but adds complexity)
def apply_fourier_transform(signal):
    N = len(signal)
    transformed = []
    for k in range(N // 2):
        real = sum(signal[n] * math.cos(2 * math.pi * k * n / N) for n in range(N))
        imag = sum(-signal[n] * math.sin(2 * math.pi * k * n / N) for n in range(N))
        magnitude = (real**2 + imag**2)**0.5
        transformed.append(round(magnitude, 2))
    return transformed[:5]  # Return only first few coefficients

# Real preprocessing pipeline
normalized_temp = normalize(temperature_readings)
filtered_humidity = filter_outliers(humidity_readings, threshold=1.8)
processed_pressure = [p / 100 for p in pressure_readings]  # Convert to kPa

# Composite data structure with slicing and tuple unpacking
all_sensors = list(zip(normalized_temp, filtered_humidity, processed_pressure))
recent_batch = all_sensors[-7:]  # Use only recent entries
historical_slice = all_sensors[1::2]  # Every other reading (unused distractor)

# Set operations on derived categories (python-specific feature)
stable_temps = {t for t in normalized_temp if abs(t) <= 1.5}
extreme_humidity = {h for h in filtered_humidity if h > 50}
common_conditions = stable_temps & extreme_humidity  # Empty set, misleading

# Threshold logic with conditional expressions
base_threshold = 24.5
adjusted_threshold = base_threshold - 1.2 if len(stable_temps) > 3 else base_threshold + 0.5

# More irrelevant computations
fft_results = apply_fourier_transform(temperature_readings)
stability_metric = calculate_stability_score(pressure_readings)
synthetic_index = sum(fft_results) * 10 // (len(fft_results) or 1)

# Core analysis logic
threshold_set = {
    'temp': adjusted_threshold,
    'humidity_range': (40, 60),
    'critical_pressure': 10.15
}

# Data transformation with nested logic
processed_data = []
for temp_offset, humidity_val, pressure_kpa in recent_batch:
    # Derived flag using conditional expression
    status_flag = 'HIGH' if humidity_val > 55 else 'NORMAL'
    
    # Composite score calculation (only some components matter)
    temp_score = abs(temp_offset) * 1.2
    humidity_penalty = (humidity_val - 50) * 0.3 if humidity_val > 50 else 0
    pressure_deviation = abs(pressure_kpa - 10.14)
    
    # Actual relevant computation
    diagnostic_weight = temp_score + humidity_penalty + (pressure_deviation * 50)
    
    # Tuple packing with extra fields (some irrelevant)
    entry = (
        temp_offset,
        humidity_val,
        pressure_kpa,
        diagnostic_weight,
        status_flag,
        f"D-{len(processed_data)}"
    )
    processed_data.append(entry)
    
    # Early termination condition (rarely triggered, not hit here)
    if pressure_deviation > 0.05 and humidity_val < 40:
        break

# Final analysis function
def analyze_readings(data_entries, thresholds):
    total_risk = 0.0
    critical_count = 0
    
    for entry in data_entries:
        temp_adj, humid, press, weight, flag, _ = entry  # Unpacking
        
        # Key decision logic
        if press > thresholds['critical_pressure']:
            adjustment_factor = 1.8
        elif humid < thresholds['humidity_range'][0]:
            adjustment_factor = 1.4
        else:
            adjustment_factor = 1.0
        
        # Only entries with normal temperature deviation contribute
        if abs(temp_adj) <= 1.0:
            total_risk += weight * adjustment_factor
            
        # Dead branch - never taken due to data properties
        if temp_adj < -5.0:  # Impossible in this dataset
            critical_count += 1
    
    # Final computation
    if critical_count > 0:
        return int(total_risk * 2)
    else:
        return int(total_risk + 0.5)  # Round to nearest integer

# Execute main analysis
final_diagnostic = analyze_readings(processed_data, threshold_set)

# Print result as required
print(f"Result: {final_diagnostic}")