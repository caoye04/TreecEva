from itertools import compress, cycle

# Simulate multi-stage industrial filtration process with diagnostic telemetry

def run_filtration_sequence(raw_input_stream):
    stage_temps = [25.0, 30.5, 35.7, 40.2, 45.0]
    pressure_decay = [0.98, 0.95, 0.92, 0.89, 0.85]
    sensor_noise = [0.001, -0.002, 0.0015, -0.0008, 0.003]

    # Irrelevant telemetry buffer (distractor)
    telemetry_log = []
    for i, temp in enumerate(stage_temps):
        noise_adjusted = temp + sensor_noise[i % len(sensor_noise)]
        telemetry_log.append(f'Stage {i}: {noise_adjusted:.3f}C')

    # Real processing begins here
    flow_rates = [80, 85, 90, 88, 83]
    retention_factors = [0.62, 0.68, 0.71, 0.67, 0.64]

    # Compute cumulative effective retention (core logic step 1)
    weighted_retention = 0
    total_flow = sum(flow_rates)
    for i, rate in enumerate(flow_rates):
        weighted_retention += (rate / total_flow) * retention_factors[i]

    # Simulate chemical degradation over cycles (core logic step 2)
    degradation_coefficient = 1.0
    for cycle in range(3):
        degradation_coefficient *= 0.97  # 3% loss per cycle

    base_purity = 0.92
    adjusted_purity = base_purity * degradation_coefficient

    # Phantom checksum calculation (red herring - looks important but unused)
    checksum = 0
    for val in retention_factors:
        checksum ^= int(val * 1000)
    checksum = (checksum + len(pressure_decay)) % 1000

    # Masked efficiency computation using zip and enumerate (core logic step 3)
    efficiency_multipliers = []
    for idx, (temp, press) in enumerate(zip(stage_temps, pressure_decay)):
        if idx % 2 == 0:
            efficiency_multipliers.append((temp / 100) * press)
        else:
            efficiency_multipliers.append((30 / temp) * (press ** 0.5))

    raw_process_score = 0
    for mult in efficiency_multipliers:
        raw_process_score += mult * 10

    # Secondary path: data transformation via itertools (distractor chain)
    expanded_flow = []
    flow_cycle = cycle(flow_rates)
    for _ in range(12):
        expanded_flow.append(next(flow_cycle) * 0.01)

    # Use compress to filter (irrelevant filtering - appears data-driven)
    mask = [i % 3 == 0 for i in range(len(expanded_flow))]
    filtered_expanded = list(compress(expanded_flow, mask))
    phantom_metric = sum(filtered_expanded) * 1.5  # Dead-end metric

    # Core chain resumes: calculate final yield components
    process_efficiency = raw_process_score / 10  # Normalize
    recovery_rate = weighted_retention * adjusted_purity

    # Critical assignment point
    filtration_yield = process_efficiency * recovery_rate

    # Post-calculation obfuscation (unused branches)
    if phantom_metric > 10:
        alternate_yield = (sum(retention_factors) / len(retention_factors)) * 100
    elif checksum > 500:
        alternate_yield = base_purity * 100
    else:
        # This branch is unreachable but looks like it might matter
        pass

    # Final output
    print(f'Result: {filtration_yield}')

    return filtration_yield

# Execute simulation
raw_stream_data = list(range(100, 600, 100))
result = run_filtration_sequence(raw_stream_data)