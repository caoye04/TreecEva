from functools import reduce

# Simulate agricultural yield optimization with noise and distractors
def analyze_soil_ph(levels):
    return list(map(lambda x: round(x * 1.07 + 0.3, 2), levels))


def compute_growth_index(temp_data, base_cycle):
    index = 0
    for t in temp_data:
        if t > 25:
            index += (t - 25) * 1.2
        elif t < 18:
            index -= (18 - t) * 0.8
    return index + base_cycle

# Distractor function - unused in final computation
def predict_market_demand(history):
    trend = sum(history) / len(history)
    return int(trend * 1.15)

# Core calculation with relevant logic chain
def calculate_harvest_efficiency(metrics, cycles):
    # Step 1: Extract key components
    raw_values = metrics['readings']
    mask = metrics['active_zones']
    
    # Step 2: Filter relevant zones using bitwise masking
    filtered = [raw_values[i] for i in range(len(raw_values)) if mask & (1 << i)]
    
    # Step 3: Apply nonlinear transformation
    adjusted = [v ** 0.9 for v in filtered]
    
    # Step 4: Aggregate using functional pattern
    total_input = reduce(lambda acc, val: acc + val, adjusted, 0)
    
    # Step 5: Normalize by cycle count with floor division
    normalized = total_input // cycles
    
    # Step 6: Apply efficiency curve (nonlinear scaling)
    if normalized > 40:
        efficiency = 85 + (normalized - 40) * 0.4
    else:
        efficiency = 60 + normalized * 0.625
    
    # Step 7: Round to nearest integer
    return int(round(efficiency))

# Irrelevant data structures and variables (distractors)
market_trends = [127, 134, 129, 142, 138]
demand_projection = predict_market_demand(market_trends)
soil_samples = [6.1, 6.3, 5.9, 6.0, 6.5]
pH_profile = analyze_soil_ph(soil_samples)

# Key input data
cluster_metrics = {
    'readings': [23, 45, 12, 67, 34, 56],
    'active_zones': 0b110101,  # bits determine which readings are active
    'calibration': 0.987
}

growth_cycles = 3

# Misleading intermediate calculations (dead code path)
temp_fluctuation = [-2, 1, 0, 3, -1]
bogus_index = compute_growth_index(temp_fluctuation, growth_cycles)
baseline_offset = sum([x for x in range(5)]) * 0.1

# Critical execution point
final_yield = calculate_harvest_efficiency(cluster_metrics, growth_cycles)

# Output result as required
print(f"Result: {final_yield}")