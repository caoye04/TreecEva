def analyze_soil_quality(readings):
    # Irrelevant helper: computes average pH (not used in final result)
    avg_ph = sum(r[1] for r in readings) / len(readings)
    return avg_ph

def extract_region_codes(locations):
    # Distractor function: processes location codes using slicing and string ops
    codes = [loc[2:5].upper() for loc in locations]
    frequency = {code: codes.count(code) for code in set(codes)}
    return frequency  # Never used

def calculate_harvest_efficiency(plots):
    total_yield = 0
    adjustment_factor = 0.85
    peak_threshold = 75
    
    # Real logic begins
    yields = [p['yield'] for p in plots if p['active']]
    sizes = [p['size_acres'] for p in plots]
    
    # Compute base efficiency using lambda filtering
    high_performers = list(filter(lambda y: y > peak_threshold, yields))
    
    # Semi-relevant computation: average yield of productive plots
    if yields:
        avg_yield = sum(yields) / len(yields)
    else:
        avg_yield = 0
    
    # Dead code path: uses string method on numeric context (never reached)
    status_msg = "Plots OK" if len(yields) > 5 else "Check sensors"
    log_entry = status_msg.replace(" ", "_").lower()  # unused
    
    # Core calculation with distraction
    size_based_bonus = 0
    for i, sz in enumerate(sizes):
        if sz > 10:
            size_based_bonus += 0.5 * (sz // 10)  # minor influence
    
    # Key step: counting character-like patterns in 'region_id'
    region_ids = [p['region_id'] for p in plots]
    char_count_map = {r: len(r) for r in region_ids}
    total_chars = sum(char_count_map.values())  # distractor
    
    # Actual key logic: min, max, and conditional adjustment
    if high_performers:
        performance_boost = len(high_performers) * 1.5
    else:
        performance_boost = 0
    
    base_total = sum(yields)
    adjusted_total = base_total * adjustment_factor
    
    # Final formula: only this matters
    final_yield = int(adjusted_total + performance_boost + size_based_bonus)
    
    # Red herring: complex slicing on sorted yields
    sorted_yields = sorted(yields)
    mid_segment = sorted_yields[1:-1]  # trimmed outliers
    smoothed = sum(mid_segment) / len(mid_segment) if mid_segment else 0  # unused
    
    return final_yield

# Main data setup
land_plots = [
    {'region_id': 'A12B', 'yield': 80, 'size_acres': 12, 'active': True},
    {'region_id': 'C34D', 'yield': 60, 'size_acres': 8, 'active': True},
    {'region_id': 'E56F', 'yield': 90, 'size_acres': 15, 'active': True},
    {'region_id': 'G78H', 'yield': 40, 'size_acres': 5, 'active': False},  # inactive
    {'region_id': 'I91J', 'yield': 85, 'size_acres': 20, 'active': True},
    {'region_id': 'K23L', 'yield': 30, 'size_acres': 10, 'active': True}
]

# Irrelevant pre-processing
soil_data = [('plot_1', 6.5), ('plot_2', 6.8), ('plot_3', 7.0)]
location_tags = ['xyA12', 'bcC34', 'deE56', 'fgG78', 'hiI91', 'jkK23']

_ = analyze_soil_quality(soil_data)
_ = extract_region_codes(location_tags)

# Critical execution point
final_yield = calculate_harvest_efficiency(land_plots)
print(f"Result: {final_yield}")