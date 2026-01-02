def analyze_productivity(x, y):
    if x < 2 or y > 10:
        return 0
    temp = (x * y) + 3
    adjustment = 1 if temp % 2 == 0 else -1
    return temp // 2 + adjustment

# Irrelevant utility function (dead code path)
def unused_calibrator(value):
    scale = 1.5
    offset = 0.7
    return (value * scale) + offset

# Decoy data structure with misleading values
decoy_metrics = {
    'peak': 999,
    'baseline': 120,
    'outlier_flag': True,
    'noise_floor': 42
}

# Real resource mapping with embedded logic
resource_map = {
    'sector_a': [3, 4, 5],
    'sector_b': [2, 6],
    'sector_c': [7]
}

# Efficiency tracking with red herring entries
efficiency_log = {
    'sector_a': 0.8,
    'sector_b': 0.9,
    'sector_x': 0.1,  # irrelevant sector
    'sector_y': 0.05, # irrelevant sector
    'calibration': 1.0 # decoy entry
}

# Phantom counter (distractor)
phantom_count = 0
for key in efficiency_log:
    if 'x' in key or 'y' in key:
        phantom_count += 1

# Simulated sensor drift (irrelevant computation)
sensor_drift = 0.0
for i in range(5):
    sensor_drift += (i * 0.01) % 0.05

# Core transformation logic
def process_sector_data(data, factor):
    total = 0
    for val in data:
        result = analyze_productivity(val, int(factor * 10))
        if result > 10:
            total += result
        else:
            total -= 1  # penalty for low yield
    return total

# Harvesting function containing key logic
def harvest_results(resources, log):
    aggregate = 0
    audit_trail = []
    
    for sector, values in resources.items():
        if sector not in log:
            continue
        raw_factor = log[sector]
        if raw_factor <= 0.75:  # filter threshold
            continue
        sector_value = process_sector_data(values, raw_factor)
        audit_trail.append(sector_value)
        
        # Early termination check (not triggered)
        if sector_value < 0:
            break
            unused_recovery = 1 # dead code
    
    # Final aggregation
    for idx, val in enumerate(audit_trail):
        if idx % 2 == 0:
            aggregate += val * (idx + 1)
        else:
            aggregate -= val
    
    # Final scaling based on non-trivial condition
    modifier = len(audit_trail) if sum(audit_trail) > 30 else 1
    return int(aggregate * modifier * 0.5)  # deterministic rounding

# Secondary decoy processing chain
shadow_copy = dict(resource_map)
for k in shadow_copy:
    shadow_copy[k].append(999)  # noise injection

# Trigger execution
temp_cache = []
for sec, vals in resource_map.items():
    temp_cache.extend(vals)

# Actual target computation
final_yield = harvest_results(resource_map, efficiency_log)

# Output result as required
print(f"Result: {final_yield}")