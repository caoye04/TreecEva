import math

# Simulated environmental sensor network data processing
def collect_readings():
    raw_readings = [23.4, 19.1, 25.6, 21.8, 18.9, 24.2, 20.5, 22.7]
    calibration_offset = 1.2
    adjusted = [r + calibration_offset for r in raw_readings]
    outliers = [x for x in adjusted if x > 26]  # None expected
    filtered = [x for x in adjusted if x <= 26]
    return filtered

# Irrelevant auxiliary function (decoy)
def compute_wind_chill(temps):
    wc_values = []
    for t in temps:
        chill = 13.12 + 0.6215*t - 11.37*(3**0.16) + 0.3965*t*(3**0.16)
        wc_values.append(round(chill, 2))
    return wc_values  # Never used

# Secondary transformation with red herring variables
def enhance_resolution(data):
    high_res = []
    noise_floor = 0.05
    for val in data:
        for _ in range(3):
            val += noise_floor
        high_res.append(round(val, 1))
    # Fake aggregation path
    peak = max(high_res)
    floor = min(high_res)
    span = peak - floor
    threshold_marker = 25.0  # Distractor
    return high_res

# Data normalization (partially relevant)
def normalize(values):
    mean_val = sum(values) / len(values)
    std_dev = (sum((x - mean_val) ** 2 for x in values) / len(values)) ** 0.5
    normalized = [(x - mean_val) / std_dev for x in values]
    return normalized, mean_val, std_dev  # Extra returns not fully used

# Core analysis logic
measure_log = []
def record_measurement(value, tag=''):
    entry = {'value': round(value, 2), 'tag': tag}
    measure_log.append(entry)
    return value

def analyze_readings(dataset):
    # Critical path begins
    base_set = [record_measurement(x, 'raw') for x in dataset]
    
    # Compute diagnostic metrics
    avg = sum(base_set) / len(base_set)
    variance = sum((x - avg)**2 for x in base_set) / len(base_set)
    stability_index = math.sqrt(variance)
    
    # Threshold checks with misleading branching
    critical_limit = 2.0
    warning_limit = 1.0
    status_flag = 0
    if stability_index > critical_limit:
        status_flag = -1
    elif stability_index > warning_limit:
        status_flag = 0  # Misleading: appears active but overridden
    else:
        status_flag = 1
    
    # Complex conditional with list comprehension side-effect
    adjustments = []
    for i, val in enumerate(base_set):
        if i % 2 == 0:
            adjustments.append(math.sin(val * 0.1))
        else:
            adjustments.append(math.cos(val * 0.1))
    
    net_drift = sum(adjustments)
    
    # Final computation chain
    significance_score = abs(avg * stability_index)
    penalty_factor = 0.95 if net_drift < 0 else 1.0
    
    # Key assignment - target of query
    final_diagnostic = significance_score * penalty_factor * status_flag
    
    # Dead code path (never executed)
    if False:
        backup_system = {'active': False, 'score': final_diagnostic * 0.8}
        return backup_system['score']
    
    return final_diagnostic

# Orchestration with decoy variables
if __name__ == '__main__':
    # Irrelevant initialization
    system_health = {'initialized': True, 'sensors': 8, 'version': '2.1'}
    debug_mode = False
    log_archive = []
    
    # Real execution flow
    raw_data = collect_readings()
    enhanced_data = enhance_resolution(raw_data)
    normalized_data, _, _ = normalize(enhanced_data)
    processed_data = [round(x, 2) for x in normalized_data]
    
    # Introduce misleading intermediate
    temp_analysis = sum(processed_data) / len(processed_data) * 0.75  # Unused
    
    # Execute key statement
    final_diagnostic = analyze_readings(processed_data)
    
    # Print required result
    print(f"Result: {final_diagnostic}")