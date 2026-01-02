import math

# Simulated sensor fusion system for environmental monitoring

def collect_sensor_data():
    raw_streams = {
        'thermal': [23.4, 24.1, 19.8, 25.6, 26.7, 18.2, 27.3],
        'humidity': [45, 47, 50, 44, 60, 62, 43],
        'pressure': [1013, 1015, 1012, 1010, 1008, 1016, 1014],
        'co2': [420, 435, 450, 415, 500, 510, 400]
    }
    return raw_streams

# Irrelevant preprocessing path (dead code path)
def legacy_normalization(data):
    scale_factor = 0.95
    adjusted = []
    for val in data:
        adjusted.append(round(val * scale_factor, 2))
    return adjusted  # Never used in main flow

# Decoy function with misleading name
def validate_integrity(x):
    if isinstance(x, list):
        checksum = sum([hash(str(v)) % 1000 for v in x])
        return checksum > 500
    return False

# Real processing begins here
def filter_anomalies(sensor_data):
    filtered_cluster = {}
    
    # Extract and slice relevant windows
    thermal_window = sensor_data['thermal'][1:6]  # Focus on central readings
    humidity_set = set(sensor_data['humidity'])
    co2_values = sensor_data['co2']
    
    # Compute moving average for thermal (distractor)
    ma_temp = sum(thermal_window) / len(thermal_window)
    
    # Identify outliers using IQR method on CO2
    sorted_co2 = sorted(co2_values)
    q1 = sorted_co2[1]
    q3 = sorted_co2[5]
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    # Filter anomalies
    filtered_co2 = [x for x in co2_values if lower_bound <= x <= upper_bound]
    filtered_cluster['co2_filtered'] = filtered_co2
    
    # Humidity clustering via set operations (actual use)
    ideal_humidity_range = set(range(44, 48))
    common_levels = ideal_humidity_range.intersection(humidity_set)
    stability_score = len(common_levels)
    
    filtered_cluster['stability_index'] = stability_score
    
    # Pressure trend analysis (irrelevant)
    pressure_trend = []
    for i in range(1, len(sensor_data['pressure'])):
        pressure_trend.append(sensor_data['pressure'][i] - sensor_data['pressure'][i-1])
    avg_trend = sum(pressure_trend) / len(pressure_trend)
    
    # Dummy correction factor (never used)
    correction_map = {i: round(math.sin(i * 0.1), 2) for i in range(10)}
    
    return filtered_cluster

# Core analysis engine
def analyze_readings(diagnostic_frame):
    # Unpack results
    co2_clean = diagnostic_frame['co2_filtered']
    stability_metric = diagnostic_frame['stability_index']
    
    # Calculate emission rate from clean CO2 samples
    base_rate = sum(co2_clean) / len(co2_clean)
    
    # Apply conditional scaling based on stability
    if stability_metric >= 3:
        adjustment_factor = 0.85
    else:
        adjustment_factor = 1.15
    
    adjusted_rate = base_rate * adjustment_factor
    
    # Secondary validation using bit manipulation (red herring)
    binary_flag = 0
    for val in co2_clean:
        binary_flag ^= int(val) & 0xF  # XOR last 4 bits
    
    # Diagnostic health check (distractor)
    health_registry = []
    for i, v in enumerate(co2_clean):
        health_registry.append((i ^ int(v)) % 7)
    
    # Final computation chain
    decay_constant = 0.92
    sample_count_weight = len(co2_clean) ** 0.5
    
    intermediate = adjusted_rate * sample_count_weight
    final_diagnostic = round(intermediate * decay_constant, 4)
    
    # Unused complex structure (dead code)
    report_card = {
        'raw_flag': binary_flag,
        'health_vector': health_registry,
        'trend_bias': avg_trend if 'avg_trend' in locals() else 0,
        'legacy_norm': legacy_normalization([1,2,3])
    }
    
    return final_diagnostic

# Main execution pipeline
if __name__ == '__main__':
    # Initial data ingestion
    all_sensors = collect_sensor_data()
    
    # Phantom calibration sequence (misleading)
    calibration_matrix = [[i*j for j in range(3)] for i in range(3)]
    calibration_sum = sum([sum(row) for row in calibration_matrix])
    
    # Critical processing path
    processed_diagnostics = filter_anomalies(all_sensors)
    final_diagnostic = analyze_readings(processed_diagnostics)
    
    # Output target result
    print(f"Result: {final_diagnostic}")