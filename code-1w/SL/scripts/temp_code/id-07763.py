from collections import defaultdict

# Simulate hourly server load tracking across zones
load_data = [
    ('zone_a', 85), ('zone_b', 92), ('zone_c', 78),
    ('zone_a', 95), ('zone_b', 88), ('zone_c', 94),
    ('zone_a', 87), ('zone_b', 96), ('zone_c', 83)
]

# Aggregate peak loads per zone using defaultdict
zone_peaks = defaultdict(int)
for zone, load in load_data:
    if load > zone_peaks[zone]:
        zone_peaks[zone] = load

# Historical record of daily peak loads (name, value)
daily_records = [('Mon', 92), ('Tue', 96), ('Wed', 89)]

# Current day's simulated load history
load_history = daily_records + [('Thu', 94)]

# Determine the day with highest recorded load
peak_capacity = max(load_history, key=lambda x: x[1])

# Irrelevant auxiliary calculation (minor distraction)
total_zones = len(zone_peaks)
efficiency_ratio = round(sum(zone_peaks.values()) / total_zones, 2)

# Output target result
print(f"Result: {peak_capacity}")