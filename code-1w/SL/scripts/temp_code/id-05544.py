def calculate_efficiency(base, load_factor, overhead):
    return (base * load_factor) - overhead

# System performance parameters
base_performance = 85.0
loads = [0.9, 1.0, 1.1, 0.8, 1.2]
overhead_costs = [5.2, 6.1, 7.3, 4.8, 8.0]

# Calculate efficiency under different conditions using list comprehension
efficiency_scores = [calculate_efficiency(base_performance, load, overhead) 
                         for load, overhead in zip(loads, overhead_costs)]

# Determine the highest efficiency rate achieved
optimal_rate = max(efficiency_scores)

# Output the result
print(f"Result: {optimal_rate}")