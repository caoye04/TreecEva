from collections import defaultdict, Counter

# Simulated sensor data processing with diagnostic validation
def process_sensors(raw_readings):
    base_metrics = defaultdict(float)
    temp_log = []
    checksum = 0
    
    for idx, reading in enumerate(raw_readings):
        if idx % 7 == 0:
            # Decoy logic: rarely triggered, misleading pattern
            base_metrics['skipped'] += 1
            continue
            
        clean_value = abs(reading) % 100
        if clean_value > 50:
            base_metrics['high_count'] += 1
            temp_log.append(clean_value * 0.9)
        else:
            base_metrics['low_count'] += 1
            temp_log.append(clean_value * 1.1)

        # Irrelevant transformation chain (distractor)
        transformed = (clean_value ^ 255) & 63
        intermediate = (transformed + 42) // 3
        checksum ^= intermediate

    # Real signal extraction
    valid_data = [x for x in temp_log if 10 < x < 90]
    signal_strength = sum(valid_data) / len(valid_data) if valid_data else 0

    # Noise analysis (used later)
    noise_ratio = len([x for x in temp_log if x <= 10 or x >= 90]) / len(temp_log) if temp_log else 0

    # Red herring: unused complex structure
    decoy_analysis = {
        'entropy': sum((v / len(temp_log))**2 for v in Counter(temp_log).values()) if temp_log else 0,
        'peak_shift': max(temp_log, default=0) - min(temp_log, default=0),
        'glitch_count': base_metrics['skipped']
    }

    # Diagnostic calibration with multiple false paths
    flags = []
    if base_metrics['high_count'] > base_metrics['low_count']:
        flags.append(1)
    if noise_ratio > 0.3:
        flags.append(2)
    if checksum % 5 == 0:
        flags.append(4)  # Never actually used

    # Actual calibration path
    mode_flag = flags[0] if len(flags) > 0 else 0
    adjustment = 0
    if mode_flag == 1:
        adjustment = 15.5
    elif mode_flag == 2:
        adjustment = -8.3
    else:
        adjustment = 5.0  # Default fallback

    # Fake scoring model (dead code path)
    def legacy_score(data):
        return sum(x**0.5 for x in data) * 0.7  # Unused

    # Real aggregation
    aggregate_score = signal_strength + adjustment

    # Misleading intermediate calculation
    pseudo_entropy = sum((x * 0.01) ** 2 for x in raw_readings)  # Not used

    # Critical statement with relevant variables
    correction_factor = 20 if noise_ratio < 0.25 else 10
    final_diagnostic = aggregate_score + correction_factor * (1 - noise_ratio)

    # Output required format
    print(f"Result: {final_diagnostic}")

    # Unused but plausible-looking diagnostics
    summary_report = {
        'readings_processed': len(raw_readings) - base_metrics['skipped'],
        'calibration_flags': flags,
        'checksum_final': checksum,
        'pseudo_entropy': pseudo_entropy
    }

    return final_diagnostic

# Input data - fixed seed for determinism
sensor_input = [88, -12, 67, 45, 91, 23, 56, 77, 14, 82, 33, 61, 19, 74, 50, 89, 27, 95, 38, 63]

result = process_sensors(sensor_input)