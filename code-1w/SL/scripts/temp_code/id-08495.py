from itertools import cycle

# Simulate water treatment plant filtration cycles
cycle_efficiency = [0.85, 0.91, 0.76, 0.94, 0.88]
duration_days = 7

# Generate daily efficiency over weekly cycle
efficiency_stream = [round(x, 2) for x in cycle(cycle_efficiency)]
daily_efficiencies = [efficiency_stream[i % len(efficiency_stream)] for i in range(duration_days)]

# Apply threshold filter: only high-efficiency days contribute to score
threshold = 0.87
filtered_cycles = [int(eff * 100) for eff in daily_efficiencies if eff >= threshold]

# Key computation point
filtration_score = sum(filtered_cycles)
print(f"Result: {filtration_score}")