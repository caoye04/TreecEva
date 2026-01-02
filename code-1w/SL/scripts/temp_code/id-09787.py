from collections import defaultdict, Counter

# Simulate agricultural yield prediction with noise filtering and data aggregation
def preprocess_sensor_readings(raw_readings):
    filtered = []
    avg = sum(raw_readings) / len(raw_readings)
    for val in raw_readings:
        if abs(val - avg) < 15:  # Filter out outliers
            filtered.append(val)
    return filtered

# Secondary unused function (distractor)
def calculate_rainfall_deviation(data):
    mean = sum(data) / len(data)
    deviation = sum(abs(x - mean) for x in data)
    return deviation  # Not used in final logic

# Core logic for yield estimation
def calculate_harvest_potential(regions):
    total_yield = 0
    region_contributions = defaultdict(float)
    
    for region_id, data in regions.items():
        # Extract sensor readings and soil quality
        sensors = data['sensors']
        soil_quality = data['soil_q']
        elevation = data['elevation']  # Unused distractor field
        
        # Preprocess sensor data
        clean_readings = preprocess_sensor_readings(sensors)
        base_yield = sum(clean_readings) / len(clean_readings)
        
        # Apply soil adjustment
        adjusted_yield = base_yield * (1 + 0.1 * soil_quality)
        
        # Track contribution per region (only some are used)
        region_contributions[region_id] = adjusted_yield
    
    # Aggregate only high-potential regions
    relevant_regions = {k: v for k, v in region_contributions.items() if k in {'R1', 'R3', 'R5'}}
    total_yield += sum(relevant_regions.values())
    
    # Additional logic: penalize over-reliance on single region
    counts = Counter(region_contributions.keys())
    penalty = 0.05 * len([v for v in region_contributions.values() if v > 80])
    total_yield -= penalty
    
    # Final adjustment based on distribution evenness
    values = list(relevant_regions.values())
    if len(values) > 1:
        variance = sum((x - sum(values)/len(values))**2 for x in values) / len(values)
        total_yield *= (1 - min(variance / 1000, 0.1))  # Small stabilizing factor

    return round(total_yield, 4)

# Simulated input data
raw_region_data = {
    'R1': {
        'sensors': [95, 102, 98, 110, 45, 100],  # 45 is outlier
        'soil_q': 7,
        'elevation': 120
    },
    'R2': {
        'sensors': [88, 90, 105, 87, 210, 89],   # 210 is outlier
        'soil_q': 6,
        'elevation': 95
    },
    'R3': {
        'sensors': [93, 96, 94, 100, 95],
        'soil_q': 8,
        'elevation': 110
    },
    'R4': {
        'sensors': [70, 160, 85, 80, 78],       # 160 is outlier
        'soil_q': 5,
        'elevation': 130
    },
    'R5': {
        'sensors': [97, 96, 98, 100, 99],
        'soil_q': 9,
        'elevation': 105
    }
}

# Misleading intermediate computation (distractor)
elevation_set = set(entry['elevation'] for entry in raw_region_data.values())
temp_correction_factor = sum(elevation_set) / 100

# Noise-only transformation (irrelevant)
distorted = [round(temp_correction_factor * (x + 2) / 3, 2) for x in elevation_set]

# Key execution point
final_yield = calculate_harvest_potential(raw_region_data)
print(f"Result: {final_yield}")