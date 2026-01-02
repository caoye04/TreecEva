def analyze_growth_patterns(data):
    results = {}
    for i, (zone, values) in enumerate(data.items()):
        avg = sum(values) / len(values)
        variance = sum((x - avg) ** 2 for x in values) / len(values)
        results[zone] = {'average': avg, 'variance': variance}
    
    # Distractor: unused transformation
    normalized = {k: [round(vi / max(vs), 2) for vi in vs] for k, vs in data.items()}
    return results


def calculate_harvest(regions, thresholds):
    total_yield = 0
    yield_map = {}
    
    # Simulate multi-step regional processing with distractors
    temp_storage = []
    for idx, (name, metrics) in enumerate(zip(regions.keys(), regions.values())):
        base = metrics.get('average', 0)
        var = metrics.get('variance', 0)
        
        # Real logic step 1: filter by threshold
        if base < thresholds['min_base']:
            continue
            
        # Real logic step 2: adjust by variance penalty
        adjusted = base - (var * 0.1)
        
        # Distractor: irrelevant list accumulation
        temp_storage.append({'zone': name, 'raw': base, 'penalty': var})
        
        # Real logic step 3: scaling factor based on index
        scale = 1 + (idx * 0.05)
        contribution = adjusted * scale
        
        yield_map[name] = contribution
        total_yield += contribution
    
    # Distractor: dead code path
    if len(temp_storage) > 100:
        fallback = sum(len(s) for s in str(temp_storage))
        return fallback

    # Real logic step 4: apply global multiplier
    bonus_factor = 1.1 if len(yield_map) >= 3 else 1.0
    total_yield *= bonus_factor
    
    # Real logic step 5: cap at upper bound
    total_yield = min(total_yield, 427.3)
    
    # Final assignment
    final_yield = round(total_yield, 2)
    return final_yield

# Main execution
sensor_data = {
    'north_field': [85, 90, 87, 89],
    'east_ridge': [76, 78, 77, 75],
    'west_meadow': [92, 94, 93, 95],
    'south_grove': [68, 70, 69, 71]
}

# Process growth characteristics (not directly used in final answer but plausible)
growth_stats = analyze_growth_patterns(sensor_data)

# Prepare region metrics using dictionary operations
regions = {}
for key, readings in sensor_data.items():
    avg_val = sum(readings) / len(readings)
    var_val = sum((x - avg_val) ** 2 for x in readings) / len(readings)
    regions[key] = {'average': avg_val, 'variance': var_val}

# Thresholds for filtering (only min_base is used)
thresholds = {
    'min_base': 75,
    'max_variance': 50  # Distractor: not actually enforced
}

# Key computation
final_yield = calculate_harvest(regions, thresholds)

# Output result
print(f"Result: {final_yield}")