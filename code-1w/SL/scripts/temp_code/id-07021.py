def analyze_system_metrics(sensor_data, thresholds):
    # Irrelevant initialization - red herring
    baseline_offset = 23.7
    calibration_matrix = [[i * j for j in range(3)] for i in range(3)]
    temp_history = [0] * len(sensor_data)
    spike_count = 0
    aggregate_score = 0
    phase_modulator = 1

    # Distractor loop: computes but doesn't use spike count
    for idx, reading in enumerate(sensor_data):
        if reading > thresholds[idx] * 1.5:
            spike_count += 1

    # Real logic begins: compute rolling adjusted average
    adjusted_values = []
    for i in range(len(sensor_data)):
        adjustment = (sensor_data[i] - baseline_offset) * 0.85
        adjusted_values.append(adjustment if adjustment > 0 else 0)

    # Compute energy envelope using bit manipulation (relevant)
    energy_sum = 0
    for val in adjusted_values:
        scaled_val = int(val * 10)
        # Bitwise processing to simulate hardware-level analysis
        processed = (scaled_val ^ 0xFF) & 0x7F  # Flip lower 8 bits, mask to 7 bits
        energy_sum += processed >> 2  # Use shifted result

    # Secondary distractor: complex but unused data structure
    status_map = {i: ('critical' if sensor_data[i] > thresholds[i] else 'normal') 
                  for i in range(len(sensor_data))}

    # Conditional expression affecting phase modulator (RELEVANT)
    phase_modulator = 3 if sum(1 for s in sensor_data if s > 50) >= 2 else 1

    # Compute aggregate score from energy and adjustments (RELEVANT)
    aggregate_score = energy_sum // 3

    # Temperature factor derived from specific pattern (RELEVANT)
    temperature_factor = 0
    for i, (s, t) in enumerate(zip(sensor_data, thresholds)):
        if s > t and i % 2 == 1:
            temperature_factor += s * 0.1

    # Dead code path - never executed due to prior logic
    if baseline_offset < 0:
        temperature_factor *= 0.5

    # Key statement: combines multiple computed values
    final_diagnostic = aggregate_score + temperature_factor * phase_modulator

    # Print result as required
    print(f"Result: {final_diagnostic}")

    return final_diagnostic

# Input data (deterministic)
sensor_readings = [45, 67, 30, 88, 40]
threshold_limits = [40, 60, 35, 80, 45]

# Execute function
def main():
    result = analyze_system_metrics(sensor_readings, threshold_limits)

main()