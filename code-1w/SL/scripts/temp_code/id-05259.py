from collections import defaultdict, Counter

# Simulated sensor network diagnostic system
def analyze_readings(readings):
    # Core variables for analysis
    valid_sensors = []
    checksum = 0
    anomaly_count = 0
    temp_log = []

    # Irrelevant tracking (distractor)
    debug_trace = []
    cycle_counter = 0
    dummy_state = [0] * 5

    # Process each sensor's data
    for idx, data in enumerate(readings):
        if not data:
            continue
        
        # Compute rolling checksum (relevant)
        for val in data:
            checksum ^= val  # Bitwise interference
            if val > 100 or val < 10:
                anomaly_count += 1

        # Determine sensor validity (relevant path)
        avg_val = sum(data) / len(data)
        if 15 <= avg_val <= 95:
            valid_sensors.append(idx)
            temp_log.extend(data)
        
        # Dead code branch - never executed due to logic (red herring)
        if idx > len(readings) * 2:
            dummy_state[cycle_counter % 5] += 1
            debug_trace.append(f"Cycle {cycle_counter}")

        # Unused transformation (distractor)
        transformed = [((x << 1) | 1) & 255 for x in data]
        
        cycle_counter += 1

    # Misleading intermediate calculation (decoy result)
    pseudo_entropy = 0
    freq_counter = Counter(temp_log)
    for freq in freq_counter.values():
        if freq > 2:
            pseudo_entropy += freq * 3

    # Secondary irrelevant structure (distractor)
    metadata_map = defaultdict(list)
    for i, r in enumerate(readings):
        metadata_map['lengths'].append(len(r))
        metadata_map['max_vals'].append(max(r) if r else 0)

    # Unused recursive helper (dead function)
    def trace_propagation(x, depth):
        if depth == 0:
            return x
        return trace_propagation((x ^ depth) + 1, depth - 1)
    
    # Call only if condition met — which it isn't (misleading call)
    if len(valid_sensors) > 100:
        trace_propagation(checksum, 10)

    # Core computation begins here — actual relevant logic
    sensor_count = len(valid_sensors)
    
    # Another decoy variable with complex but unused logic
    weighted_sum = 0
    for i, data in enumerate(readings):
        if i in valid_sensors:
            for v in data:
                weighted_sum += (v * (i + 1)) >> 1

    # Real signal extraction
    primary_signal = 0
    for val in temp_log:
        if val % 2 == 0:
            primary_signal += val ** 2
        else:
            primary_signal -= val

    # Final aggregation — this is where the answer comes from
    aggregate_score = primary_signal + (checksum * anomaly_count)
    
    # Key statement: target variable assignment
    final_diagnostic = aggregate_score // (sensor_count + 1)
    
    # Print required output
    print(f"Result: {final_diagnostic}")
    
    # Return unused metrics (distraction)
    return {
        'diagnostic': final_diagnostic,
        'valid_sensors': valid_sensors,
        'pseudo_entropy': pseudo_entropy,
        'weighted_sum': weighted_sum
    }

# Input data (deterministic seed)
sensor_data = [
    [24, 35, 46, 57],
    [80, 22, 18, 91],
    [105, 12, 77, 88],  # First and third entries have anomalies
    [44, 52, 61, 39],
    [10, 96, 30, 41]
]

# Execute analysis
result = analyze_readings(sensor_data)