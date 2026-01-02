def calculate_efficiency(base, factor):
    return (base * factor) + 2

# System parameters for thermal energy calculation
temperature_readings = [32, 45, 67, 89, 101]
factor_sequence = [0.8, 1.1, 1.4, 0.9, 1.3]

# Irrelevant auxiliary variable (minor distraction)
status_flags = [True, False, True, False, True]

# Compute efficiency for each sensor reading using list comprehension and zip
efficiency_scores = [
    calculate_efficiency(temp, fac) 
    for temp, fac in zip(temperature_readings, factor_sequence)
]

# Determine which values are above threshold using enumerate
optimized_values = [
    score for i, score in enumerate(efficiency_scores) 
    if score > 50 and i % 2 == 0
]

# Final aggregation step
energy_output = sum(optimized_values)

print(f"Result: {energy_output}")