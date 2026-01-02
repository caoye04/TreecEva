from itertools import compress, cycle

def analyze_soil_composition(elements):
    # Irrelevant analysis with red herring computations
    atomic_weights = {'N': 14, 'P': 31, 'K': 39, 'C': 12}
    total_weight = sum(atomic_weights.get(el, 0) * 2 for el in elements)
    normalized = total_weight / (len(elements) + 1)
    return normalized > 25

def validate_irrigation_pattern(pattern):
    # Distractor function: looks important but unused in final logic
    flow_rate = 0
    for i, status in enumerate(pattern):
        if status == 'active' and i % 2 == 0:
            flow_rate += 1.5
    return flow_rate

def calculate_crop_health(sensor_data):
    # Semi-relevant processing: used to set a condition but not directly impacting final yield
    readings = [x for x in sensor_data if x > 0]
    avg_reading = sum(readings) / len(readings) if readings else 0
    return 'healthy' if avg_reading > 50 else 'stressed'

def calculate_optimal_yield(parcel):
    size = parcel['size_acres']
    soil_type = parcel['soil']
    irrigation = parcel['irrigation_zones']
    sensors = parcel['health_sensors']
    
    # Key computation branch
    base_yield_per_acre = 120 if soil_type in ['loam', 'silt'] else 80
    
    # Apply health modifier from sensor data
    health_status = calculate_crop_health(sensors)
    health_modifier = 1.2 if health_status == 'healthy' else 0.7
    
    # Simulate seasonal adjustment using cycle from itertools
    seasonal_factors = list(compress([1.1, 0.9, 1.0, 1.2], cycle([1, 0])))  # Yields [1.1, 1.0]
    season_factor = seasonal_factors[0]  # Use first
    
    # Dummy filtering operation with string method
    valid_zones = [z.strip().lower() for z in irrigation if 'north' not in z.lower()]
    efficiency_bonus = 1.1 if len(valid_zones) >= 2 else 1.0
    
    # Intermediate irrelevant calculation
    total_flow_capacity = 0
    for zone in irrigation:
        if 'pump' in zone:
            total_flow_capacity += 10

    # Actual yield formula
    estimated_yield = size * base_yield_per_acre * health_modifier
    estimated_yield *= season_factor
    estimated_yield *= efficiency_bonus
    
    # Final adjustment based on soil composition (triggers actual dependency)
    elements_present = parcel.get('elements', [])
    if analyze_soil_composition(elements_present):
        estimated_yield *= 1.15
    
    # Red herring: unused variable
    projected_revenue = estimated_yield * 3.5
    
    # Final result
    final_yield = int(round(estimated_yield))
    return final_yield

# Main execution block
land_parcel = {
    'size_acres': 45,
    'soil': 'loam',
    'irrigation_zones': ['pump_north_a', 'valve_south_b', 'pump_east_c'],
    'health_sensors': [68, 72, 55, 0, 81],
    'elements': ['N', 'P', 'K', 'C', 'N']
}

final_yield = calculate_optimal_yield(land_parcel)
print(f"Result: {final_yield}")