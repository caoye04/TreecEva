from itertools import groupby
from math import log

# Simulate agricultural field data with noise and metadata
def generate_field_data():
    raw_readings = [
        (1, 20.5, 'A'), (2, 18.3, 'A'), (3, 22.1, 'A'),
        (1, 19.8, 'B'), (2, 20.9, 'B'), (3, 17.6, 'B'),
        (1, 21.0, 'C'), (2, 22.5, 'C'), (3, 19.4, 'C')
    ]
    
    # Add irrelevant calibration offsets
    calib_offsets = {'A': 0.3, 'B': -0.2, 'C': 0.1}
    adjusted = [(day, temp + calib_offsets[zone], zone) for day, temp, zone in raw_readings]
    
    # Misleading transformation: normalize temperatures (not used in final logic)
    max_temp = max(t for _, t, _ in adjusted)
    normalized = [(d, round(t / max_temp, 3), z) for d, t, z in adjusted]
    
    # Reconstruct original signal from normalized (dead code path)
    reconstructed = [(d, round(n * max_temp, 1), z) for d, n, z in normalized]
    
    return reconstructed

# Configuration with red herring parameters
class Config:
    def __init__(self):
        self.base_threshold = 19.5
        self.penalty_factor = 0.8
        self.bonus_multiplier = 1.2
        self.max_iter = 500  # unused parameter
        self.debug_mode = True  # misleading flag

config = Config()
field_data = generate_field_data()

# Auxiliary function that appears important but only used once
def filter_productive_days(data, threshold=20.0):
    return [entry for entry in data if entry[1] >= threshold]

# Dead utility: computes entropy of zone distribution (unused)
def compute_zone_entropy(data):
    zones = [z for _, _, z in data]
    freq = {z: zones.count(z) for z in set(zones)}
    total = len(zones)
    return -sum((count/total) * log(count/total) for count in freq.values())

# Real processing begins here
sorted_data = sorted(field_data, key=lambda x: x[2])  # sort by zone

# Group by zone and compute average temp per zone
zone_averages = {}
for zone, group in groupby(sorted_data, key=lambda x: x[2]):
    temps = [temp for _, temp, _ in group]
    avg_temp = sum(temps) / len(temps)
    zone_averages[zone] = round(avg_temp, 2)

# Compute deviation scores (some irrelevant)
deviations = {}
for zone, avg in zone_averages.items():
    dev = abs(avg - config.base_threshold)
    deviations[zone] = round(dev, 2)

# Track state across zones
productivity_flags = {}
temp_buckets = {'high': 0, 'medium': 0, 'low': 0}

for zone, avg in zone_averages.items():
    if avg > config.base_threshold + 1:
        productivity_flags[zone] = 'high'
        temp_buckets['high'] += 1
    elif avg < config.base_threshold - 1:
        productivity_flags[zone] = 'low'
        temp_buckets['low'] += 1
    else:
        productivity_flags[zone] = 'normal'
        temp_buckets['medium'] += 1

# Critical calculation function
def calculate_harvest_efficiency(data, cfg):
    # Recompute zone averages again (redundant but simulates state sync)
    sorted_data = sorted(data, key=lambda x: x[2])
    new_avgs = {}
    for zone, group in groupby(sorted_data, key=lambda x: x[2]):
        temps = [t for _, t, _ in group]
        new_avgs[zone] = sum(temps) / len(temps)
    
    # Base yield estimate
    base_yield = 0
    bonus_applied = False
    penalty_applied = False
    
    for zone, avg in new_avgs.items():
        if avg > cfg.base_threshold:
            base_yield += 10
            if not bonus_applied and productivity_flags[zone] == 'high':
                base_yield *= cfg.bonus_multiplier  # apply once only
                bonus_applied = True
        else:
            base_yield -= 2
            penalty_applied = True
    
    # Final adjustment based on bucket distribution (only uses counts)
    imbalance = abs(temp_buckets['high'] - temp_buckets['low'])
    if imbalance >= 2:
        base_yield *= 0.9
    
    # Apply penalty factor if any penalty was triggered
    if penalty_applied:
        base_yield *= cfg.penalty_factor
    
    return round(base_yield, 2)

# Execute critical statement
final_yield = calculate_harvest_efficiency(field_data, config)
print(f"Target result: {final_yield}")