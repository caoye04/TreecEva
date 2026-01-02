def preprocess_sensor_readings(readings):
    processed = {}
    for key, values in readings.items():
        if 'moisture' in key:
            processed[key] = [v * 0.95 for v in values if v > 0]
        elif 'temperature' in key:
            processed[key] = [v + 2 for v in values]
    return processed

# Irrelevant helper function (decoy)
def calculate_compression_ratio(data):
    total = 0
    for d in data:
        if isinstance(d, dict):
            total += len(d) * 2
        else:
            total += d // 3
    return total

def normalize_field_zones(zone_matrix):
    normalized = []
    for row in zone_matrix:
        new_row = []
        for val in row:
            if val > 100:
                new_row.append(100)
            elif val < 0:
                new_row.append(0)
            else:
                new_row.append(val)
        normalized.append(new_row)
    return normalized

def compute_growth_potential(zones, sensors):
    score = 0
    for i, zone in enumerate(zones):
        avg_zone = sum(zone) / len(zone)
        moisture_key = f'moisture_zone_{i+1}'
        if moisture_key in sensors:
            avg_moisture = sum(sensors[moisture_key]) / len(sensors[moisture_key])
            score += avg_zone * avg_moisture * 0.1
    return round(score, 4)

def filter_outliers(data_list):
    # Dead code path — never actually used
    mean_val = sum(data_list) / len(data_list)
    return [x for x in data_list if abs(x - mean_val) < 20]

def aggregate_nutrient_levels(nutrients):
    totals = {}
    for nutrient, levels in nutrients.items():
        totals[nutrient] = sum(levels)
    return totals

def simulate_irrigation_cycle(state_vector):
    result = []
    for s in state_vector:
        result.append((s * 1.1) % 90)
    return result

# Main data structures
agronomic_data = {
    'zone_map': [
        [85, 92, 76],
        [68, 94, 88],
        [77, 83, 90]
    ],
    'sensor_readings': {
        'moisture_zone_1': [30, 35, 0, 40],
        'moisture_zone_2': [25, -5, 38, 42],
        'temperature_zone_1': [20, 22],
        'temperature_zone_2': [19, 23]
    },
    'nutrient_levels': {
        'nitrogen': [12, 15, 10],
        'phosphorus': [8, 10, 12]
    },
    'historical_yields': [88, 91, 85, 87]
}

# Irrelevant transformations (distractors)
dummy_compression = calculate_compression_ratio([{'a':1}, {'b':2}, 150, 200])
temp_zones = normalize_field_zones(agronomic_data['zone_map'])
processed_sensors = preprocess_sensor_readings(agronomic_data['sensor_readings'])

# Unused aggregation (red herring)
nutrient_totals = aggregate_nutrient_levels(agronomic_data['nutrient_levels'])

# Simulated cycle with no downstream effect (dead computation)
irrigation_state = [70, 65, 80]
simulated_output = simulate_irrigation_cycle(irrigation_state)

# Core logic embedded within distractions
def harvest_results(data):
    zones = data['zone_map']
    sensors = preprocess_sensor_readings(data['sensor_readings'])
    
    # Step 1: Normalize zones
    normalized_zones = normalize_field_zones(zones)
    
    # Step 2: Compute growth potential using normalized data
    growth_score = compute_growth_potential(normalized_zones, sensors)
    
    # Step 3: Calculate average historical yield (rounded down)
    avg_historical = sum(data['historical_yields']) // len(data['historical_yields'])
    
    # Step 4: Extract valid moisture values from zone 1
    valid_moisture_z1 = [m for m in data['sensor_readings']['moisture_zone_1'] if m > 0]
    avg_moisture_z1 = sum(valid_moisture_z1) / len(valid_moisture_z1)
    
    # Step 5: Apply correction factor based on temperature count
    temp_count = len(data['sensor_readings']['temperature_zone_1']) + len(data['sensor_readings']['temperature_zone_2'])
    correction = 1 + (temp_count * 0.05)
    
    # Step 6: Combine components into base yield
    base_yield = (growth_score * 10) + avg_historical
    
    # Step 7: Adjust with moisture and correction
    adjusted_yield = base_yield * avg_moisture_z1 * correction
    
    # Step 8: Final transformation (integer truncation)
    final_yield = int(adjusted_yield)  # This is the key assignment
    
    return final_yield

# Execution point of interest
final_yield = harvest_results(agronomic_data)
print(f"Result: {final_yield}")