from itertools import compress, cycle

def analyze_growth_cycles(plots):
    # Irrelevant helper: simulates sensor noise (not used in final result)
    noise_pattern = [x % 3 for x in range(len(plots))]
    filtered = [p for p, n in zip(plots, noise_pattern) if n != 2]
    return sum(filtered) // len(filtered) if filtered else 0

def calculate_harvest_efficiency(data, limit):
    base_rates = [d[1] for d in data]
    locations = [d[0] for d in data]
    
    # Intermediate distractor computation: average with padding
    padded_avg = (sum(base_rates) + 10) / (len(base_rates) + 1)
    adjustment_factor = 0.9 if padded_avg > limit else 1.0
    
    # Real logic begins: detect sustained yield sequences
    streak = 0
    max_streak = 0
    efficiency_counter = 0
    
    for i, rate in enumerate(base_rates):
        if rate >= limit:
            streak += 1
            efficiency_counter += 1
        else:
            if streak > max_streak:
                max_streak = streak
            streak = 0
    
    if streak > max_streak:
        max_streak = streak
    
    # Use enumerate and conditional expression
    modifiers = [(i+1)*0.1 if rate < limit else 0.05 for i, rate in enumerate(base_rates)]
    total_modifier = sum(modifiers)
    
    # Secondary distractor: simulate wind impact (unused)
    wind_factors = list(zip([0.98]*len(base_rates), cycle([1.02, 0.99])))
    
    # Key computation
    raw_yield = sum(base_rates) * adjustment_factor
    final_yield = int(raw_yield - total_modifier * 100)
    
    # Early return not taken (dead path)
    if False:
        return analyze_growth_cycles(data)
        
    return final_yield

# Main execution
field_coords = ['A1', 'B2', 'C3', 'D4', 'E5']
growth_data = [85, 92, 88, 76, 95]
status_flags = [True, True, False, True, True]

# Assemble field data using zip and filtering
field_data = list(zip(field_coords, growth_data, status_flags))
field_data = [(loc, val) for loc, val, active in field_data if active]  # Filter inactive

threshold = 80

# Dummy tracking variables (distractors)
cycle_count = len(growth_data)
total_energy_input = cycle_count * 15
baseline_projection = sum(growth_data) / len(growth_data)

final_yield = calculate_harvest_efficiency(field_data, threshold)

print(f"Result: {final_yield}")