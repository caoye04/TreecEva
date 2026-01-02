def analyze_soil_composition(data):
    # Irrelevant function: analyzes soil but not used in final calculation
    ph_levels = [6.5, 7.2, 6.8, 7.0]
    nutrient_score = 0
    for val in ph_levels:
        nutrient_score += (val * 1.5) // 1
    return nutrient_score

def preprocess_growth_data(raw):
    # Dead code path: never called
    return [x ** 0.5 for x in raw if x > 0]

def calculate_harvest_efficiency(areas, cycles):
    # Core logic with distractors
    efficiency_map = {}
    temp_buffer = []
    offset = 3
    
    # Distractor: complex-looking but unused transformation
    decoy_matrix = [[i * j for j in range(len(areas))] for i in range(len(areas))]
    for i in range(len(decoy_matrix)):
        decoy_matrix[i][i] = offset ** 2

    # Real logic begins
    total_area = sum(areas)
    adjusted_cycles = [c + 0.5 for c in cycles]
    weighted_sum = 0
    
    # Using enumerate and zip as required
    for idx, (area, cycle) in enumerate(zip(areas, adjusted_cycles)):
        normalized = area / total_area
        contribution = normalized * (cycle ** 2)
        efficiency_map[idx] = round(contribution, 6)
        temp_buffer.append(contribution)
    
    # Intermediate decoy result
    avg_decoy = sum(decoy_matrix[0]) / len(decoy_matrix[0])
    
    # Key computation
    raw_yield = sum(temp_buffer) * 1000
    
    # Additional distraction: bitwise red herring
    magic_factor = (len(areas) << 2) ^ 7
    fake_correction = raw_yield & magic_factor  # Unused
    
    # Final adjustment with integer division and rounding
    final_yield = int(raw_yield // 1.07)  # Simulates transport loss
    
    # Decoy conditional that doesn't affect outcome
    if len(efficiency_map) > 10:
        final_yield *= 0.9
        
    return final_yield

# Main execution block
area_metrics = [120, 85, 200, 150, 95]
growth_cycles = [3, 4, 2, 5, 3]

# Irrelevant preprocessing
soil_analysis = analyze_soil_composition([1,2,3])
dummy_stats = [x % 4 for x in range(100)]  # Dead data

# Unused tuple unpacking
_, _, *rest = area_metrics

# Core call
final_yield = calculate_harvest_efficiency(area_metrics, growth_cycles)

# Output result as required
print(f"Result: {final_yield}")