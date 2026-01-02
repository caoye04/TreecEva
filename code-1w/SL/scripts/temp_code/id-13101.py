from collections import defaultdict, Counter

# Simulated sensor data processing with diagnostic scoring
def process_sensor_readings(raw_data):
    readings_log = defaultdict(int)
    anomalies = []
    cumulative_power = 0
    temp_buffer = []
    checksum = 0

    for idx, val in enumerate(raw_data):
        readings_log[f'entry_{idx}'] = val
        if val < 0:
            anomalies.append(idx)
        if idx % 3 == 0:
            cumulative_power += val ** 2
        elif idx % 5 == 0:
            temp_buffer.append(val * 1.5)
        else:
            checksum += (val + idx) % 7

    # Irrelevant transformation chain
    transformed = [x * 1.1 for x in raw_data if x > 10]
    shifted = [t - 5 for t in transformed]
    normalized = [n / sum(shifted) if sum(shifted) != 0 else 0 for n in shifted]

    # Decoy statistical analysis
    mean_val = sum(raw_data) / len(raw_data) if raw_data else 0
    variance_proxy = sum((x - mean_val) ** 2 for x in raw_data) / len(raw_data) if raw_data else 0
    entropy_estimate = 0
    freq_counter = Counter(transformed)
    for freq in freq_counter.values():
        if freq > 0:
            entropy_estimate -= (freq / len(transformed)) * (freq / len(transformed))

    # Unused recursive helper (red herring)
    def calculate_depth(n):
        return 1 + calculate_depth(n - 1) if n > 0 else 0
    
    # Dead code path - never executed due to condition
    emergency_override = False
    if len(anomalies) > 100:
        backup_register = [0] * 100
        for i in range(len(backup_register)):
            backup_register[i] = i * 2
        emergency_override = True

    # Core computation buried in noise
    base_integral = sum(x for x in raw_data if x % 2 == 1 and x > 0)
    spike_count = sum(1 for i in range(1, len(raw_data)) if raw_data[i] - raw_data[i-1] > 20)
    aggregate_score = base_integral + spike_count * 5

    # Distractor: complex but unused formula
    hypothetical_yield = (cumulative_power * entropy_estimate) / (variance_proxy + 1e-5) if variance_proxy else 0
    decay_sequence = [hypothetical_yield]
    for _ in range(4):
        next_val = decay_sequence[-1] * 0.7 + 2
        decay_sequence.append(next_val)

    # Key variables for final calculation
    correction_factor = len(anomalies) + 1
    adjustment_multiplier = len(temp_buffer) - len(normalized)

    # Final result embedded among distractions
    final_diagnostic = aggregate_score + correction_factor * adjustment_multiplier

    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Input data
sensor_input = [12, -5, 18, 23, 7, 41, 3, 66, -14, 9, 25, 31, 8, 17, 73]

# Execute
process_sensor_readings(sensor_input)