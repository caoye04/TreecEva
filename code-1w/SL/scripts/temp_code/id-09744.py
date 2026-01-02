import math

# Simulated sensor data processing with diagnostic analysis
def collect_sensor_readings():
    raw_values = [127, 255, 64, 192, 32, 180, 95, 220]
    scaling_factor = 0.75
    adjusted = [val * scaling_factor for val in raw_values]
    return adjusted

# Irrelevant helper: color mapping for UI (dead code path)
def map_to_color(value):
    if value < 100:
        return 'blue'
    elif value < 200:
        return 'yellow'
    else:
        return 'red'

# Decoy function: never called but looks important
def compute_checksum(data_list):
    checksum = 0
    for i, val in enumerate(data_list):
        checksum ^= int(val) ^ (i * 31)
    return checksum % 256

# Signal processor with multiple transformation stages
def preprocess_signal(raw_readings):
    filtered = []
    noise_floor = 45.0
    for reading in raw_readings:
        if reading > noise_floor:
            normalized = (reading - noise_floor) / (255.0 * 0.75 - noise_floor)
            filtered.append(round(normalized * 100, 3))
    return filtered

# Threshold configuration using dictionary and set operations
base_thresholds = {
    'low': 30.0,
    'medium': 60.0,
    'high': 85.0,
    'critical': 95.0
}

active_zones = {'low', 'medium', 'high'}
excluded_zones = {'critical'}
enabled_thresholds = active_zones - excluded_zones

threshold_map = {k: v for k, v in base_thresholds.items() if k in enabled_thresholds}
system_status = { 'initialized': True, 'mode': 'diagnostic' }

# Data enrichment with zip and enumerate (some fields unused)
def enrich_data(filtered_data):
    timestamps = list(range(len(filtered_data)))
    labeled_data = []
    
    for idx, (t, val) in enumerate(zip(timestamps, filtered_data)):
        deviation = abs(val - 50.0)
        category = 'stable' if deviation < 15 else 'variable'
        # Unused metadata simulates complexity
        metadata = {
            'index': idx,
            'time_offset': t * 0.001,
            'sequence_id': f"S{idx % 4}",
            'calibration_flag': idx % 7 == 0
        }
        labeled_data.append({
            'value': val,
            'deviation_score': deviation,
            'type': category
        })
    return labeled_data

# Core analysis logic with branching and aggregation
def analyze_signal(data_records, thresholds):
    aggregate_score = 0.0
    event_log = []
    
    for entry in data_records:
        val = entry['value']
        dev = entry['deviation_score']
        
        # Multi-level classification logic
        if val >= thresholds['medium']:
            if val >= thresholds['high']:
                level = 'high_risk'
            else:
                level = 'moderate_risk'
        else:
            level = 'low_risk'
            
        # Parallel evaluation using logical combinations
        is_anomalous = dev > 20.0 and level != 'low_risk'
        is_critical_phase = val > 88.0  # Never reached due to preprocessing cap
        
        if is_anomalous:
            event_log.append(level)
        
        # Scoring with arithmetic combination
        contribution = 0
        if level == 'high_risk':
            contribution = val * 1.2
        elif level == 'moderate_risk':
            contribution = val * 0.8
        else:
            contribution = val * 0.3
        
        aggregate_score += contribution
    
    # Final adjustment based on event frequency
    anomaly_count = len(event_log)
    if anomaly_count > 3:
        aggregate_score *= 1.15
    elif anomaly_count == 0:
        aggregate_score *= 0.85
    
    # Secondary transformation
    transformed = math.log(aggregate_score + 10) * 10
    final_weight = len(data_records) / 10.0
    weighted_result = transformed * final_weight
    
    # Red herring: complex bit manipulation (unused)
    decoy_int = int(transformed)
    masked = (decoy_int << 3) & 0xFF
    rotated = ((masked >> 1) | (masked << 7)) & 0xFF
    
    # Actual output
    return round(weighted_result, 4)

# Execution pipeline
if __name__ == "__main__":
    # Step 1: Collect raw sensor input
    raw_data = collect_sensor_readings()
    
    # Step 2: Preprocess to remove noise
    processed_readings = preprocess_signal(raw_data)
    
    # Step 3: Enrich with contextual labels
    enriched_dataset = enrich_data(processed_readings)
    
    # Step 4: Run final diagnostic analysis
    final_diagnostic = analyze_signal(enriched_dataset, threshold_map)
    
    # Output target result
    print(f"Target result: {final_diagnostic}")