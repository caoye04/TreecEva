from itertools import compress, cycle

def analyze_system_load(base_units, threshold=75):
    # Irrelevant transformation: normalize units (not used in final result)
    normalized = [round(u / max(base_units) * 100, 2) for u in base_units]
    over_threshold = [val > threshold for val in base_units]
    high_load_indices = [i for i, ht in enumerate(over_threshold) if ht]
    return high_load_indices

# System capacity data across zones
capacities = [120, 150, 90, 200, 130]

# Simulate sensor readings and log usage patterns
raw_readings = "12,15,9,20,13"
usage_strings = raw_readings.split(',')
usage_ints = [int(x) * 10 for x in usage_strings]  # Convert to actual usage values

# Misleading redundancy: duplicate processing with no impact
usage_backup = [u + 5 for u in usage_ints]  # Offset for safety margin (never used)

# Construct detailed log with time slicing
timestamps = list(range(1001, 1001 + len(usage_ints)))
usage_log = {t: val for t, val in zip(timestamps, usage_ints)}

# Red herring: analyze load (called but result not used in final calculation)
analyze_system_load(capacities)

# Core logic disguised among distractions
def calculate_remaining(caps, logs):
    # Extract values in order
    log_values = list(logs.values())
    
    # Apply efficiency decay per unit (modular arithmetic)
    adjusted = []
    for i, cap in enumerate(caps):
        factor = (i + 1) % 3 + 1  # cycles: 2,3,1,2,3
        reduced = cap * (1 - 0.1 * (factor - 1))  # 10% drop per factor level
        adjusted.append(int(reduced))
    
    # Mask out entries where usage exceeds 140% of adjusted capacity (unrealistic surge)
    mask = [log_values[i] <= adjusted[i] * 1.4 for i in range(len(log_values))]
    filtered_caps = list(compress(adjusted, mask))
    
    # Final computation: sum remaining headroom
    total_used = sum(log_values)
    total_avail = sum(filtered_caps)
    
    # Secondary filter: if any usage event divisible by 7, reduce final capacity by 5%
    if any(v % 7 == 0 for v in log_values):
        total_avail = int(total_avail * 0.95)
    
    return total_avail - total_used  # Net free capacity

# Key assignment statement
final_capacity = calculate_remaining(capacities, usage_log)

# Output result
print(f"Result: {final_capacity}")