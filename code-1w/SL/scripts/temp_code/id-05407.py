from itertools import combinations, chain

def analyze_sensor_network():
    # Simulated environmental sensor readings (real data)
    base_readings = [14.3, 18.7, 22.1, 19.5, 16.8, 25.3, 20.4, 17.9]
    calibration_offset = 1.2
    adjusted_readings = [round(x + calibration_offset, 2) for x in base_readings]

    # Irrelevant secondary system: legacy binary flag decoder (distraction)
    def decode_flags(flag_seq):
        result = 0
        for i, bit in enumerate(flag_seq):
            result += bit << (3 - i)
        return result

    legacy_flags = [1, 0, 1, 1]
    decoded_status = decode_flags(legacy_flags)  # Red herring

    # Primary data processing begins
    outlier_indices = []
    mean_val = sum(adjusted_readings) / len(adjusted_readings)
    for i, val in enumerate(adjusted_readings):
        if abs(val - mean_val) > 3.5:
            outlier_indices.append(i)

    filtered_data = [v for i, v in enumerate(adjusted_readings) if i not in outlier_indices]

    # Complex threshold logic with decoy mappings
    safety_levels = {'low': 15.0, 'med': 18.5, 'high': 22.0}
    maintenance_cycle = [0] * 4  # Unused tracking array

    # Decoy state tracker (dead code path)
    system_state_log = []
    for tick in range(3):
        system_state_log.append(f"IDLE:{tick}")

    # Real threshold map used in computation
    threshold_map = {
        'warning': safety_levels['med'] + 1.7,
        'critical': safety_levels['high'] + 2.4
    }

    # Auxiliary transformation using itertools (valid usage)
    pair_combinations = list(combinations(filtered_data, 2))
    high_risk_pairs = []
    for pair in pair_combinations:
        if sum(pair) > 42.0:
            high_risk_pairs.append(pair)

    risk_count = len(high_risk_pairs)

    # Core diagnostic function with nested logic
    def process_readings(data, thresholds):
        warning_level = thresholds['warning']
        critical_level = thresholds['critical']
        count_warn = 0
        count_crit = 0

        for reading in data:
            if reading >= critical_level:
                count_crit += 1
            elif reading >= warning_level:
                count_warn += 1

        # Secondary check: pattern in deviations
        deviations = [abs(x - mean_val) for x in data]
        large_deviation_count = sum(1 for d in deviations if d > 2.0)

        # Bit manipulation red herring (irrelevant)
        encoded_diagnostic = (count_warn << 2) | (large_deviation_count & 3)

        # Actual formula for final result
        base_score = count_crit * 1000 + count_warn * 100
        adjustment = 0
        if large_deviation_count >= 3:
            adjustment = 42
        elif risk_count > 2:
            adjustment = -17

        return base_score + adjustment

    # Final computation step
    intermediate_flag = decoded_status > 0  # Misleading boolean
    temporal_buffer = list(chain.from_iterable([(x,) * 1 for x in filtered_data]))  # No-op transformation

    final_diagnostic = process_readings(filtered_data, threshold_map)
    
    print(f"Result: {final_diagnostic}")

analyze_sensor_network()