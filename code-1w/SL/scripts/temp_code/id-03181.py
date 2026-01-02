from collections import defaultdict

# Simulate industrial thermal process with state tracking
def analyze_process_state(sequence):
    state_log = defaultdict(int)
    temp_accumulator = 0
    cycle_count = 0
    spike_detected = False

    for step in sequence:
        phase_id = step['phase']
        temperature = step['temp']
        duration = step['duration']

        # Irrelevant logging (distractor)
        state_log[phase_id] += 1
        
        # Real computation branch
        if temperature > 450 and not spike_detected:
            spike_detected = True
            temp_accumulator += 120

        if duration > 10:
            temp_accumulator += duration * 1.5

        # Dead code path (distractor)
        if phase_id == 'Z99':
            adjustment_factor = 0.0
            temp_accumulator -= adjustment_factor  # No effect

        cycle_count += 1

    # Secondary irrelevant aggregation
    avg_cycle_weight = sum(state_log.values()) / len(state_log) if state_log else 0
    return temp_accumulator, cycle_count, avg_cycle_weight

# Misleading helper function with unused logic
def estimate_pressure_rise(steps):
    total_rise = 0
    for s in steps:
        if 'pressure' in s:
            total_rise += s['pressure'] * 0.3
    return total_rise  # Never used in main flow

# Core calculation with key logic
def calculate_thermal_output(process_sequence):
    base_score = 0
    high_temp_bursts = 0

    for entry in process_sequence:
        temp = entry['temp']
        if temp > 500:
            high_temp_bursts += 1

    # Key accumulation step
    raw_energy = sum([s['temp'] * s['duration'] for s in process_sequence])
    efficiency_dampener = 0.8 if high_temp_bursts > 2 else 1.0

    intermediate_hold = raw_energy / (len(process_sequence) + 1)
    processed_signal = str(intermediate_hold).replace('.', '')
    signal_sum = sum(int(d) for d in processed_signal if d.isdigit())

    # Final result built from mixed sources
    base_score += intermediate_hold * 0.7
    base_score += signal_sum * 0.3
    base_score -= high_temp_bursts * 5

    return int(base_score)

# Main execution
if __name__ == '__main__':
    # Process data definition
    process_data = [
        {'phase': 'A1', 'temp': 300, 'duration': 5},
        {'phase': 'B2', 'temp': 520, 'duration': 12},
        {'phase': 'A1', 'temp': 480, 'duration': 8},
        {'phase': 'C3', 'temp': 560, 'duration': 15},
        {'phase': 'B2', 'temp': 470, 'duration': 7},
        {'phase': 'C3', 'temp': 510, 'duration': 10},
        {'phase': 'D4', 'temp': 580, 'duration': 6}
    ]

    # Irrelevant preprocessing (distractor)
    pressure_total = estimate_pressure_rise(process_data)
    normalized_phases = [p['phase'].lower() for p in process_data]
    phase_counter = defaultdict(int)
    for ph in normalized_phases:
        phase_counter[ph] += 1

    # State analysis (semi-relevant but not used in final answer)
    _, cycles, _ = analyze_process_state(process_data)

    # Critical statement
    thermal_capacity = calculate_thermal_output(process_data)
    
    print(f"Result: {thermal_capacity}")