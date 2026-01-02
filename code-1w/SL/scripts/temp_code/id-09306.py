def analyze_growth_stage(plant_height, leaf_count):
    # Irrelevant helper function (dead code path)
    return leaf_count > 4 and plant_height > 15

def calculate_moisture_index(temp, humidity):  # Distractor function
    # Unused in final computation but looks important
    base = temp * 0.7
    adjusted = base + (humidity * 0.3)
    return round(adjusted, 2) if adjusted > 0 else 0.0

def compute_nutrient_score(n_level, p_level, k_level):
    # Another decoy calculation that seems critical but isn't used
    score = (n_level * 0.4) + (p_level * 0.3) + (k_level * 0.3)
    return max(score, 10)  # artificial floor

def filter_valid_entries(entries):
    # Filters out malformed data points (used)
    valid = []
    for e in entries:
        if isinstance(e, dict) and 'height' in e and 'leaves' in e:
            valid.append(e)
    return valid

def accumulate_biomass(data_list):
    total_mass = 0
    growth_factor = 1.65
    suppression_factor = 0.85
    
    # Simulate biomass accumulation with conditional logic
    for item in data_list:
        height = item['height']
        leaves = item['leaves']
        age = item.get('age', 30)
        
        # Core logic hidden among red herrings
        base_yield = height * leaves
        
        # Conditional expression (required language feature)
        modifier = (1.2 if age < 45 else 0.9) if height > 20 else (1.1 if leaves >= 6 else 0.8)
        
        adjusted_yield = base_yield * modifier * growth_factor
        
        # Suppression logic based on overcrowding (simulated)
        density_flag = item.get('density_flag', False)
        if density_flag:
            adjusted_yield *= suppression_factor
        
        total_mass += adjusted_yield
    
    return total_mass

def harvest_results(sensor_data):
    # High-level orchestrator with multiple distractions
    
    # Irrelevant preprocessing steps
    nutrient_levels = {'N': 18, 'P': 12, 'K': 22}
    temperature_readings = [23.5, 24.1, 22.7, 25.0]
    avg_temp = sum(temperature_readings) / len(temperature_readings)
    moisture_index = calculate_moisture_index(avg_temp, 68)  # unused later
    
    # Real work begins: clean and process agronomic data
    filtered_data = filter_valid_entries(sensor_data)
    
    # Secondary distractor: fake yield prediction
    dummy_prediction = compute_nutrient_score(**nutrient_levels)
    fallback_mode = False
    
    if len(filtered_data) == 0:
        return -1  # emergency exit (not triggered)
    
    # Accumulate actual biomass from valid plants
    raw_output = accumulate_biomass(filtered_data)
    
    # Final adjustment using conditional expression (second use)
    efficiency_rate = 0.91 if raw_output > 500 else 0.76
    final_yield = int(raw_output * efficiency_rate) if raw_output > 0 else 0
    
    # Decoy assignment to mislead tracking
    final_yield = final_yield + 50 if moisture_index > 20 else final_yield  # moisture_index always > 20
    
    # Return the key result
    return final_yield

# Main execution block
if __name__ == "__main__":
    # Simulated field sensor readings (some invalid)
    agronomic_data = [
        {'height': 25, 'leaves': 7, 'age': 40, 'density_flag': True},
        {'height': 18, 'leaves': 5, 'age': 50},
        {'height': 30, 'leaves': 8, 'age': 35},
        {'height': 22, 'leaves': 6, 'age': 42, 'density_flag': False},
        "invalid_entry",  # will be filtered out
        {'height': 16, 'leaves': 4, 'age': 33}  # low productivity
    ]
    
    # Extraneous variables to increase interference
    calibration_offset = 0.034
    control_sequence = [x**2 for x in range(5)]  # unused
    status_flags = {"synced": True, "validated": False, "finalized": None}
    
    # Key execution point
    final_yield = harvest_results(agronomic_data)
    
    # Output result as required
    print(f"Result: {final_yield}")