from collections import defaultdict

# Simulate hourly system load over a workday
time_slots = ['09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00']
base_loads = [45, 67, 89, 95, 78, 83, 91, 76]

# Apply temperature-dependent scaling factor
temperatures = [22, 24, 26, 28, 27, 25, 23, 21]
temp_factor = [1 + (t - 25) * 0.02 for t in temperatures]

# Calculate adjusted load
efficiency_ratio = 0.95
load_history = [round(base_loads[i] * temp_factor[i] / efficiency_ratio) for i in range(len(base_loads))]

# Track capacity trends by hour category
load_by_period = defaultdict(list)
for i, slot in enumerate(time_slots):
    period_key = "morning" if slot < '12:00' else "afternoon"
    load_by_period[period_key].append(load_history[i])

average_morning_load = sum(load_by_period["morning"]) / len(load_by_period["morning"])
average_afternoon_load = sum(load_by_period["afternoon"]) / len(load_by_period["afternoon"])

# Identify peak operational capacity
peak_capacity = max(load_history)

# Output result
print(f"Result: {peak_capacity}")