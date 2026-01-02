def analyze_phase_stability(temp, pressure):
    stability_index = (temp * 0.73) + (pressure * 0.27)
    threshold = 450.0
    adjustment_factor = 1.0
    if temp > 600:
        adjustment_factor *= 0.9
    if pressure < 10:
        adjustment_factor *= 1.1
    return stability_index * adjustment_factor


def calculate_entropy_flow(rate, phase):
    base_entropy = len(phase) * rate * 0.03
    modifier = 1.0
    if 'vapor' in phase:
        modifier += 0.4
    elif 'liquid' in phase:
        modifier -= 0.2
    return base_entropy * modifier

# Simulate industrial thermal process
process_sequence = ['heating', 'condensation', 'vaporization', 'cooling']
temp_profile = [300, 550, 700, 400]
pressure_profile = [20, 15, 8, 25]
flow_rates = [120, 95, 110, 100]
phase_states = ['liquid', 'liquid', 'vapor', 'liquid']

total_diagnostic_score = 0
for i in range(len(process_sequence)):
    score = 0
    if temp_profile[i] > 500:
        score += 30
    if pressure_profile[i] < 12:
        score += 25
    if 'ation' in process_sequence[i]:
        score += 15
    total_diagnostic_score += score

diagnostic_flag = f"STATUS_{'CRITICAL' if total_diagnostic_score > 100 else 'NORMAL'}"

entropy_outputs = []
stability_metrics = []
for idx in range(len(process_sequence)):
    entropy_val = calculate_entropy_flow(flow_rates[idx], phase_states[idx])
    entropy_outputs.append(round(entropy_val, 3))
    
    stability_val = analyze_phase_stability(temp_profile[idx], pressure_profile[idx])
    stability_metrics.append(round(stability_val, 3))

    # Irrelevant tracking variables (distractors)
    temp_buffer = [t for t in temp_profile if t > 400]
    pressure_snapshot = {i: p for i, p in enumerate(pressure_profile)}

combined_weight = 0.0
for i in range(len(process_sequence)):
    if stability_metrics[i] > 400 and 'vapor' in phase_states[i]:
        combined_weight += entropy_outputs[i] * 0.6
    else:
        combined_weight += entropy_outputs[i] * 0.3

# Core calculation with string-based dispatch logic
method_key = ''.join([step[0] for step in process_sequence]).upper()  # 'HCVS'
scaling_vector = {
    'HCVS': 1.8,
    'HCSS': 1.5,
    'OTHER': 1.0
}

scale_factor = scaling_vector.get(method_key, scaling_vector['OTHER'])

auxiliary_checksum = 0
for char in method_key:
    auxiliary_checksum += ord(char) - ord('A')

# Key execution point
thermal_capacity = calculate_thermal_output(process_sequence)

# Dummy function to simulate modular design (only one path is relevant)
def calculate_thermal_output(seq):
    base = 0
    for i, step in enumerate(seq):
        if i % 2 == 0:
            base += len(step) * 10
        else:
            base += temp_profile[i] // 100
    
    # String method used meaningfully
    if ''.join(seq).count('a') > 5:
        base *= 2
    
    # Final adjustment based on control flow history
    flag_check = diagnostic_flag.lower().replace('_', '').startswith('status')
    if flag_check and scale_factor == 1.8:
        base += int(auxiliary_checksum * 0.5)
    
    return int(base * scale_factor)

print(f"Result: {thermal_capacity}")