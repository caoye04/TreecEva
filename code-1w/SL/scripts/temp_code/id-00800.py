def analyze_sensor(value, baseline):
    deviation = abs(value - baseline)
    if deviation > 50:
        return 'CRITICAL'
    elif deviation > 25:
        return 'WARNING'
    else:
        return 'NORMAL'


def compute_efficiency(rpm, load, factor=0.85):
    if rpm == 0:
        return 0.0
    efficiency = (load / rpm) * factor * 100
    return round(efficiency, 2)


def validate_readings(readings):
    valid_count = 0
    for r in readings:
        if 10 <= r <= 150:
            valid_count += 1
    return valid_count > len(readings) * 0.7


def generate_diagnostic_code(status, code_map):
    return code_map.get(status, 'ERR')

# Irrelevant helper function (dead path)
def deprecated_calib_adjust(x):
    return x * 0.9 + 3

# Unused constant
turbine_version = "T-4.7X"

# Simulated sensor data from wind turbine array
turbine_data = [
    {'id': 'WT-01', 'rpm': 1280, 'load': 320, 'vibration': 45, 'temp': 78},
    {'id': 'WT-02', 'rpm': 1190, 'load': 290, 'vibration': 62, 'temp': 85},
    {'id': 'WT-03', 'rpm': 1320, 'load': 340, 'vibration': 24, 'temp': 70},
    {'id': 'WT-04', 'rpm': 1210, 'load': 305, 'vibration': 58, 'temp': 82}
]

# Threshold baselines (used in analysis)
thresh_vibration = 55
thresh_temp = 80

# Mapping status to diagnostic codes (partially used)
diagnostic_codes = {
    'CRITICAL': 99,
    'WARNING': 42,
    'NORMAL': 7
}

# Decoy dictionary with misleading values
status_weights = {
    'CRITICAL': 10,
    'WARNING': 5,
    'NORMAL': 1,
    'INFO': 0
}

# Auxiliary processing list (distractor)
recent_logs = ['OK', 'OK', 'REVIEW', 'OK']

# Main aggregation function
def aggregate_metrics(data, thresholds):
    results = []
    total_efficiency = 0.0
    critical_count = 0
    statuses = []
    
    for idx, turbine in enumerate(data):
        rpm = turbine['rpm']
        load = turbine['load']
        vib = turbine['vibration']
        temp = turbine['temp']
        
        # Compute derived metric
        efficiency = compute_efficiency(rpm, load)
        total_efficiency += efficiency
        
        # Analyze health metrics
        vib_status = analyze_sensor(vib, thresholds)
        temp_status = analyze_sensor(temp, thresholds)
        
        # Determine overall status
        if vib_status == 'CRITICAL' or temp_status == 'CRITICAL':
            status = 'CRITICAL'
        elif vib_status == 'WARNING' or temp_status == 'WARNING':
            status = 'WARNING'
        else:
            status = 'NORMAL'
        
        statuses.append(status)
        
        # Track critical units
        if status == 'CRITICAL':
            critical_count += 1
    
    # Calculate average efficiency
    avg_efficiency = total_efficiency / len(data)
    
    # Generate status summary using zip (irrelevant to final answer but adds complexity)
    indexed_statuses = list(zip(range(len(statuses)), statuses))
    status_summary = {i: s for i, s in indexed_statuses}
    
    # Validate sensor inputs (unused result)
    all_rpm = [t['rpm'] for t in data]
    _ = validate_readings(all_rpm)  # Result ignored
    
    # Compute composite score (distractor)
    composite_score = 0
    for s in statuses:
        if s == 'CRITICAL':
            composite_score -= 10
        elif s == 'WARNING':
            composite_score -= 5
        else:
            composite_score += 2
    
    # Final logic branch determining output
    if critical_count >= 2:
        category_flag = 3
    elif critical_count == 1:
        category_flag = 2
    else:
        if avg_efficiency > 25.0:
            category_flag = 1
        else:
            category_flag = 0
    
    # Key transformation using conditional expression and bitwise op
    adjustment = 17 if category_flag > 1 else 9
    raw_value = int(avg_efficiency * 2) ^ adjustment  # XOR as nonlinear transform
    
    # Final diagnostic calculation (this is the real answer)
    final_diagnostic = (raw_value * 1000) + category_flag
    
    return final_diagnostic

# Execution entry point
final_diagnostic = aggregate_metrics(turbine_data, thresh_vibration)
print(f"Target result: {final_diagnostic}")