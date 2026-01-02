def transform_sequence(seq, factor):
    """Irrelevant transformation function (dead code path)"""
    return [x * factor + 2 for x in seq if x % 3 != 0]


def evaluate_stability(risk_matrix):
    """Unused risk evaluation (distractor)"""
    total_risk = 0
    for row in risk_matrix:
        for val in row:
            if val > 5:
                total_risk += val ** 0.5
    return total_risk

# Simulated sensor data from environmental monitoring stations
raw_readings = {
    'station_alpha': [14, 17, 23, 19, 42, 8],
    'station_beta': [11, 20, 18, 25, 41, 13],
    'station_gamma': [9, 16, 22, 24, 38, 7]
}

# Irrelevant metadata (distractor)
station_locations = {
    'station_alpha': {'lat': 40.7128, 'lon': -74.0060, 'elevation': 12},
    'station_beta': {'lat': 34.0522, 'lon': -118.2437, 'elevation': 78},
    'station_gamma': {'lat': 41.8781, 'lon': -87.6298, 'elevation': 189}
}

# Threshold configurations for anomaly detection (partially relevant)
threshold_map = {
    'normal': 15,
    'caution': 25,
    'warning': 35
}

# Noise filter settings (mostly irrelevant)
filter_config = {
    'window_size': 3,
    'smoothing_factor': 0.85,
    'max_noise_floor': 5
}

# Intermediate processing: extract and flatten readings above baseline
processed_data = []
duplicate_tracker = set()
for station, readings in raw_readings.items():
    for value in readings:
        if value > 10:
            # Apply conditional scaling based on magnitude
            if value < threshold_map['caution']:
                processed_data.append(value * 1.1)
            elif value < threshold_map['warning']:
                processed_data.append(value * 1.25)
            else:
                processed_data.append(value * 1.4)
        
        # Track duplicates (used later)
        if value in duplicate_tracker:
            pass  # Just observing
        else:
            duplicate_tracker.add(value)

# Secondary transformation: normalize around median (distractor computation)
if len(processed_data) > 0:
    sorted_vals = sorted(processed_data)
    mid = len(sorted_vals) // 2
    median_val = (sorted_vals[mid] + sorted_vals[~mid]) / 2
    normalized = [x / median_val for x in sorted_vals]

# Simulate diagnostic rules engine
rule_weights = {
    'exceedance_count': 1.8,
    'high_magnitude_penalty': 2.3,
    'trend_breach': 1.5
}

# Unused rule components (red herring)
device_logs = [
    {'event': 'reboot', 'code': 101},
    {'event': 'calibration', 'code': 205},
    {'event': 'timeout', 'code': 301}
]

# Core analysis function
def analyze_readings(data, thresholds):
    count_normal = 0
    count_caution = 0
    count_warning = 0
    
    for val in data:
        orig_int = int(val // 1)  # Reverse mapping attempt
        if val >= thresholds['warning'] * 1.2:
            count_warning += 1
        elif val >= thresholds['caution'] * 1.1:
            count_caution += 1
        else:
            count_normal += 1
    
    # Compute diagnostic score
    base_score = 100
    base_score -= count_caution * rule_weights['exceedance_count']
    base_score -= count_warning * rule_weights['high_magnitude_penalty']
    
    # Additional penalty if high values are clustered
    sorted_data = sorted(data)
    cluster_penalty = 0
    for i in range(1, len(sorted_data)):
        if sorted_data[i] - sorted_data[i-1] < 2 and sorted_data[i] > thresholds['warning'] * 1.1:
            cluster_penalty += 0.7
    
    final_score = base_score - cluster_penalty * rule_weights['trend_breach']
    
    # Final adjustment based on integer composition
    digit_sum = 0
    temp = abs(int(final_score))
    while temp:
        digit_sum += temp % 10
        temp //= 10
    
    return final_score - digit_sum

# Execute critical statement
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Print result for extraction
print(f"Result: {final_diagnostic}")