from collections import Counter

# Simulate daily energy consumption readings over a week (in kWh)
daily_readings = [18, 22, 18, 24, 27, 24, 20]

# Compute frequency of each consumption level
consumption_freq = Counter(daily_readings)

# Extract unique daily loads without duplicates while preserving order
daily_energy_loads = list(dict.fromkeys(daily_readings))

# Identify peak energy demand during the week
peak_demand = max(daily_energy_loads)

print(f"Target result: {peak_demand}")