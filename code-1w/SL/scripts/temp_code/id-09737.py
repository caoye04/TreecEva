import itertools

# Simulate environmental sensor data (irrelevant but plausible)
def collect_sensor_data():
    return [0.1 * i for i in range(10)]

# Misleading function: appears important but unused
def calculate_root_depth(temp, moisture):
    return (temp * 0.3) + (moisture * 0.7) - 5

# Decoy model calibration (dead code path)
def calibrate_model_v1(data):
    return sum(x ** 0.5 for x in data if x > 0.5)

def calibrate_model_v2(data):
    return sum(x ** 2 for x in data if x < 0.5)

# Real computation begins here — deeply nested and interwoven with distractions
def evaluate_stress_index(values):
    index = 0
    for i, val in enumerate(values):
        if i % 3 == 0:
            index += val * 1.1
        elif val > 0.4:
            index -= 0.5
    return round(index, 4)

# Core logic obscured by abstraction and red herrings
def apply_growth_factor(age, health_map):
    factor = 1.0
    adjustments = []
    for key, score in health_map.items():
        if 'nutrient' in key:
            factor *= (score / 100)
        elif 'pest' in key:
            factor *= (1 - (score / 100))
    return factor * (0.1 + age * 0.02)

# Primary transformation using itertools and zip (required features)
def generate_phenotype_sequence(bases):
    rotated = itertools.cycle(bases)
    shifted = [bases[(i+2) % len(bases)] for i in range(len(bases))]
    return [a + b for a, b in zip(rotated, shifted)][:len(bases)]

# High-nesting recursive function with pruning (short-circuit)
def predict_yield_recursive(stage, limit, buffer):
    if stage >= limit:
        return buffer * 1.5
    if buffer <= 0.1:
        return 0.1
    next_buffer = buffer - 0.05
    branches = []
    for _ in range(2):
        result = predict_yield_recursive(stage + 1, limit, next_buffer)
        if result > 0.5:  # short-circuit filter
            branches.append(result * 0.9)
    return sum(branches) if branches else buffer

# Distractor: complex-looking but unused bitwise operation
def encode_condition(state, level):
    return (state << 2) ^ (level & 7) | (state >> 1)

# Actual optimization logic buried among decoys
def optimize_harvest(climate, soil):
    # Step 1: process climate through misleading index
    stress = evaluate_stress_index(climate)
    
    # Step 2: use lambda for dynamic filtering (required feature)
    valid_soil = list(filter(lambda x: x > 30, soil))
    base_yield = sum(valid_soil) / 100.0
    
    # Step 3: simulate growth over time
    health_profile = {
        'nutrient_N': 85,
        'nutrient_P': 70,
        'pest_attack': 15
    }
    growth_factor = apply_growth_factor(3, health_profile)
    
    # Step 4: generate sequence (required: itertools + zip)
    seq = generate_phenotype_sequence([0.5, 0.7, 0.6])
    enhancement = seq[1]  # relevant extraction
    
    # Step 5: recursive prediction with modular arithmetic
    season_mod = len(climate) % 4
    projected = predict_yield_recursive(season_mod, 4, enhancement)
    
    # Step 6: final adjustment (this is where answer is determined)
    final = (base_yield * growth_factor * projected) + stress
    
    # Irrelevant bit operations for distraction
    metadata_flag = encode_condition(5, 3)
    metadata_flag = (metadata_flag ^ 10) >> 1
    
    return int(round(final * 100))  # deterministic integer output

# Main execution with hidden signal in noise
if __name__ == '__main__':
    # Sensor data collection (distractor)
    sensors = collect_sensor_data()
    
    # Real inputs
    climate_data = [0.8, 0.6, 0.9, 0.7, 0.5, 0.4, 0.6, 0.8]
    soil_quality = [45, 60, 30, 75, 20, 55]
    
    # Dead calibration calls (misleading intermediate results)
    v1_score = calibrate_model_v1(sensors)
    v2_score = calibrate_model_v2(sensors)
    
    # Key assignment
    final_yield = optimize_harvest(climate_data, soil_quality)
    
    # Print required result
    print(f"Result: {final_yield}")