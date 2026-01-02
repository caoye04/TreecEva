def calculate_harvest_efficiency(areas, limit):
    total_yield = 0
    temp_buffer = []
    efficiency_flags = [False] * len(areas)
    cumulative_score = 0.0

    for i, (zone_id, yield_val) in enumerate(areas):
        if yield_val < limit:
            continue
        
        # Irrelevant string processing (distractor)
        zone_code = f"Z{str(zone_id).zfill(3)}"
        is_valid_zone = zone_code.startswith('Z') and len(zone_code) == 4
        
        # Real computation begins
        adjusted_yield = yield_val * 0.95  # Apply decay factor
        total_yield += adjusted_yield
        
        # Bitwise tracking (semi-relevant)
        cumulative_score ^= int(adjusted_yield) & 255
        
        efficiency_flags[i] = True
    
    # Secondary loop with zip - semi-distracting accumulation
    zone_ids, yields = zip(*areas)
    max_yield = max(yields)
    avg_yield = sum(yields) / len(yields)
    
    # Dead code: this list is never used
    outlier_zones = [z for z, y in areas if y > avg_yield * 1.5]
    
    # Actual final calculation (depends only on filtered total_yield)
    scaling_factor = 1.0 + (cumulative_score % 100) * 0.01
    final_yield = int(total_yield * scaling_factor)
    
    # Print required result
    return final_yield

# Main execution
area_data = [
    (101, 120), (102, 85), (103, 200), (104, 60), (105, 180)
]
threshold = 100

# Misleading pre-processing (irrelevant)
buffered_data = area_data[1:4]
sorted_data = sorted(buffered_data, key=lambda x: x[1], reverse=True)
duplicate_check = dict(zip(zone for zone, _ in area_data, range(len(area_data))))

final_yield = calculate_harvest_efficiency(area_data, threshold)
print(f"Result: {final_yield}")