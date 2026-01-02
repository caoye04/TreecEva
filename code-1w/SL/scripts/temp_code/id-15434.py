from collections import defaultdict

# Simulate a multi-stage industrial process with quality control and resource tracking
def calculate_process_yield():
    raw_input_batch = [84, 92, 77, 63, 96, 88, 75, 60]
    rejection_threshold = 70
    processed_units = []
    rejected_count = 0

    # Initial filtering and transformation
    for unit in raw_input_batch:
        if unit < rejection_threshold:
            rejected_count += 1
            continue
        processed_units.append(unit ** 0.5 * 1.2)  # Normalize and scale

    # Misleading secondary computation (irrelevant to final result)
    avg_rejected_severity = sum([x for x in raw_input_batch if x < rejection_threshold])
    if avg_rejected_severity > 0:
        avg_rejected_severity /= max(rejected_count, 1)

    # Resource allocation simulation (partially relevant)
    resource_pool = defaultdict(int)
    for i, val in enumerate(processed_units):
        resource_pool[f'phase_{i % 3}'] += val * 0.7

    total_resource_utilization = sum(resource_pool.values())
    baseline_efficiency = len(processed_units) / len(raw_input_batch)

    # Dummy optimization pass (dead code - not used later)
    optimized_units = [u * 1.1 for u in processed_units if u > 9.0]
    peak_concentration = len([u for u in processed_units if u > 10.0])

    # Core calculation chain
    cumulative_stability = 0
    for i in range(len(processed_units)):
        cumulative_stability += processed_units[i] * (i + 1)

    system_load = cumulative_stability / (len(processed_units) + 1)
    net_outcome = int(system_load // 1.5)

    # Efficiency degradation model
    degradation_coefficients = [0.98, 0.95, 0.90, 0.85, 0.80]
    efficiency_factor = 1.0
    for d in degradation_coefficients:
        efficiency_factor *= d
        if efficiency_factor < 0.75:
            efficiency_factor += 0.05  # Stabilization threshold

    # Final computation (target statement)
    final_yield = net_outcome * efficiency_factor

    # Extraneous logging output (no impact)
    diagnostic_trace = [f"Step_{i}: {val:.2f}" for i, val in enumerate(resource_pool.values())]

    return final_yield

result = calculate_process_yield()
print(f"Target result: {result}")