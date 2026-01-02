def calculate_final_score(data):
    base_score = sum(data) * 0.8
    adjustment = len(data) > 5
    
    # Irrelevant computation - distractor
    temp_analysis = [x ** 0.5 for x in data if x > 10]
    avg_temp = sum(temp_analysis) / len(temp_analysis) if temp_analysis else 0
    
    # Real logic branch
    multiplier = 1.2 if all(x < 25 for x in data) else 0.9
    raw_score = base_score * multiplier
    
    # More distraction: unused transformation
    transformed = list(map(lambda y: y + 2 if y < 15 else y - 3, data))
    validity_check = ''.join([str(int(x % 2)) for x in transformed])
    
    # Actual score refinement
    if len(data) % 2 == 0:
        raw_score += 5
    else:
        raw_score -= 3
    
    # Final adjustment based on spread
    spread = max(data) - min(data)
    if spread > 20:
        raw_score *= 0.95
    
    return int(raw_score)

# Simulated sensor readings (core data)
sensor_readings = [12, 18, 7, 21, 5, 16]

# Preprocessing step with red herring operations
filtered_readings = [x for x in sensor_readings if x >= 5]
duplicates_removed = list(set(filtered_readings))
sorted_readings = sorted(duplicates_removed, reverse=True)

# Unused statistical analysis
mean_val = sum(sensor_readings) / len(sensor_readings)
variance_proxy = sum((x - mean_val) ** 2 for x in sensor_readings)

# Key processing with meaningful transformations
processed_data = [x + 1 for x in sorted_readings if x % 2 == 0]

# Critical execution point
final_score = calculate_final_score(processed_data)
print(f"Target result: {final_score}")