from collections import defaultdict

# Simulate daily system load over a week in hourly intervals
daily_loads = [
    [0.3, 0.4, 0.6, 0.8, 1.2, 1.5, 1.7, 1.6, 1.4, 1.1, 0.9, 0.7],  # Mon
    [0.3, 0.5, 0.7, 0.9, 1.3, 1.6, 1.8, 1.7, 1.5, 1.2, 1.0, 0.8],  # Tue
    [0.4, 0.5, 0.8, 1.0, 1.4, 1.7, 1.9, 1.8, 1.6, 1.3, 1.1, 0.9],  # Wed
    [0.3, 0.6, 0.8, 1.1, 1.5, 1.8, 2.0, 1.9, 1.7, 1.4, 1.2, 1.0],  # Thu
    [0.5, 0.7, 0.9, 1.2, 1.6, 1.9, 2.1, 2.0, 1.8, 1.5, 1.3, 1.1]   # Fri
]

# Aggregate total load per day
daily_totals = defaultdict(float)
for i, loads in enumerate(daily_loads):
    for j, load in enumerate(loads):
        daily_totals[f'day_{i+1}'] += load

# Extract peak measurement from middle segment of Thursday (index 3)
daily_loads_sliced = daily_loads[3][4:8]  # Focus on high-activity window

# Calculate rolling average for stability analysis
rolling_avg = sum(daily_loads_sliced) / len(daily_loads_sliced)

# Determine peak capacity during critical period
peak_capacity = max(daily_loads_sliced)

# Print result for evaluation
print(f"Result: {peak_capacity}")