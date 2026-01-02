from itertools import cycle, islice

def simulate_growth(baseline, factors):
    adjusted = baseline
    temp_buffer = 0
    for factor in factors:
        if factor > 1.2:
            adjusted *= factor
        elif factor > 0.8:
            adjusted += 5
        else:
            adjusted -= 3
        temp_buffer += adjusted * 0.1
    return int(adjusted)

def evaluate_stability(metrics):
    mean_val = sum(metrics) / len(metrics)
    variance = sum((x - mean_val) ** 2 for x in metrics) / len(metrics)
    return variance < 15

def generate_factor_sequence(seeds):
    sequence = []
    for seed in seeds:
        if seed % 2 == 0:
            sequence.append(1.1 + seed * 0.05)
        else:
            sequence.append(0.95 - seed * 0.02)
    return sequence + [1.0] * (5 - len(sequence))

def harvest_results(cycles):
    total = 0
    peak_recorded = False
    peak_threshold = 120
    buffer_sum = 0

    base_factors = [1.5, 0.9, 1.3, 1.05]
    extended_cycle = list(islice(cycle(base_factors), 12))

    for i, cycle_chunk in enumerate([extended_cycle[n:n+3] for n in range(0, 12, 3)]):
        growth_rate = simulate_growth(i * 10 + 20, cycle_chunk)
        
        # Irrelevant stability check (does not affect output but adds cognitive load)
        dummy_metrics = [growth_rate, growth_rate + 5, growth_rate - 3]
        is_stable = evaluate_stability(dummy_metrics)
        
        if growth_rate > peak_threshold and not peak_recorded:
            growth_rate = int(growth_rate * 0.9)
            peak_recorded = True
            
        adjustment_factor = 1.1 if i % 2 == 0 else 0.95
        net_yield = growth_rate * adjustment_factor
        
        # Buffer accumulation (irrelevant to final result)
        buffer_sum += net_yield * 0.05
        
        total += int(net_yield)
        
    # Dead computation path: unused final adjustment
    if buffer_sum > 50:
        total -= 10

    return total

# Simulate agricultural production cycles
seeds_input = [2, 5, 3]
factors_used = generate_factor_sequence(seeds_input)
production_cycles = [factors_used[:4], factors_used[1:5], factors_used[2:], factors_used[:3]]

intermediate_score = sum(len(cycle) for cycle in production_cycles)  # Distractor variable
reference_map = {i: val for i, val in enumerate([10, 25, 18, 30])}  # Unused data structure

final_yield = harvest_results(production_cycles)
print(f"Result: {final_yield}")