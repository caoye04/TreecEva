def simulate_growth(factor, cycles):
    result = 1
    for i in range(cycles):
        result += factor * (i % 4) ** 1.5
    return result

# Irrelevant simulation: Atmospheric pressure effect (unused)
atm_pressure = [101.3, 102.1, 99.7, 100.5]
pressure_trend = sum(p * 0.01 for p in atm_pressure)

def calculate_resilience_score(stress_events):
    score = 100
    for event in stress_events:
        if event > 5:
            score -= 10
        else:
            score += 5
    return score

# Unused resilience computation
stress_tests = [3, 7, 2, 8]
score_result = calculate_resilience_score(stress_tests)

# Core data pipeline with relevant logic
baseline_inputs = [4, 6, 8, 7, 5]
adjusted_factors = [x * 0.7 + 2 for x in baseline_inputs]

# Distractor: Energy consumption model (not connected)
energy_log = {f'hour_{i}': val * 1.3 for i, val in enumerate(adjusted_factors)}
total_energy = sum(energy_log.values())

# Real processing begins here
processed_data = {}
for idx, (raw, adj) in enumerate(zip(baseline_inputs, adjusted_factors)):
    growth_cycle = simulate_growth(adj, raw)
    efficiency_ratio = (adj / raw) * 100
    processed_data[f'section_{idx}'] = {
        'input': raw,
        'adjusted': adj,
        'growth': growth_cycle,
        'efficiency': efficiency_ratio
    }

# Misleading intermediate aggregation (looks important but unused)
temp_aggregate = 0
for key, values in processed_data.items():
    temp_aggregate += values['growth'] * values['efficiency'] * 0.01

# Actual target computation path
def extract_viable_outputs(data_dict):
    viable = []
    for k, v in data_dict.items():
        if v['efficiency'] > 120 or v['growth'] > 100:
            viable.append(v['growth'] * 0.8)
        elif v['input'] % 2 == 0:
            viable.append(v['growth'] * 0.6)
        else:
            viable.append(v['growth'] * 0.4)
    return viable

filtered_yields = extract_viable_outputs(processed_data)

# Secondary transformation with red herring list comprehension
offsets = [i * 0.1 for i in range(len(filtered_yields))]
adjusted_yields = [y + offsets[j] for j, y in enumerate(filtered_yields)]

# Decoy function that looks like final step
def compute_financial_projection(yield_list):
    base = sum(y * 0.05 for y in yield_list)
    return base * 1.2

projected_revenue = compute_financial_projection(adjusted_yields)  # Unused

# True final computation
scaling_map = {i: 0.95 - i*0.05 for i in range(len(filtered_yields))}

scaled_outputs = []
for index, yield_val in enumerate(filtered_yields):
    scaling_factor = scaling_map.get(index, 0.7)
    scaled_outputs.append(yield_val * scaling_factor)

# Final accumulation using enumerate and dictionary lookup
final_yield = 0
for i, val in enumerate(scaled_outputs):
    adjustment = processed_data[f'section_{i}']['adjusted'] * 0.01
    final_yield += val + adjustment

# Correct output print
print(f"Result: {final_yield}")