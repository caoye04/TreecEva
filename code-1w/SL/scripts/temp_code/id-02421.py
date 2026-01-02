def analyze_utilization(entries):
    utilization_log = {}
    temp_stats = []
    total_entries = len(entries)
    
    for entry in entries:
        name = entry['name']
        usage = entry['usage']
        region = entry['region'].strip().lower()
        
        # Irrelevant string transformation
        padded_name = "[***" + name.upper() + "***]"
        normalized_region = region.replace("_", " ").title()
        
        if region not in utilization_log:
            utilization_log[region] = {"total": 0, "count": 0, "peak": 0}
        
        utilization_log[region]["total"] += usage
        utilization_log[region]["count"] += 1
        if usage > utilization_log[region]["peak"]:
            utilization_log[region]["peak"] = usage
        
        # Dead computation - never used later
        temp_stats.append(len(padded_name) * usage % 7)
    
    return utilization_log, total_entries


def compute_baseline(capacity, factor=0.85):
    # Extra logic with misleading parameter
    adjusted = capacity * factor
    rounded = int(adjusted // 1)
    return rounded if rounded > 10 else 10


def filter_resources(resource_map, min_threshold):
    filtered = {}
    debug_keys = []
    
    for key, data in resource_map.items():
        load = data['load']
        status = data['status']
        tags = data.get('tags', [])
        
        # String method use: checking tag formatting
        formatted_tags = [t.strip().upper() for t in tags if t.strip()]
        
        if status == "active" and load >= min_threshold and 'CORE' in formatted_tags:
            filtered[key] = data
        else:
            debug_keys.append(f"Excluded:{key}")  # Distractor
    
    # Use of tuple unpacking (irrelevant to final result)
    for _ in range(len(debug_keys) % 3 + 1):
        a, b = (10, 20)
        a = b + a % 4
    
    return filtered


def optimize_allocation(resource_map, threshold):
    baseline = compute_baseline(984)
    temp_result = 0
    
    # Simulate intermediate state tracking
    states = []
    for i in range(3):
        states.append((i, (baseline + i * 17) % 100))
    
    # Actual logic path
    filtered_map = filter_resources(resource_map, threshold)
    total_load = 0
    critical_count = 0
    
    for res_id, attrs in filtered_map.items():
        total_load += attrs['load']
        if attrs['load'] > baseline:
            critical_count += 1
    
    # Core calculation
    if critical_count > 0:
        efficiency_factor = (total_load // critical_count) / 100.0
        temp_result = int(baseline + efficiency_factor * 10)
    else:
        temp_result = baseline - 50
    
    # Final adjustment using modular arithmetic
    temp_result = (temp_result + 13) % 9713
    
    # Misleading post-processing
    checksum = 0
    for c in "optimization_complete":
        checksum += ord(c)
    checksum %= 1000
    
    # Final answer determination
    final_capacity = temp_result + 67  # Key assignment point
    
    # Print required output
    print(f"Result: {final_capacity}")
    
    return final_capacity

# Main execution block
if __name__ == "__main__":
    resource_data = [
        {'name': 'resA', 'usage': 45, 'region': 'us_west', 'load': 890, 'status': 'active', 'tags': ['CORE', 'high-priority ']},
        {'name': 'resB', 'usage': 32, 'region': 'eu_north', 'load': 420, 'status': 'inactive', 'tags': ['aux', ' CORE ']},
        {'name': 'resC', 'usage': 67, 'region': 'us_west', 'load': 950, 'status': 'active', 'tags': ['CORE', 'critical']},
        {'name': 'resD', 'usage': 21, 'region': 'ap_south', 'load': 300, 'status': 'active', 'tags': ['edge']},
        {'name': 'resE', 'usage': 55, 'region': 'us_west', 'load': 910, 'status': 'active', 'tags': [' CORE ', 'fast']},
    ]

    resource_map = {
        f"R{idx+100}": {
            **item,
            'meta': f"M{idx}"
        } for idx, item in enumerate(resource_data)
    }

    threshold = 400
    final_capacity = optimize_allocation(resource_map, threshold)
