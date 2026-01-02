def calculate_system_efficiency(ratios):
    efficiencies = []
    temp_offset = 0.5
    for i, ratio in enumerate(ratios):
        adjusted_ratio = ratio * (i + 1)
        efficiency = adjusted_ratio / (1 + abs(ratio - 0.5))
        efficiencies.append(round(efficiency, 3))
    
    # Irrelevant tracking variable (low interference)
    total_updates = len(efficiencies)
    
    peak_efficiency = max(efficiencies)
    return peak_efficiency

ratios = [0.2, 0.4, 0.6, 0.8, 1.0]
result = calculate_system_efficiency(ratios)
print(f"Result: {result}")