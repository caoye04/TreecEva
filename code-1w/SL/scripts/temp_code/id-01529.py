def compute_aggregate(values, multipliers):
    harmonic_sum = 0.0
    adjustment_factor = 1.5 if len(values) > 3 else 0.8
    
    for i, (val, mult) in enumerate(zip(values, multipliers)):
        inverse_val = 1 / val if val != 0 else 0
        weighted_inverse = inverse_val * mult
        harmonic_sum += weighted_inverse
    
    final_correction = adjustment_factor if sum(multipliers) > 10 else 1.0
    return (1 / harmonic_sum) * final_correction if harmonic_sum != 0 else 0

# Input data
demand_rates = [2, 4, 5, 8, 10]
weights = [1 / r for r in demand_rates]
factors = [i * 2 for i in range(len(demand_rates))]

# Irrelevant auxiliary variable (minimal distraction)
temp_debug_log = f"Processing {len(demand_rates)} entries"

# Key computation step
total_harmonic_weight = compute_aggregate(weights, factors)

print(f"Result: {total_harmonic_weight}")