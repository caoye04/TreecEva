def analyze_pattern(sequence):
    return [i for i, x in enumerate(sequence) if x % 3 == 0]

# Irrelevant helper function (distractor)
def validate_timing(timestamps):
    if len(timestamps) < 5:
        return False
    avg = sum(timestamps) / len(timestamps)
    return avg > 100

# Another distractor: unused data transformation
def transform_data(entries):
    return [e * 1.5 for e in entries if e > 10]

# Efficiency calculation using lambda and set operations
efficiency_score = lambda x, base: (x ** 0.5) / base if x > 0 else 0

# Simulate resource distribution across zones
def generate_efficiency_map(zones, base_level):
    zone_ids = [z[0] for z in zones]
    raw_values = [z[1] for z in zones]
    scores = [efficiency_score(val, base_level) for val in raw_values]
    
    # Use zip and enumerate together (required feature)
    indexed_scores = list(enumerate(zip(zone_ids, scores)))
    
    # Distractor: create a set but don't use it directly in main logic
    unique_zone_prefixes = {z[:2] for z in zone_ids}
    temp_analysis = {idx: (zone, score) for idx, (zone, score) in indexed_scores}
    
    return {zone: scores[i] for i, (zone, _) in enumerate(zip(zone_ids, scores))}

# Core optimization logic with misleading intermediate steps
def optimize_allocation(resources, efficiency):
    allocation = {}
    remaining = resources
    adjustments = 0
    
    # Sorting by efficiency (descending) — relevant step
    sorted_zones = sorted(efficiency.keys(), key=lambda k: efficiency[k], reverse=True)
    
    # Dead code path: never executed due to constant condition (distractor)
    if len(allocation) > 100:
        fallback = sum(efficiency.values())
        adjustments += fallback

    # Actual allocation process
    for zone in sorted_zones:
        ideal = int(resources * efficiency[zone])
        capped = min(ideal, remaining)
        allocation[zone] = capped
        remaining -= capped
        
        # Red herring computation
        debug_ratio = capped / (ideal + 1e-8)
        adjustments += len(str(capped))  # meaningless accumulation

    # Secondary adjustment phase based on parity filtering (relevant)
    valid_allocations = {k: v for k, v in allocation.items() if v % 2 == 0}
    final_sum = sum(valid_allocations.values())
    
    # Use of set difference (required feature): irrelevant cleanup
    active_keys = set(allocation.keys())
    removed_keys = set(sorted_zones) - active_keys  # always empty
    adjustments += len(removed_keys)
    
    # Final capacity is only based on valid_allocations sum
    final_capacity = final_sum
    
    # Print required output format
    print(f"Result: {final_capacity}")
    return final_capacity

# Main execution block
if __name__ == "__main__":
    # Initialize system parameters (meaningful names from logistics domain)
    max_resources = 9876
    base_efficiency_level = 4.0
    
    # Zone configuration data
    operational_zones = [
        ('ZG11', 12), ('ZG12', 18), ('ZG13', 6), ('ZG14', 24),
        ('ZH21', 30), ('ZH22', 42), ('ZH23', 15), ('ZH24', 9)
    ]
    
    # Generate efficiency mapping
    efficiency_map = generate_efficiency_map(operational_zones, base_efficiency_level)
    
    # Irrelevant preprocessing (dead end)
    timestamps_log = [105, 110, 115, 120, 125]
    is_valid = validate_timing(timestamps_log)
    
    # More distraction: transform but never use
    sensor_readings = [5, 12, 15, 20, 25, 30]
    processed = transform_data(sensor_readings)
    
    # Key execution point
    final_capacity = optimize_allocation(max_resources, efficiency_map)