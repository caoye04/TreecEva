import itertools

# Simulated sensor array data from a distributed environmental monitoring system
def collect_sensor_data():
    raw_readings = [
        (101, 23.4, 1), (102, 24.1, 0), (103, 19.5, 1), (104, 25.0, 0),
        (105, 22.8, 1), (106, 18.9, 0), (107, 24.3, 1), (108, 20.1, 0)
    ]
    return raw_readings

# Legacy function for backward compatibility – not used in current logic
def deprecated_normalization(data):
    mean_val = sum(x[1] for x in data) / len(data)
    return [(x[0], (x[1] - mean_val) * 1.5, x[2]) for x in data]

# Irrelevant transformation: applies bitwise mask to sensor IDs (not part of final logic)
def apply_bitwise_mask(readings, mask=0xFF):
    masked = []
    for r in readings:
        masked_id = r[0] & mask
        masked.append((masked_id, r[1], r[2]))
    return masked

# Misleading intermediate calculation – appears important but unused
def compute_variance(readings):
    temps = [r[1] for r in readings]
    mean_temp = sum(temps) / len(temps)
    variance = sum((t - mean_temp) ** 2 for t in temps) / len(temps)
    return round(variance, 4)

# Data filtering based on status flag and temperature threshold
def filter_valid_readings(readings):
    valid = []
    for sid, temp, active in readings:
        if active == 1 and temp > 20.0:
            valid.append((sid, temp))
    return valid

# Flag analysis module – evaluates system health from binary indicators
def analyze_flags(flag_sequence):
    flag_count = {0: 0, 1: 0}
    for f in flag_sequence:
        if f in flag_count:
            flag_count[f] += 1
    return flag_count[1] > flag_count[0]  # True if majority active

# Core processing: computes weighted diagnostic score
def process_readings(valid_pairs, flags_dict):
    base_score = 0
    weight_distribution = itertools.cycle([0.8, 1.1, 0.9])

    for (sensor_id, temp), weight in zip(valid_pairs, weight_distribution):
        contribution = temp * weight
        if sensor_id % 2 == 1:
            contribution *= 0.95  # Slight decay for odd IDs
        base_score += contribution

    # Additional adjustment based on global flag state
    if flags_dict.get('overload', False):
        base_score *= 0.8
    elif flags_dict.get('optimal', False):
        base_score *= 1.2

    # Final nonlinear transformation
    import math
    adjusted_score = math.log(base_score * 2 + 1, 1.5)
    return int(round(adjusted_score))

# Unused recursive helper – looks relevant but not called in execution path
def recursive_sum_threshold(data, threshold=50.0, acc=0):
    if not data or acc > threshold:
        return acc
    return recursive_sum_threshold(data[1:], threshold, acc + data[0][1])

# Main execution flow
if __name__ == "__main__":
    # Step 1: Collect raw sensor data
    all_readings = collect_sensor_data()

    # Step 2: Apply irrelevant bitwise masking (distraction)
    masked_readings = apply_bitwise_mask(all_readings)

    # Step 3: Compute misleading variance statistic (red herring)
    variance_snapshot = compute_variance(all_readings)  # Not used later

    # Step 4: Extract status flags for analysis
    status_flags = [r[2] for r in all_readings]
    majority_active = analyze_flags(status_flags)

    # Step 5: Filter valid sensor entries
    filtered_data = filter_valid_readings(all_readings)

    # Step 6: Construct system flag dictionary with decoy keys
    system_flags = {
        'optimal': majority_active and variance_snapshot < 5.0,
        'overload': False,
        'debug_mode': True,
        'version': '2.1'
    }

    # Step 7: Process final diagnostic score
    final_diagnostic = process_readings(filtered_data, system_flags)

    # Output target result
    print(f"Result: {final_diagnostic}")