from collections import defaultdict, Counter

# Simulate agricultural yield optimization across growth phases
def simulate_growth_cycle(baseline, stress_factors):
    temp_buffer = [0] * len(stress_factors)
    adjusted_yields = []
    cumulative_loss = 0

    for i, factor in enumerate(stress_factors):
        if factor > 7:
            temp_buffer[i] = baseline * 0.3
        elif factor > 4:
            temp_buffer[i] = baseline * 0.6
        else:
            temp_buffer[i] = baseline * 0.8

        # Irrelevant smoothing pass (distractor)
        smoothed = max(temp_buffer[i] - 5, baseline * 0.2)
        adjusted_yields.append(temp_buffer[i])

    return adjusted_yields


def calculate_risk_metrics(yields):
    above_threshold = 0
    risk_score = 0.0
    total = sum(yields)

    for y in yields:
        if y > 60:
            above_threshold += 1
            risk_score += y * 0.05
        else:
            risk_score += y * 0.02

    # Dead computation - not used later
    avg_yield = total / len(yields) if yields else 0
    normalized_risk = risk_score / (total + 1e-8)

    return above_threshold


def track_resource_allocation(phases):
    allocation_log = defaultdict(int)
    peak_usage = 0
    phase_names = ['germination', 'growth', 'flowering', 'maturation']

    for idx, units in enumerate(phases):
        phase_key = phase_names[idx % 4]
        allocation_log[phase_key] += units * 1.1
        if allocation_log[phase_key] > peak_usage:
            peak_usage = allocation_log[phase_key]

    # Unused summary (distractor)
    summary_counts = Counter(allocation_log.values())
    avg_allocation = sum(allocation_log.values()) / len(allocation_log)

    return len(allocation_log)


def harvest_results(phases):
    base_input = 50
    stress_levels = [8, 5, 3, 9, 6]
    
    # Core logic chain
    growth_outputs = simulate_growth_cycle(base_input, stress_levels)
    valid_phases_count = calculate_risk_metrics(growth_outputs)
    resource_bottlenecks = track_resource_allocation(phases)

    intermediate_total = sum(growth_outputs[:valid_phases_count])

    scaling_factor = 1.2 if resource_bottlenecks >= 3 else 0.9
    adjustment_offset = 10 if sum(phases) > 100 else 5

    # Final computation with multiple dependencies
    final_yield = int(intermediate_total * scaling_factor + adjustment_offset)

    # Additional misleading calculation (not affecting result)
    projected_surplus = (final_yield - 100) * 0.15 if final_yield > 100 else 0

    return final_yield

# Execution sequence
production_phases = [20, 30, 25, 35]
baseline_efficiency = 50
auxiliary_data = [1.1, 0.9, 1.2, 0.8]

# Trigger key statement
final_yield = harvest_results(production_phases)
print(f"Result: {final_yield}")