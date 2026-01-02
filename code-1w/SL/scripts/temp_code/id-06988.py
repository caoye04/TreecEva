from collections import defaultdict

# Simulate sensor data from industrial equipment
equipment_readings = [
    {'sensor': 'temp', 'values': [23.5, 24.1, 22.9, 25.0, 23.8]},
    {'sensor': 'pressure', 'values': [98, 101, 97, 103, 99]},
    {'sensor': 'vibration', 'values': [4, 7, 3, 8, 5]}
]

# Auxiliary transformation map for non-linear calibration
calibration_map = lambda x: round(x ** 0.5 * 1.1, 2)

# Misleading preprocessing: unused in final logic but adds cognitive load
preliminary_stats = {}
for reading in equipment_readings:
    key = reading['sensor']
    values = reading['values']
    preliminary_stats[key] = {
        'raw_mean': sum(values) / len(values),
        'adjusted': [calibration_map(v) for v in values if v > 0]
    }

# Distractor: historical baseline (not used in calculation)
historical_baseline = {
    'temp_avg': 24.0,
    'tolerance_window': 1.5
}

# Core processing pipeline
processed_data = defaultdict(list)
for entry in equipment_readings:
    sensor_type = entry['sensor']
    raw_values = entry['values']
    
    # Normalize temperature readings to deviation from mean
    if sensor_type == 'temp':
        mean_val = sum(raw_values) / len(raw_values)
        deviations = [abs(v - mean_val) for v in raw_values]
        processed_data['deviations'] = deviations
    elif sensor_type == 'pressure':
        # Only store pressure values above 100
        high_pressure = [p for p in raw_values if p > 100]
        processed_data['pressure_peaks'] = high_pressure
    elif sensor_type == 'vibration':
        # Count significant vibrations
        spike_count = len([v for v in raw_values if v >= 6])
        processed_data['spike_count'] = spike_count

# Secondary distractor: string-based status check (irrelevant)
diagnostic_log = "System nominal: TEMP_STABLE, PRESSURE_FLUCTUATING"
status_flags = diagnostic_log.lower().split(': ')[1].split(', ')
active_warnings = [flag for flag in status_flags if 'FLUCT' in flag.upper()]

# Helper function with red herring parameter
def calculate_stability(data, threshold=0.5):
    dev = data.get('deviations', [])
    if len(dev) == 0:
        return 0
    avg_dev = sum(dev) / len(dev)
    return 1 if avg_dev < threshold else 0  # Not used in final answer

# Actual efficiency calculation
def calculate_efficiency(data):
    deviations = data.get('deviations', [])
    pressure_peaks = data.get('pressure_peaks', [])
    spike_count = data.get('spike_count', 0)
    
    base_efficiency = 100.0
    
    # Deduct based on thermal instability
    if deviations:
        instability_penalty = sum(deviations) * 2.5
        base_efficiency -= instability_penalty
    
    # Bonus for stable pressure
    pressure_bonus = len(pressure_peaks) * 3.2
    base_efficiency += pressure_bonus
    
    # Heavy penalty for vibration spikes
    vibration_penalty = spike_count * 7.8
    base_efficiency -= vibration_penalty
    
    return round(base_efficiency, 4)

# Key execution point
stability_flag = calculate_stability(processed_data)
efficiency_score = calculate_efficiency(processed_data)

# Final output
Result: {efficiency_score}