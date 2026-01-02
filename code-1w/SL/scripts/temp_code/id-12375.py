from collections import defaultdict
import itertools

# Simulate hourly network load across multiple servers over a week
time_slots = list(itertools.product(range(7), range(24)))  # (day, hour)
servers = ['alpha', 'beta', 'gamma', 'delta']

# Track total usage per time slot across all servers
usage_log = defaultdict(lambda: defaultdict(int))
baseline_load = 50
fluctuation_factor = 1.2
penalty_threshold = 85

# Initialize tracker for peak identification
daily_peak = {}
server_stress_test = {s: 0 for s in servers}
phantom_load = 0  # Distractor: accumulates irrelevant test data

for day, hour in time_slots:
    daily_total = 0
    hourly_deviation = (hour ** 0.5) * fluctuation_factor
    if hour in [8, 9, 17, 18]:  # Commute times: higher usage
        hourly_deviation *= 1.8

    for server in servers:
        base_usage = baseline_load + hourly_deviation
        if server == 'beta':
            base_usage += 10  # Higher baseline capacity
        elif server == 'gamma' and day % 2 == 0:
            base_usage -= 5  # Maintenance dip

        # Simulated packet loss correction increases effective load
        corrected_load = int(base_usage * 1.08)

        # Record usage per server per time slot
        usage_log[(day, hour)][server] = corrected_load
        daily_total += corrected_load

        # Stress tracking (semi-relevant but not used in final answer)
        if corrected_load > penalty_threshold:
            server_stress_test[server] += 1

    # Log daily peak per hour (distractor computation)
    if day not in daily_peak:
        daily_peak[day] = 0
    daily_peak[day] = max(daily_peak[day], daily_total)

    # Phantom accumulation (dead-end logic)
    phantom_load += len([x for x in usage_log[(day, hour)].values() if x > 80])

# Aggregate total usage per server over the week (irrelevant to peak capacity)
total_per_server = defaultdict(int)
for key, loads in usage_log.items():
    for srv, val in loads.items():
        total_per_server[srv] += val

# Compute average hourly load across days (distractor)
avg_hourly = defaultdict(float)
hourly_count = defaultdict(int)
for (day, hour), loads in usage_log.items():
    total_load = sum(loads.values())
    avg_hourly[hour] += total_load
    hourly_count[hour] += 1

for h in avg_hourly:
    avg_hourly[h] /= hourly_count[h]

# Core metric: track maximum concurrent usage in any time slot
usage_tracker = defaultdict(int)
for (day, hour), loads in usage_log.items():
    usage_tracker[(day, hour)] = sum(loads.values())

# Critical statement: find peak system-wide capacity demand
peak_capacity = max(usage_tracker.values())

# Final distractor: normalize peak relative to average
average_peak_ratio = peak_capacity / sum(avg_hourly.values()) * 24 / 7

print(f"Result: {peak_capacity}")