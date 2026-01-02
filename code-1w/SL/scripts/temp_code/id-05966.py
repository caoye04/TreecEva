import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 25.3, 22.8, 26.0, 24.7, 23.9, 25.1, 24.4, 23.7]
humidity_readings = [45, 47, 50, 52, 48, 55, 51, 49, 53, 46]
pressure_readings = [1013, 1015, 1012, 1016, 1014, 1011, 1017, 1013, 1015, 1010]

# Irrelevant calibration coefficients (distractor)
calibration_a = 0.987
salinity_offset = 3.14159
elevation_factor = 1.015
baseline_correction = [0.1, -0.2, 0.05, 0.15, -0.1]

# Preprocessing: Normalize temperature readings
def normalize_temperatures(raw_temps):
    mean_temp = sum(raw_temps) / len(raw_temps)
    normalized = [(t - mean_temp) * 1.05 for t in raw_temps]
    return normalized

# Redundant humidity adjustment function (unused path)
def adjust_humidity(humidities, factor=1.02):
    adjusted = [h * factor for h in humidities]
    return [min(h, 100) for h in adjusted]

# Complex data transformation with conditional logic
def process_sensor_data(temps, humids, pressures):
    processed = []
    for i in range(len(temps)):
        # Composite index calculation (partially relevant)
        temp_weight = temps[i] * 0.6
        pressure_weight = (1015 - pressures[i]) * 0.1  # deviation from standard
        humidity_ratio = humids[i] / 100
        
        # Apply non-linear transformation
        if temp_weight > 14.5:
            impact_factor = math.log(temp_weight) * (1 + humidity_ratio)
        else:
            impact_factor = temp_weight * (0.8 + humidity_ratio * 0.5)
        
        # Conditional override based on pressure anomaly
        pressure_diff = abs(pressures[i] - 1013)
        if pressure_diff > 3:
            impact_factor *= 0.9  # slight dampening
        
        processed.append(round(impact_factor, 4))
    
    # Inject dummy entries (distractor)
    processed.append(0.0)  # placeholder
    processed.append(-1.0)  # invalid reading marker
    
    return processed

# Advanced analysis function with multiple concepts
def analyze_readings(data_stream, cutoff):
    # Filter out dummy values
    filtered = [x for x in data_stream if x >= 0]
    
    # Compute moving average over window of 3 (relevant)
    if len(filtered) < 3:
        return 0
    
    moving_averages = []
    for i in range(len(filtered) - 2):
        avg = (filtered[i] + filtered[i+1] + filtered[i+2]) / 3
        moving_averages.append(avg)
    
    # Identify peaks above threshold
    significant_peaks = [m for m in moving_averages if m > cutoff]
    
    # Calculate peak density (peaks per unit length)
    peak_density = len(significant_peaks) / len(moving_averages) if moving_averages else 0
    
    # Determine stability score using min/max spread
    if significant_peaks:
        max_peak = max(significant_peaks)
        min_peak = min(significant_peaks)
        spread = max_peak - min_peak
        stability_score = 1 / (1 + spread) if spread > 0 else 1.0
    else:
        stability_score = 0.5
    
    # Final diagnostic computation combining multiple factors
    # This includes a hidden bit manipulation check for even count
    peak_count = len(significant_peaks)
    parity_adjustment = 1.05 if (peak_count & 1) == 0 else 0.95  # XOR-like logic
    
    # Composite diagnostic formula
    diagnostic_value = (peak_density * 100) * stability_score * parity_adjustment
    
    # Dead code branch - never executed due to logic (red herring)
    extreme_flag = False
    if diagnostic_value > 100:
        scaling_factor = 0.75
        diagnostic_value *= scaling_factor
        extreme_flag = True  # unreachable in this dataset
    
    # Final rounding and clamping
    result = round(diagnostic_value, 4)
    return result

# Unused auxiliary function (decoy)
def calculate_entropy(data):
    total = sum(data)
    if total == 0:
        return 0
    probabilities = [x / total for x in data]
    entropy = -sum(p * math.log(p) for p in probabilities if p > 0)
    return entropy

# Main execution flow
normalized_temps = normalize_temperatures(temperature_readings)
processed_data = process_sensor_data(normalized_temps, humidity_readings, pressure_readings)
threshold = 1.85

# Critical statement
final_diagnostic = analyze_readings(processed_data, threshold)

# Print final result as required
print(f"Target result: {final_diagnostic}")