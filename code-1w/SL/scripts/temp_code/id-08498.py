from collections import defaultdict

# Simulate hourly energy load for a microgrid over a day
time_slots = range(24)
base_load = [300 + (t - 12)**2 // 3 for t in time_slots]
solar_reduction = [max(0, 150 - abs(t - 15) * 10) for t in time_slots]

# Compute net load after solar contribution
net_load = [base_load[t] - solar_reduction[t] for t in range(24)]

# Track load history and anomalies
load_history = []
anomalies = defaultdict(int)
for hour, load in enumerate(net_load):
    if load > 400:
        anomalies['high'] += 1
    elif load < 200:
        anomalies['low'] += 1
    load_history.append(load)

# Critical operation: determine peak capacity required
peak_capacity = max(load_history)

# Additional system check (irrelevant to peak but adds minor interference)
stable_hours = sum(1 for x in net_load if 250 <= x <= 350)

print(f"Result: {peak_capacity}")