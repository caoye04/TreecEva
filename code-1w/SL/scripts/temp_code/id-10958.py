from itertools import compress, cycle

# Simulate industrial thermal process efficiency analysis
def analyze_efficiency(logs):
    uptime = sum([entry['duration'] for entry in logs if entry['status'] == 'active'])
    total = sum([entry['duration'] for entry in logs])
    return uptime / total if total > 0 else 0

def calculate_thermal_output(sequence):
    base_temp = 25.0
    pressure_coeff = 1.87
    decay_factor = 0.92
    transient_loss = 0.03

    # Irrelevant diagnostic counters (distractor variables)
    diag_cycles = 0
    system_warnings = []
    debug_trace = [0] * len(sequence)  # Unused tracking

    # Simulate fluctuating input conditions
    temp_fluctuations = [(i % 7 + 1) * 0.4 for i in range(len(sequence))]
    filtered_seq = [x for x in sequence if x > 2]  # Preprocessing step

    # Complex state tracking with slicing and cycling
    extended_cycle = list(cycle([0.1, -0.05, 0.2]))[:len(filtered_seq)]
    adjusted_inputs = [
        (val + temp_fluctuations[i]) * extended_cycle[i % len(extended_cycle)]
        for i, val in enumerate(filtered_seq)
    ]

    # Core thermal model
    accumulator = base_temp
    for i, adj in enumerate(adjusted_inputs):
        if i % 3 == 0:
            accumulator += adj * pressure_coeff
        elif accumulator > 30:
            accumulator -= transient_loss
        else:
            accumulator *= decay_factor

        # Dead code branch (never reached due to logic above)
        if accumulator < 0 and False:
            accumulator = 0.1

    # Secondary computation that looks important but isn't used
    peak_momentary_load = max(adjusted_inputs) * pressure_coeff if adjusted_inputs else 0
    stability_ratio = accumulator / (peak_momentary_load + 1e-5)

    # Final output calculation — depends only on accumulator
    thermal_output = int(accumulator * 100) / 100.0
    return thermal_output

# Main execution
process_log = [
    {'timestamp': 1001, 'duration': 120, 'status': 'active', 'mode': 'high'},
    {'timestamp': 1121, 'duration': 45, 'status': 'idle', 'mode': 'low'},
    {'timestamp': 1166, 'duration': 200, 'status': 'active', 'mode': 'high'},
    {'timestamp': 1366, 'duration': 30, 'status': 'error', 'mode': 'off'},
    {'timestamp': 1396, 'duration': 180, 'status': 'active', 'mode': 'med'}
]

input_sequence = [1, 4, 2, 5, 3, 6, 2, 4, 7]
efficiency = analyze_efficiency(process_log)
baseline_shift = efficiency * 10

# Key statement
thermal_capacity = calculate_thermal_output(input_sequence)

# Output result
print(f"Result: {thermal_capacity}")