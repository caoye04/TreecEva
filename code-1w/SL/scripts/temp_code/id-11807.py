import itertools

# Simulated sensor array diagnostics with noise filtering and pattern analysis
def collect_sensor_readings():
    raw_signals = [12, 15, 22, 27, 30, 31, 34, 36, 38, 40]
    noise_floor = 14
    filtered = [x for x in raw_signals if x > noise_floor]  # Remove low-noise artifacts
    return filtered

# Legacy function - unused but looks relevant (red herring)
def legacy_calibrate(signal_list):
    adjusted = []
    for s in signal_list:
        if s % 3 == 0:
            adjusted.append(s * 0.9)
        else:
            adjusted.append(s * 1.1)
    return adjusted

# Signal transformation pipeline
def transform_signal_sequence(data):
    shifted = [(x << 1) + 3 for x in data]  # Bit shift and offset
    modded = [x % 17 for x in shifted]      # Modular reduction to wrap values
    return modded

# Advanced combinatorics-based pattern generator (distractor)
def generate_combinatorial_profiles(n):
    profiles = []
    for i in range(1, n+1):
        combos = list(itertools.combinations(range(n), i))
        profiles.append(len(combos))
    return profiles  # Never used

# Main diagnostic analyzer
def detect_anomaly_clusters(seq, limit):
    count = 0
    for a, b in itertools.pairwise(seq):
        if abs(b - a) > limit:
            count += 1
    return count

# Core logic: analyze transformed data patterns
def analyze_pattern(values, thresh):
    cumulative = 0
    for v in values:
        if v & 1:  # Check oddness via bitwise AND
            cumulative += v ** 2
        else:
            cumulative -= v
    result = cumulative * (thresh or 1)
    return result

# Secondary path - appears important but not used (dead code)
def compute_thermodynamic_index(readings):
    base = sum(readings) / len(readings)
    fluctuation = max(readings) - min(readings)
    index = base * 0.7 + fluctuation * 1.3
    return round(index, 3)

# Tertiary distraction: recursive checksum (unused)
def recursive_checksum(data, depth=0):
    if depth >= 3 or not data:
        return 0
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]
    return (sum(left) ^ sum(right)) + recursive_checksum(left, depth+1)

# Real execution path
if __name__ == "__main__":
    # Step 1: Collect real sensor data
    sensor_data = collect_sensor_readings()  # [15, 22, 27, 30, 31, 34, 36, 38, 40]

    # Step 2: Transform signal sequence
    transformed_data = transform_signal_sequence(sensor_data)
    # Apply transformations: (x << 1) + 3 → then % 17
    # 15→33%17=16, 22→47%17=13, 27→57%17=6, 30→63%17=12, 31→65%17=14,
    # 34→71%17=3, 36→75%17=7, 38→79%17=11, 40→83%17=15
    # transformed_data = [16, 13, 6, 12, 14, 3, 7, 11, 15]

    # Irrelevant computations below (distractions)
    anomaly_count = detect_anomaly_clusters(transformed_data, 4)  # Looks important
    combinatorial_signature = generate_combinatorial_profiles(6)   # Dead end
    recalibrated = legacy_calibrate(sensor_data)                    # Unused path
    thermodynamic_rating = compute_thermodynamic_index(sensor_data) # Not used
    dummy_checksum = recursive_checksum(transformed_data)          # Red herring

    # Critical threshold computed from non-obvious expression
    threshold = len([x for x in transformed_data if x > 10]) - 5  # Count >10: 16,13,12,14,11,15 → 6 elements → 6-5 = 1

    # Key statement
    final_diagnostic = analyze_pattern(transformed_data, threshold)

    # Print result as required
    print(f"Result: {final_diagnostic}")