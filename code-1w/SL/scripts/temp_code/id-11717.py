import math

# Simulated sensor network data processing with diagnostic logic
def collect_sensor_readings():
    raw_readings = {
        'sensor_a': [23.4, 25.1, 22.8, 24.6, 23.9],
        'sensor_b': [19.5, 18.7, 19.1, 20.3, 18.9],
        'sensor_c': [45.2, 44.8, 46.1, 45.5, 44.9],
        'sensor_d': [31.3, 32.7, 30.9, 31.8, 32.1]
    }
    return raw_readings

# Irrelevant preprocessing function (dead code path)
def normalize_readings(readings):
    normalized = {}
    for k, v in readings.items():
        mean_val = sum(v) / len(v)
        normalized[k] = [x / mean_val for x in v]
    return normalized  # Never used

# Core transformation pipeline
def preprocess_readings(raw_data):
    processed = {}
    stats_log = []  # Distractor: logged but not used later

    for sensor_id, values in raw_data.items():
        filtered = [v for v in values if 15 < v < 50]  # Validity filter
        avg = sum(filtered) / len(filtered)
        variance = sum((x - avg) ** 2 for x in filtered) / len(filtered)
        stddev = math.sqrt(variance)

        # Bit manipulation red herring
        magic_key = (int(avg) ^ int(stddev * 100)) & 0xFFFF
        checksum = (magic_key >> 8) | (magic_key << 8)  # Obfuscation

        processed[sensor_id] = {
            'baseline': round(avg, 3),
            'stability': round(100 / (stddev + 1), 2),
            'size_flag': len(values) > 4,
            'diagnostic_code': checksum  # Unused in final logic
        }

        # Logging irrelevant intermediate
        stats_log.append(f"{sensor_id}: {stddev:.3f}")

    return processed

# Decoy analysis function
def legacy_diagnostic(data):
    risk_score = 0
    for info in data.values():
        if info['stability'] < 80:
            risk_score += 10
    return risk_score * 2  # Not used

# Threshold configuration map (used in final step)
def generate_thresholds():
    base_config = {
        'critical': 20.0,
        'warning': 25.0,
        'optimal': 30.0
    }
    
    # Set operation red herring
    zones = set(['industrial', 'residential', 'mixed'])
    zone_offsets = {'industrial': -2.0, 'residential': 1.5, 'mixed': 0.0}
    applied_offsets = {zone: base_config['optimal'] + offset 
                       for zone in zones for offset in [zone_offsets[zone]]}
    
    # Only this subset is actually used
    return {
        'sensor_a': base_config['optimal'],
        'sensor_b': base_config['warning'],
        'sensor_c': base_config['critical'],
        'sensor_d': base_config['optimal']
    }

# Main analysis logic with conditional aggregation
def analyze_readings(processed_data, thresholds):
    alert_count = 0
    compliance_set = set()
    deviation_log = []  # Collected but not used

    for sensor, info in processed_data.items():
        baseline = info['baseline']
        stability = info['stability']
        threshold = thresholds[sensor]

        # Primary decision logic
        if baseline > threshold:
            if stability < 90.0:
                alert_count += 1
                deviation_log.append((sensor, 'HIGH_BASELINE_LOW_STABILITY'))
            else:
                compliance_set.add(sensor)
        elif baseline < threshold - 10:
            alert_count += 2
            deviation_log.append((sensor, 'CRITICALLY_LOW'))
        else:
            compliance_set.add(sensor)

    # Secondary rule: override if majority non-compliant
    if alert_count >= 2:
        final_state = 'REVIEW_NEEDED'
        impact_factor = 3
    elif len(compliance_set) == len(processed_data):
        final_state = 'STABLE'
        impact_factor = 1
    else:
        final_state = 'MONITORING'
        impact_factor = 2

    # Tertiary: compute diagnostic metric using bit math and set size
    code_hash = 0
    for c in final_state:
        code_hash ^= ord(c)
    code_hash &= 0xFF

    # Final computation - only this matters
    diagnostic_value = (alert_count * 100) + len(compliance_set) + (code_hash % 7)
    derived_flags = (alert_count << 3) | len(compliance_set)  # Distractor

    # Key result variable
    final_diagnostic = diagnostic_value + impact_factor

    # Dead assignment chain
    temp_buffer = [final_diagnostic + i for i in range(3)]
    temp_buffer = [x * 0.9 for x in temp_buffer]
    buffer_mean = sum(temp_buffer) / len(temp_buffer)

    return final_diagnostic

# Orphaned utility function (never called)
def calculate_entropy(values):
    from collections import Counter
    counts = Counter(values)
    total = len(values)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

# Execution flow
if __name__ == "__main__":
    # Step 1: Collect raw data
    raw_data = collect_sensor_readings()
    
    # Step 2: Preprocess into structured format
    processed_data = preprocess_readings(raw_data)
    
    # Step 3: Generate threshold rules
    threshold_map = generate_thresholds()
    
    # Step 4: Compute final diagnostic score
    final_diagnostic = analyze_readings(processed_data, threshold_map)
    
    # Output target result
    print(f"Result: {final_diagnostic}")