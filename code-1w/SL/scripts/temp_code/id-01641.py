import math

# Simulated sensor data processing system for environmental monitoring
raw_readings = [14.2, 18.7, 25.3, 9.8, 30.1, 28.6, 19.5, 22.4, 11.9, 16.8]

timestamps = [1623456000 + i*300 for i in range(len(raw_readings))]
location_grid = [(lat, lon) for lat in [40.5, 40.6] for lon in [-73.8, -73.7]]

# Irrelevant auxiliary mappings (distractor)
color_codes = {'low': '#00FF00', 'medium': '#FFFF00', 'high': '#FF0000'}
status_icons = ['!', '?', '*', '+']

# Data calibration constants (some are decoys)
CALIBRATION_A = 1.08
CALIBRATION_B = 0.93
CALIBRATION_C = 2.1  # Unused
BASELINE_OFFSET = -0.5

# Misleading transformation chains
adjusted_readings = []
for val in raw_readings:
    temp = val * CALIBRATION_A
    temp -= BASELINE_OFFSET
    if temp > 20:
        temp *= CALIBRATION_B
    adjusted_readings.append(round(temp, 2))

# Dead code path - never executed due to logic (red herring)
def legacy_transform(x):
    return (x ** 2) / 100 + 5

legacy_results = [legacy_transform(x) for x in adjusted_readings if x < 0]  # Always empty

# Real processing begins here
valid_readings = [x for x in adjusted_readings if 10 <= x <= 30]

# Compute rolling window averages (3-point)
rolling_averages = []
for i in range(2, len(valid_readings)):
    window_avg = sum(valid_readings[i-2:i+1]) / 3
    rolling_averages.append(round(window_avg, 2))

# Statistical summary (only some values used later)
mean_value = sum(valid_readings) / len(valid_readings)
variance = sum((x - mean_value) ** 2 for x in valid_readings) / len(valid_readings)
std_dev = math.sqrt(variance)
median_value = sorted(valid_readings)[len(valid_readings)//2]

# Decoy structure with unused computations
summary_stats = {
    'count': len(valid_readings),
    'mean': round(mean_value, 2),
    'std': round(std_dev, 2),
    'median': median_value,
    'skew': 0.0,  # Placeholder
    'kurtosis': None  # Not calculated
}

# Threshold logic setup (relevant)
thresh_a = mean_value - 0.5 * std_dev
thresh_b = mean_value + 0.3 * std_dev

threshold_map = {
    'low_risk': lambda x: x < thresh_a,
    'moderate_risk': lambda x: thresh_a <= x < thresh_b,
    'high_risk': lambda x: x >= thresh_b
}

# Aggregation engine
aggregated_data = {}
for i, val in enumerate(rolling_averages):
    category = None
    for risk_level, condition in threshold_map.items():
        if condition(val):
            category = risk_level
            break
    
    if category not in aggregated_data:
        aggregated_data[category] = []
    aggregated_data[category].append(val)

# Secondary aggregation by magnitude bands (unused distractor)
magnitude_groups = {}
for val in rolling_averages:
    band = int(val // 5) * 5
    if band not in magnitude_groups:
        magnitude_groups[band] = 0
    magnitude_groups[band] += 1

# Core diagnostic processor (key function)
def process_metrics(data_dict, thresholds):
    # Irrelevant local constants
    MAX_ITER = 100
    TOLERANCE = 1e-6
    DEBUG_MODE = False
    
    # Unused helper (decoy)
    def validate_structure(d):
        required_keys = {'low_risk', 'moderate_risk', 'high_risk'}
        return required_keys.issubset(set(d.keys()))
    
    # Actual computation
    total_points = sum(len(vals) for vals in data_dict.values())
    high_risk_count = len(data_dict.get('high_risk', []))
    moderate_risk_count = len(data_dict.get('moderate_risk', []))
    low_risk_count = len(data_dict.get('low_risk', []))
    
    # Complex weighting formula
    if total_points == 0:
        return 0
    
    weight_high = high_risk_count / total_points
    weight_moderate = moderate_risk_count / total_points
    weight_low = low_risk_count / total_points
    
    # Diagnostic score calculation
    severity_index = (weight_high * 3.0 + 
                     weight_moderate * 1.5 + 
                     weight_low * 0.5)
    
    # Normalize to 0-100 scale
    normalized_score = min(100.0, severity_index * 25.0)
    
    # Apply non-linear correction based on dominance
    if weight_high > 0.5:
        normalized_score = min(100.0, normalized_score * 1.2)
    elif weight_low > 0.7:
        normalized_score = max(10.0, normalized_score * 0.8)
    
    # Final adjustment using unused statistical moment (misleading)
    # Note: kurtosis was never computed but this line looks relevant
    final_adjustment = 1.0  # Simulates use of missing metric
    
    result = round(normalized_score * final_adjustment, 4)
    
    # Dead return path (never reached)
    if DEBUG_MODE:
        return -999.0  # Would indicate error, but debug is false
    
    return result

# Execute key statement
target_threshold = 22.5  # Unused parameter (red herring)
final_diagnostic = process_metrics(aggregated_data, threshold_map)

# Print result as required
print(f"Target result: {final_diagnostic}")