def analyze_soil(reading):
    return sum(int(d) for d in str(reading)) % 4 == 0

def assess_rainfall(pattern):
    count = 0
    for p in pattern:
        if p > 20:
            count += 1
    return count > len(pattern) // 2

def calculate_harvest(regions):
    total_yield = 0
    temp_buffer = []
    efficiency_log = []
    
    for region in regions:
        base_value = region['soil']
        rainfall_data = region['rainfall']
        
        # Irrelevant transformation (distractor)
        transformed_data = [x * 1.5 for x in rainfall_data if x < 50]
        temp_buffer.extend(transformed_data)
        
        # Core logic begins
        if analyze_soil(base_value) and assess_rainfall(rainfall_data):
            peak_count = sum(1 for r in rainfall_data if r > 25)
            modifier = 1.8 if peak_count >= 3 else 1.2
            
            # Real yield calculation
            avg_rain = sum(rainfall_data) / len(rainfall_data)
            base_yield = (base_value * avg_rain) / 10
            adjusted_yield = base_yield * modifier
            
            # Bitwise adjustment based on region id (semi-relevant)
            region_id = region['id']
            if region_id & 1:
                adjusted_yield = adjusted_yield * 0.9  # Slight reduction for odd IDs
            
            total_yield += int(adjusted_yield)
            
            # Logging (distractor)
            efficiency_log.append({'region': region_id, 'yield': adjusted_yield})
        else:
            # Dead code path (mild red herring)
            dummy_calc = (base_value + len(rainfall_data)) // 3
            continue
    
    # Final aggregation with slicing distraction
    if len(temp_buffer) > 5:
        slice_avg = sum(temp_buffer[2:5]) / 3
        total_yield = int(total_yield - slice_avg + 5)  # Minor correction
    
    final_yield = total_yield * 2  # Final scaling
    return final_yield

# Main data setup
regions_data = [
    {
        'id': 101,
        'soil': 322,
        'rainfall': [18, 22, 35, 45, 28]
    },
    {
        'id': 102,
        'soil': 1234,
        'rainfall': [15, 20, 26, 30, 32, 40]
    },
    {
        'id': 103,
        'soil': 4444,
        'rainfall': [28, 33, 41, 27, 36]
    }
]

# Execution
final_yield = calculate_harvest(regions_data)
print(f"Result: {final_yield}")