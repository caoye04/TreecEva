def analyze_thermal_efficiency(room_temperatures, threshold):
    above_threshold = [temp for temp in room_temperatures if temp > threshold]
    below_threshold = [temp for temp in room_temperatures if temp <= threshold]
    
    # Bitwise analysis of zone patterns (using index as identifier)
    zone_signature = 0
    for i, temp in enumerate(room_temperatures):
        if temp > threshold:
            zone_signature ^= i << 1
    
    # Irrelevant distraction: unused variable (minimal interference)
    max_temp = max(room_temperatures)
    
    # Efficient zones are those above threshold
    efficient_zones = set(above_threshold)
    inefficient_zones = set(below_threshold)
    
    # Score based on high-efficiency count and signature property
    temperature_score = len(efficient_zones) * (zone_signature % 7)
    
    # Key statement
    result = temperature_score + len(efficient_zones)
    
    return result

# Input data
temperatures = [22, 19, 24, 18, 25, 20]
limit = 21

# Execute function
final_output = analyze_thermal_efficiency(temperatures, limit)
print(f"Result: {final_output}")