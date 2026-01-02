from collections import defaultdict
from itertools import cycle

# Simulate a thermal regulation system with state tracking
def monitor_temperature_flux(sensor_readings):
    flux_records = defaultdict(int)
    spike_count = 0
    base_threshold = 75.3
    adjustment_factor = 0.89

    for reading in sensor_readings:
        if reading > base_threshold:
            flux_records['overheat'] += 1
            spike_count += 1
        elif reading < 30.0:
            flux_records['freeze'] += 1
        flux_records['total_anomalies'] += 1 if reading < 30.0 or reading > base_threshold else 0

    # Distractor computation: unrelated to final result
    cumulative_drift = sum(abs(r - base_threshold) for r in sensor_readings) * adjustment_factor
    normalized_drift = cumulative_drift / len(sensor_readings) if sensor_readings else 0

    return flux_records, normalized_drift

# Core calculation function
def calculate_thermal_output(sequence):
    energy_states = [0] * len(sequence)
    decay_rate = 0.93
    boost_multiplier = 1.07
    temp_offset = 273.15  # Kelvin conversion reference (unused but plausible)

    for i, op_code in enumerate(sequence):
        base_energy = (i + 1) * 1.5
        if op_code % 4 == 0:
            energy_states[i] = base_energy * decay_rate
        elif op_code % 3 == 0:
            energy_states[i] = base_energy * boost_multiplier
        else:
            energy_states[i] = base_energy

    # Intermediate distractor variables
    average_state = sum(energy_states) / len(energy_states)
    peak_state = max(energy_states)
    state_variance = sum((x - average_state) ** 2 for x in energy_states) / len(energy_states)

    # Final output depends only on sum of transformed states
    transformed_sum = sum(x * 0.91 for x in energy_states if x > 1.8)
    return int(transformed_sum * 1.05)

# Simulated process sequence (deterministic input)
process_sequence = [4, 9, 12, 7, 8, 15, 6, 11]

# Irrelevant data structure - distractor
system_log = {
    'init_time': '2024-05-17',
    'mode': 'diagnostic',
    'version': 3.14,
    'active_sensors': set([1, 2, 3, 5, 8])
}

# Dummy sensor data used only for side function
sensor_data = [70.1, 82.3, 25.0, 77.6, 68.9, 91.2, 73.4, 29.8, 88.0]

# Execute monitoring (result not used in final answer)
flux_metrics, drift_value = monitor_temperature_flux(sensor_data)

# Key statement: this determines the answer
thermal_capacity = calculate_thermal_output(process_sequence)

# Print final result as required
print(f"Result: {thermal_capacity}")