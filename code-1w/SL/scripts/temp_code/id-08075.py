def analyze_phase_transition(energy_levels):
    # Irrelevant transformation
    normalized = [e * 1.05 for e in energy_levels if e > 0]
    threshold = sum(normalized) / len(normalized) if normalized else 0

    # Distractor: unused data structure
    phase_map = {i: 'solid' if e < threshold else 'liquid' for i, e in enumerate(energy_levels)}

    # Red herring computation
    cumulative = 0
    for val in energy_levels:
        if val % 2 == 0:
            cumulative += val ** 0.5  # Not used later

    # Relevant logic: count transitions above critical point
    critical_count = sum(1 for e in energy_levels if e > 75)
    return critical_count


def transform_metrics(raw_data):
    # Unrelated data processing
    squared = [x**2 for x in raw_data]
    offset = max(squared) - min(squared)
    adjusted = [x - offset//2 for x in squared]

    # Dead code path
    if len(adjusted) > 100:
        return [x for x in adjusted if x > 0]

    # Real operation disguised among noise
    result_set = set(adjusted)
    filtered = [x for x in raw_data if x in result_set]

    return len(filtered) if filtered else 1


def calculate_thermal_output(stages):
    base = 0
    multipliers = {'startup': 1.2, 'stable': 1.8, 'decay': 0.5}
    stage_efficiency = []

    for stage in stages:
        # Nested logic with distractors
        if stage['type'] == 'startup':
            base += stage['input'] * 0.3
            efficiency = stage['input'] * multipliers['startup']
            stage_efficiency.append(efficiency)

            # Misleading intermediate that looks important
            temp_adj = efficiency * 0.1
            base -= temp_adj  # Net zero effect due to compensation below
            base += temp_adj

        elif stage['type'] == 'stable':
            # Real contribution
            base += stage['input'] * 0.6
            stage_efficiency.append(stage['input'] * multipliers['stable'])

            # Unused complex calculation
            history_log = [{'val': base / (i+1)} for i in range(len(stage_efficiency))]

        elif stage['type'] == 'decay':
            decay_value = stage['input'] * 0.1
            base -= decay_value
            stage_efficiency.append(decay_value * multipliers['decay'])

    # Core answer computation hidden in multiple steps
    avg_efficiency = sum(stage_efficiency) / len(stage_efficiency) if stage_efficiency else 0
    adjustment_factor = len([e for e in stage_efficiency if e > 40])

    # Final result derived from non-obvious combination
    final_output = int(base * 10 + avg_efficiency - adjustment_factor * 2)

    # Decoy output variables
    theoretical_max = max(stage_efficiency) * len(stages)
    system_loss = sum(stage_efficiency) * 0.05

    return final_output

# Main execution flow
if __name__ == '__main__':
    # Input data setup
    process_stages = [
        {'type': 'startup', 'input': 50},
        {'type': 'stable', 'input': 80},
        {'type': 'stable', 'input': 90},
        {'type': 'decay', 'input': 30}
    ]

    energy_readings = [60, 85, 70, 95, 40]
    sensor_data = [12, 15, 10, 20]

    # Irrelevant preprocessing
    transition_count = analyze_phase_transition(energy_readings)
    metric_score = transform_metrics(sensor_data)

    # Key computation
    thermal_capacity = calculate_thermal_output(process_stages)

    # Additional distractions
    diagnostics = {
        'readings_processed': transition_count,
        'metrics_evaluated': metric_score,
        'anomalies': 0
    }

    # Output only the target variable
    print(f"Result: {thermal_capacity}")