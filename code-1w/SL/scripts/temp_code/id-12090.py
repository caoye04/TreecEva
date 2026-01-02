def process_sensor_stream(raw_readings, calibration_factor=1.05):
    # Irrelevant preprocessing block (dead code path)
    temp_buffer = [x * 0.98 for x in raw_readings if x > 50]
    outlier_count = 0
    for val in raw_readings:
        if val > 100 or val < 0:
            outlier_count += 1
    # Unused function - red herring
    def smooth_signal(data):
        return [sum(data[max(0, i-2):i+1]) / (i+1) for i in range(len(data))]
    
    # Core transformation (relevant)
    normalized = [calibration_factor * x for x in raw_readings]
    return normalized

# Simulated sensor data from biomedical device
data_packet = [72, 68, 74, 60, 80, 78, 63, 75, 69, 71]

# Decoy variables with plausible names
baseline_shift = 2.1
reference_pool = {65, 68, 70, 72, 75}
dummy_weights = [0.1, 0.2, 0.3]  # Unused

# Threshold configuration map (partially used)
thresholds = {
    'hr_low': 60,
    'hr_high': 100,
    'stress_index': 73,
    'recovery_zone': 65
}

# Data structure manipulation - relevant but obscured
health_data = []
for idx, reading in enumerate(data_packet):
    status = 'normal'
    if reading > thresholds['hr_high']:
        status = 'elevated'
    elif reading < thresholds['hr_low']:
        status = 'low'
    
    # Use of enumerate and zip (required Python feature)
    tags = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    paired = list(zip(data_packet, tags))
    
    health_data.append({'index': idx, 'value': reading, 'status': status})

# Spurious set operations (distractor)
active_zones = {x['value'] for x in health_data if x['status'] == 'normal'}
critical_set = {x for x in data_packet if x > 70}
overlap_region = active_zones & critical_set  # Looks important, unused later

# Secondary irrelevant computation chain
rolling_avg = 0
if len(data_packet) >= 3:
    rolling_avg = sum(data_packet[-3:]) / 3

# Key analysis function with embedded logic
def analyze_metrics(metrics, config):
    risk_score = 0
    stress_events = 0
    recovery_periods = 0
    
    # Complex conditional logic with interdependencies
    for entry in metrics:
        val = entry['value']
        if val > config['stress_index']:
            risk_score += 2
            stress_events += 1
        elif val <= config['recovery_zone']:
            risk_score -= 1
            recovery_periods += 1
    
    # Bitwise manipulation red herring
    encoded_flag = stress_events << 2 | (recovery_periods & 3)
    
    # Summation and accumulation (relevant)
    total_adjustment = 0
    for i, reading in enumerate(data_packet):
        if i % 2 == 0 and reading > 70:
            total_adjustment += reading // 10
        elif i % 2 == 1 and reading < 70:
            total_adjustment -= reading // 20
    
    # Final composite calculation (answer path)
    base_metric = len([m for m in metrics if m['value'] > 70])
    penalty = stress_events * 2
    bonus = recovery_periods
    
    # Critical execution point
    final_diagnostic = base_metric * 100 + bonus * 10 - penalty * 5 + total_adjustment
    
    # Dead code - misleading return alternatives
    if final_diagnostic < 0:
        return 0
    # Actual return
    return final_diagnostic

# Process data through pipeline
processed_readings = process_sensor_stream(data_packet)

# Primary evaluation call
final_diagnostic = analyze_metrics(health_data, thresholds)

# Output result as required
print(f"Target result: {final_diagnostic}")