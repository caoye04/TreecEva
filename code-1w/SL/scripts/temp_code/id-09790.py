def analyze_efficiency(rates, thresholds):
    temp_log = []
    adjusted_rates = [r * 1.05 for r in rates if r > 0]
    filtered = [r for r in adjusted_rates if r >= thresholds[0]]
    
    # Irrelevant transformation (distractor)
    inverted_map = {i: 1.0 / (r + 1) for i, r in enumerate(adjusted_rates)}
    decay_weights = [0.9 ** i for i in range(len(adjusted_rates))]

    # Meaningful but obfuscated computation chain
    cumulative = 0
    growth_phases = []
    for i, rate in enumerate(filtered):
        if rate > thresholds[1]:
            cumulative += rate * 0.8
        elif rate > thresholds[2]:
            cumulative += rate * 0.6
        else:
            cumulative += rate * 0.3
        growth_phases.append(cumulative)

    # Dead code path (distractor)
    if len(growth_phases) > 100:
        smoothing_factor = 0.1
        growth_phases = [g * (1 - smoothing_factor) for g in growth_phases]

    # Core logic embedded with noise
    base_projection = [g * 1.2 for g in growth_phases]
    final_projection = []
    for val, idx in zip(base_projection, range(len(base_projection))):
        if idx % 2 == 0:
            final_projection.append(val + 5)
        else:
            final_projection.append(val - 3)

    # Secondary distractor: unused complex structure
    status_flags = {"stable": True, "overload": False}
    for v in final_projection:
        if v > 200:
            status_flags["overload"] = True
            break

    # Critical assignment mixed with red herrings
    outlier_mask = [abs(x - sum(final_projection)/len(final_projection)) < 10 for x in final_projection]
    cleaned_output = [final_projection[i] for i in range(len(final_projection)) if outlier_mask[i]]
    
    # Key data transformation
    optimized_output = []
    shift_value = len(cleaned_output) % 7
    for i, val in enumerate(cleaned_output):
        if i < shift_value:
            optimized_output.append(val * 0.9)
        else:
            optimized_output.append(val * 1.1)

    peak_capacity = max(optimized_output)

    # Unused debug print and irrelevant logging (distractor)
    debug_trace = [f"Step {j}: {val:.2f}" for j, val in enumerate(optimized_output)]
    log_entry = f"Analysis complete: {len(debug_trace)} entries"

    # Final red herring operation (dead code)
    hypothetical_scenario = [h * 0.75 for h in optimized_output if h > peak_capacity * 0.5]

    return peak_capacity

# Input data
rate_inputs = [120, 135, -5, 142, 130, 0, 150, 148, 132, 145]
threshold_levels = [100, 130, 120]

# Execution
result = analyze_efficiency(rate_inputs, threshold_levels)
print(f"Target result: {result}")