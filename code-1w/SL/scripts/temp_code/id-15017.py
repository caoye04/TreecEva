from collections import defaultdict, Counter

# Simulated sensor network data processing with diagnostic analysis
def collect_sensor_data():
    raw_data = [
        ('temp', 23.5), ('pressure', 101.3), ('temp', 24.1), ('humidity', 45.2),
        ('pressure', 102.0), ('temp', 19.8), ('humidity', 50.1), ('temp', 25.3),
        ('pressure', 99.7), ('humidity', 55.6), ('temp', 22.8), ('pressure', 100.8)
    ]
    data_map = defaultdict(list)
    for sensor_type, value in raw_data:
        data_map[sensor_type].append(value)
    return data_map

# Irrelevant transformation - red herring
def transform_coordinates(coords):
    x, y = coords
    transformed = (x * 0.9 + 5, y * 1.1 - 3)
    magnitude = (transformed[0]**2 + transformed[1]**2)**0.5
    normalized = (transformed[0] / magnitude, transformed[1] / magnitude)
    return normalized

# Unused function - dead code path
def deprecated_filter(data_list, limit):
    result = []
    for item in data_list:
        if item > limit:
            result.append(item * 0.75)
    return result

# Auxiliary statistical function
def moving_average(values, window_size=3):
    if len(values) < window_size:
        return [sum(values)/len(values)]
    averages = []
    for i in range(len(values) - window_size + 1):
        averages.append(sum(values[i:i+window_size]) / window_size)
    return averages

# Data cleansing with distractor logic
def preprocess_readings(raw_map):
    cleaned = {}
    stats_summary = {}  # Distractor: collected but not used directly
    
    for sensor, readings in raw_map.items():
        # Real processing
        sorted_vals = sorted(readings)
        midpoint = len(sorted_vals) // 2
        median_val = (sorted_vals[midpoint] + sorted_vals[-(midpoint+1)]) / 2
        
        # Compute quartiles - partially relevant
        q1 = sorted_vals[len(sorted_vals)//4]
        q3 = sorted_vals[3*len(sorted_vals)//4]
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        
        # Filter outliers
        filtered = [v for v in readings if lower_bound <= v <= upper_bound]
        cleaned[sensor] = filtered
        
        # Distractor computation
        squared_diffs = [(v - median_val)**2 for v in filtered]
        variance = sum(squared_diffs) / len(squared_diffs) if squared_diffs else 0
        stats_summary[sensor] = {
            'median': median_val,
            'variance': variance,
            'iqr': iqr,
            'outliers_removed': len(readings) - len(filtered)
        }
    
    # Dead assignment - misleading
    stats_summary['aggregates'] = {
        'total_sensors': len(cleaned),
        'overall_mean': sum(sum(v) for v in cleaned.values()) / sum(len(v) for v in cleaned.values())
    }
    
    return cleaned

# Threshold configuration - actually used
def generate_thresholds(sensor_types):
    base_config = {'temp': 24.0, 'pressure': 101.0, 'humidity': 50.0}
    safety_margin = {'temp': 2.0, 'pressure': 3.0, 'humidity': 8.0}
    thresholds = defaultdict(dict)
    for st in sensor_types:
        if st in base_config:
            thresholds[st]['warning'] = base_config[st] + safety_margin[st]
            thresholds[st]['critical'] = base_config[st] + 2 * safety_margin[st]
            # Decoy values
            thresholds[st]['deprecated_min'] = base_config[st] - safety_margin[st]
    return dict(thresholds)

# Core analysis function
def analyze_readings(data_dict, thresholds):
    diagnostic_code = 0
    severity_weights = {'temp': 3, 'pressure': 2, 'humidity': 1}
    
    for sensor_type, values in data_dict.items():
        if sensor_type not in thresholds:
            continue
        
        high_threshold = thresholds[sensor_type]['warning']
        extreme_threshold = thresholds[sensor_type]['critical']
        
        # Count high readings
        high_count = sum(1 for v in values if v > high_threshold)
        extreme_count = sum(1 for v in values if v > extreme_threshold)
        
        # Irrelevant normalization
        total_observations = len(values)
        if total_observations == 0:
            continue
            
        high_ratio = high_count / total_observations
        extreme_ratio = extreme_count / total_observations
        
        # Real impact on result
        if high_ratio > 0.4:
            diagnostic_code += severity_weights[sensor_type] * 10
        if extreme_ratio > 0.2:
            diagnostic_code += severity_weights[sensor_type] * 25
        
        # Distractor block: complex but unused calculation
        if high_ratio > 0.1:
            expected_fluctuation = 0.15 * total_observations
            deviation_score = abs(high_count - expected_fluctuation)
            normalized_score = deviation_score / (total_observations * 0.5)
            # Not used anywhere

    # Final computation with decoy intermediate steps
    temp_data = data_dict.get('temp', [])
    if temp_data:
        temp_avg = sum(temp_data) / len(temp_data)
        # This adjustment is actually critical
        adjustment_factor = int(abs(temp_avg - 24.0) * 2)
        diagnostic_code += adjustment_factor * 3
    
    # Dead logic branch
    pressure_data = data_dict.get('pressure', [])
    if pressure_data and len(pressure_data) % 2 == 0:
        sorted_p = sorted(pressure_data)
        median_p = (sorted_p[len(sorted_p)//2] + sorted_p[-(len(sorted_p)//2 + 1)]) / 2
        if median_p < 100.0:
            # This would add 15, but condition is not met
            diagnostic_code += 15
    
    # Critical statement
    final_diagnostic = diagnostic_code * 2 + 10
    
    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Execution flow
if __name__ == "__main__":
    # Collect raw data
    raw_sensor_data = collect_sensor_data()
    
    # Preprocess - filter outliers
    filtered_data = preprocess_readings(raw_sensor_data)
    
    # Generate detection thresholds
    threshold_map = generate_thresholds(filtered_data.keys())
    
    # Perform diagnostic analysis
    final_diagnostic = analyze_readings(filtered_data, threshold_map)