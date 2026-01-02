def simulate_growth(base, cycles):
    growth_factor = 1.5
    decay_rate = 0.9
    temp_result = 0
    intermediate_values = []
    
    for cycle in range(cycles):
        if cycle % 2 == 0:
            base += base * growth_factor
        else:
            base -= base * (1 - decay_rate)
        
        # Distractor: tracking unused stats
        running_avg = base / (cycle + 1)
        intermediate_values.append(running_avg)

    return int(base)


def calculate_efficiency(input_val):
    efficiency = input_val * 0.75
    buffer_zone = efficiency * 0.1  # Unused in final logic
    return efficiency


def filter_outliers(data_list):
    data_set = set(data_list)
    min_val = min(data_set)
    max_val = max(data_set)
    cleaned = data_set - {min_val, max_val}
    return list(cleaned) if len(cleaned) > 0 else [min_val]


def harvest_results(cycle_logs):
    raw_output = sum(cycle_logs)
    adjusted_output = raw_output * 0.85
n    # Irrelevant transformation
    normalized = adjusted_output / (len(cycle_logs) or 1)
    
    # Key computation
    threshold = 500
    bonus_factor = 1.2 if adjusted_output > threshold else 1.0
    final_yield = adjusted_output * bonus_factor
    
    # Dead code branch (never executed due to fixed input)
    if False and len(cycle_logs) > 100:
        final_yield *= 0.95  # Would reduce yield, but not triggered
    
    return int(final_yield)

# Simulate agricultural production cycles
initial_input = 40
production_cycles = []
for i in range(3):
    cycle_yield = simulate_growth(initial_input + i * 10, 4)
    production_cycles.append(cycle_yield)

# Unrelated preprocessing step (distractor)
dummy_stats = [calculate_efficiency(x) for x in production_cycles]
dummy_stats = filter_outliers(dummy_stats)

# Critical statement
final_yield = harvest_results(production_cycles)

print(f"Result: {final_yield}")