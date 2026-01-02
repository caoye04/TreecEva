def analyze_efficiency(records):
    efficiency_scores = []
    for i, (input_units, output_units) in enumerate(records):
        base_efficiency = output_units / (input_units + 1e-5)
        adjustment_factor = (i + 1) / len(records)
        adjusted_score = base_efficiency * (1 + adjustment_factor)
        efficiency_scores.append(adjusted_score)

    return efficiency_scores


def filter_outliers(data, threshold=1.5):
    median_val = sorted(data)[len(data)//2]
    deviation = [abs(x - median_val) for x in data]
    mad = sorted(deviation)[len(deviation)//2]  # Median absolute deviation
    filtered = [x for x in data if abs(x - median_val) <= threshold * mad]
    return filtered


def calculate_optimal_yield(runs):
    raw_data = [(run[0], run[1]) for run in runs]
    temp_analysis = [run[0] * 0.8 + run[1] * 0.2 for run in runs]  # Irrelevant metric

    efficiencies = analyze_efficiency(raw_data)
    
    # Simulate sensor fluctuation compensation (partially irrelevant)
    compensated = []
    for idx, eff in enumerate(efficiencies):
        if idx % 2 == 0:
            compensated.append(eff * 0.95)
        else:
            compensated.append(eff * 1.05)
    
    cleaned = filter_outliers(compensated)
    
    # Dummy tracking variables (distraction)
    total_computations = 0
    intermediate_logs = []
    for x in cleaned:
        total_computations += 1
        intermediate_logs.append(f"Log-{x:.3f}")

    # Core logic: weighted average based on position
    weights = [i+1 for i in range(len(cleaned))]
    weighted_sum = sum(val * weight for val, weight in zip(cleaned, weights))
    total_weight = sum(weights)
    
    final_yield = weighted_sum / total_weight if total_weight else 0
    
    # Extraneous post-processing (no effect)
    if final_yield > 1.0:
        final_yield *= 0.9
    elif final_yield < 0.5:
        final_yield += 0.1

    return final_yield

# Main execution
production_runs = [
    (120, 98), (150, 110), (130, 102), (160, 115), (140, 107),
    (180, 120), (170, 118), (190, 125), (200, 130), (165, 112)
]

initial_stats = {"runs_count": len(production_runs), "total_input": sum(r[0] for r in production_runs)}
dummy_pairs = list(zip([r[0] for r in production_runs], [r[1] for r in production_runs]))
indexed_labels = [f"Run-{i}" for i in range(len(production_runs))]

final_yield = calculate_optimal_yield(production_runs)
print(f"Result: {final_yield}")