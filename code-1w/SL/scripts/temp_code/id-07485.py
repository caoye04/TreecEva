def analyze_system_integrity():
    # Simulated sensor readings (irrelevant to final result)
    temperature_readings = [23.5, 24.1, 22.7, 25.3]
    pressure_samples = {"p1": 101.3, "p2": 102.8, "p3": 99.4}
    calibration_offset = sum(temperature_readings) % 7

    # Core logic variables
    base_signature = 17
    sequence_pool = [1, 0, 1, 1, 0, 1]
    mask_pattern = [0, 1, 1, 0, 1, 0]

    # Irrelevant transformation chain (distractor)
    def transform(x):
        return (x ** 2 + 3 * x + 5) % 101

    processed_temperatures = list(map(lambda t: transform(int(t)), temperature_readings))
    entropy_score = len(processed_temperatures) * calibration_offset

    # Critical data structures
    logic_trace = []
    activation_map = set()

    for i in range(len(sequence_pool)):
        bit = sequence_pool[i]
        mask_bit = mask_pattern[i]

        if bit == 1:
            logic_trace.append(base_signature ^ i)
            if mask_bit == 1:
                activation_map.add(base_signature + i)

        # Dead code path (misleading)
        if i > 10:
            fallback_value = (base_signature << 3) | 7
            logic_trace.append(fallback_value)

    # Secondary irrelevant computation (red herring)
    checksum = 0
    for key in pressure_samples:
        checksum += int(pressure_samples[key])
    checksum = (checksum * 37) % 97

    # Decoy function that's never called
    def compute_health_index(data):
        return sum(data) / len(data) + 100

    # Another decoy variable
    system_risk_factor = checksum / (calibration_offset + 1) if calibration_offset else 0

    # Key intermediate steps with meaningful computation
    filtered_trace = [x for x in logic_trace if x % 2 == 1]  # Only odd values matter
    mapped_values = list(map(lambda x: (x * 2) ^ 15, filtered_trace))

    # Aggregation with modular arithmetic
    aggregate = 0
    for val in mapped_values:
        aggregate = (aggregate + val) % 10000

    # Set-based calculation
    influence_score = sum(activation_map) if activation_map else 50

    # Final combination
    def process_metrics(trace_data, act_map):
        trace_sum = sum(trace_data)
        map_sum = sum(act_map)
        return (trace_sum * 3 + map_sum * 2) % 50000

    final_diagnostic = process_metrics(logic_trace, activation_map)
    
    # Output required format
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Execute function
analyze_system_integrity()