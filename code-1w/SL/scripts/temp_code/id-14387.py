from collections import defaultdict, Counter

# Simulated sensor data from IoT medical device array
def collect_medical_readings():
    readings = [
        (102.3, 'temp'), (76, 'bpm'), (102.5, 'temp'), (78, 'bpm'), 
        (101.9, 'temp'), (80, 'bpm'), (103.1, 'temp'), (77, 'bpm')
    ]
    return readings

# Legacy function – intentionally unused but looks relevant
def compute_average_temperature_v1(data):
    temps = [x[0] for x in data if x[1] == 'temp']
    total = 0
    for t in temps:
        total += t
    return total / len(temps)

# Primary processing pipeline
def process_patient_data(raw_readings):
    # Distractor: Initialize multiple tracking structures
    vital_stats = defaultdict(list)
    anomaly_log = []
    processed_entries = []
    cumulative_shift = 0.0

    # Real work: categorize and normalize
    for value, vtype in raw_readings:
        vital_stats[vtype].append(value)
        processed_entries.append((vtype, value))
        
        # Irrelevant transformation chain
        shifted = value * 1.002 - 0.3
        shifted = round(shifted, 2)
        cumulative_shift += shifted % 1

    # Compute base metrics
    temp_values = vital_stats['temp']
    heart_rates = vital_stats['bpm']
    avg_temp = sum(temp_values) / len(temp_values)
    avg_bpm = sum(heart_rates) / len(heart_rates)

    # Distractor: unused statistical analysis
    rate_counter = Counter(heart_rates)
    most_common_rate = rate_counter.most_common(1)[0][1]

    # Begin diagnostic logic
    temperature_deviation = abs(avg_temp - 98.6)
    bpm_stability = max(heart_rates) - min(heart_rates)

    # Intermediate diagnostic scores (some used, some not)
    thermal_risk_score = 0
    if temperature_deviation > 3.0:
        thermal_risk_score = 4
    elif temperature_deviation > 2.0:
        thermal_risk_score = 3
    elif temperature_deviation > 1.0:
        thermal_risk_score = 2
    else:
        thermal_risk_score = 1

    # Unused risk branch – looks important
    cardiac_risk_estimate = 0
    if avg_bpm > 100:
        cardiac_risk_estimate = 5
    elif avg_bpm < 60:
        cardiac_risk_estimate = 4

    # Real path: stability index calculation
    stability_index = 0
    for i, hr in enumerate(heart_rates):
        if i > 0 and abs(hr - heart_rates[i-1]) > 8:
            stability_index += 1

    # Secondary distractor: time-series mockup
    time_gaps = []
    for idx, (val, typ) in enumerate(processed_entries):
        time_gaps.append(idx * 0.5 + (val % 2))

    # Core health metric computation
    base_health_score = 100 - (temperature_deviation * 5) - (stability_index * 3)
    
    # Legacy bias factor from old calibration (irrelevant but referenced)
    legacy_bias_table = {76: 0.1, 77: 0.2, 78: 0.1, 80: 0.3}
    system_bias = sum(legacy_bias_table.get(int(hr), 0) for hr in heart_rates)

    # Correction mechanism based on entry count
    entry_count_map = {}
    for typ in vital_stats:
        entry_count_map[typ] = len(vital_stats[typ])
    
    total_entries = sum(entry_count_map.values())
    correction_factor = 1.0
    if total_entries > 6:
        correction_factor = 0.95
    elif total_entries > 4:
        correction_factor = 1.05
    else:
        correction_factor = 1.1

    # Red herring: unused weighted average
    weighted_sum = 0.0
    weights = [0.7, 1.0, 0.8, 0.9, 1.1, 1.0, 0.7, 0.8]
    for w_idx, (_, val) in enumerate(processed_entries):
        if w_idx < len(weights):
            weighted_sum += val * weights[w_idx]

    # Final aggregation with key statement
    aggregate_health_score = base_health_score + 10  # Boost for responsiveness
    final_diagnostic = aggregate_health_score + system_bias * correction_factor

    # Distractor: late-stage override that never triggers
    if len(anomaly_log) > 5:
        final_diagnostic *= 0.5

    return final_diagnostic

# Orchestration layer with mock calibration
if __name__ == '__main__':
    # Unused calibration profile
    calibration_mode = 'standard'
    debug_trace = []

    # Simulate multi-patient batch (only first matters)
    all_readings = [collect_medical_readings()]
    
    # Apply dummy normalization across patients
    normalized_offsets = []
    for patient_data in all_readings:
        offset = sum(r[0] for r in patient_data) % 7
        normalized_offsets.append(offset)
    
    # Process only the first patient
    result = process_patient_data(all_readings[0])
    
    # Print target result
    print(f"Result: {result}")