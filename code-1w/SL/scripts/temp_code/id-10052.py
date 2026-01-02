def compute_filtration_metrics(contaminants, cycles):
    total_weight = sum(contaminants)
    avg_efficiency = total_weight / len(cycles) if cycles else 0
    cycle_count = len(cycles)
    efficiency_log = [c / avg_efficiency for c in contaminants if avg_efficiency > 0]
    stable_cycles = [c for c in cycles if c >= 2]
    filtration_score = total_weight // (cycle_count + 1) if cycle_count >= 3 else round(avg_efficiency * 0.75)
    return filtration_score

contaminant_loads = [18, 24, 36, 42]
cycle_phases = [1, 3, 4]
result = compute_filtration_metrics(contaminant_loads, cycle_phases)
print(f"Result: {result}")