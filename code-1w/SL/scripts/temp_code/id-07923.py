import math

# Irrelevant helper function (decoy)
def compute_noise(x):
    return (x ** 2 + 3 * x + 5) % 7

# Distractor data structure (unused in final calculation)
noise_cache = {i: compute_noise(i) for i in range(15)}

# Simulated regional agricultural data (relevant input)
regional_data = [
    {'id': 'A', 'soil_quality': 8, 'rainfall': 120, 'temperature': 24},
    {'id': 'B', 'soil_quality': 6, 'rainfall': 150, 'temperature': 26},
    {'id': 'C', 'soil_quality': 9, 'rainfall': 90,  'temperature': 22},
    {'id': 'D', 'soil_quality': 7, 'rainfall': 130, 'temperature': 25}
]

# Misleading intermediate calculation (dead path)
def deprecated_yield_model(data):
    total = 0
    for entry in data:
        if entry['soil_quality'] > 5:
            total += entry['rainfall'] // 10
    return total * 0.8  # Unused result

# Core logic with nested conditions and transformations
def assess_viability(entry):
    base_score = entry['soil_quality'] * 10
    if entry['rainfall'] < 100:
        adjustment = -15
    elif entry['rainfall'] > 140:
        adjustment = -10
    else:
        adjustment = 5
    
    # Temperature penalty if extreme
    if entry['temperature'] < 20 or entry['temperature'] > 27:
        adjustment -= 8
    
    return base_score + adjustment

# Higher-order function returning a lambda (relevant)
def get_multiplier(factor):
    return lambda x: x * factor if x > 0 else 0

# Unused but plausible transformation (red herring)
transform_rainfall = lambda r: int(math.log(r) * 10) if r > 0 else 0
transformed_rain = [transform_rainfall(d['rainfall']) for d in regional_data]

# Real processing pipeline
def calculate_sector_yield(sector):
    score = assess_viability(sector)
    
    # Apply dynamic multiplier based on quality tier
    if sector['soil_quality'] >= 8:
        mult = get_multiplier(1.25)
    elif sector['soil_quality'] >= 6:
        mult = get_multiplier(1.1)
    else:
        mult = get_multiplier(0.9)
    
    adjusted_yield = mult(score)
    
    # Conditional rounding based on rainfall parity
    if sector['rainfall'] % 2 == 0:
        adjusted_yield = math.floor(adjusted_yield)
    else:
        adjusted_yield = math.ceil(adjusted_yield)
    
    return adjusted_yield

# Orchestration function with early returns and filtering
def calculate_harvest(regions):
    valid_regions = []
    for r in regions:
        # Filter out invalid entries (all are valid here)
        if r['soil_quality'] <= 0:
            continue
        if r['rainfall'] <= 0:
            break
        valid_regions.append(r)
    
    if len(valid_regions) == 0:
        return 0
    
    # Compute individual yields
    yields = []
    for region in valid_regions:
        yield_val = calculate_sector_yield(region)
        yields.append(yield_val)
        
        # Early termination condition (never triggered - distraction)
        if yield_val > 1000:
            break
    
    # Final aggregation with weighted mean (integer division)
    total_weighted = sum(yields)
    num_regions = len(yields)
    
    # Integer division with rounding toward zero
    average_yield = int(total_weighted / num_regions)
    
    # Final adjustment based on global pattern
    if any(y > 90 for y in yields):
        final_bonus = 12
    else:
        final_bonus = 0
    
    return average_yield + final_bonus

# Spurious post-processing (irrelevant)
formatted_report = [f"{r['id']}:{assess_viability(r)}" for r in regional_data]
summary_hash = sum(len(s) for s in formatted_report) % 100

# Key execution point
final_yield = calculate_harvest(regional_data)

# Output the target result
print(f"Target result: {final_yield}")