def analyze_growth_potential(conditions):
    """Irrelevant analysis function (dead code path)"""
    score = 0
    for c in conditions:
        if c > 0.5:
            score += c * 2
    return score

# Distractor: Unused growth model parameters
growth_factors = [0.8, 1.2, 0.9, 1.5, 0.7]
baseline_cycles = 4
theoretical_max = 987654

# Real data: Climate index sequence (hidden pattern)
climate_data = [0.3, 0.7, 0.6, 0.8, 0.4]
soil_profiles = [
    {'ph': 6.5, 'moisture': 0.7, 'nutrients': 3},
    {'ph': 5.8, 'moisture': 0.5, 'nutrients': 2},
    {'ph': 6.2, 'moisture': 0.6, 'nutrients': 4}
]

# Decoy transformation with slicing (misleading intermediate)
def transform_readings(data):
    sliced = data[1:-1]
    normalized = [x * 100 for x in sliced]
    reversed_norm = normalized[::-1]
    return sum(reversed_norm)  # Not used in final result

# Hidden logic: nutrient threshold filter disguised in string processing
def extract_viable_zones(profiles):
    ph_levels = []
    for p in profiles:
        ph_str = f"{p['ph']:.1f}"
        if '6' in ph_str:  # Only include pH containing '6' digit
            ph_levels.append(p['ph'])
    return ph_levels

# Bit manipulation red herring
current_state = 0b1010
mask = 0b1100
shifted = (current_state & mask) << 2
status_flag = shifted | 0b0010

# Main computation chain (obfuscated by surrounding noise)
def compute_rainfall_effect(data):
    total = 0
    multiplier = 1
    for i, val in enumerate(data):
        if i % 2 == 0:
            total += val * 100
        else:
            multiplier *= val
    return int(total * multiplier)

# Critical distractor: complex-looking but unused mathematical transform
def calculate_entropy(arr):
    import math
    return sum(math.log(x + 1e-5) for x in arr) * -1.0

# Real logic buried in multiple steps
precipitation_index = compute_rainfall_effect(climate_data)
viable_soils = extract_viable_zones(soil_profiles)
base_yield = len(viable_soils) * precipitation_index

# Secondary filtering using string method distraction
diagnostic_codes = ['OK6', 'NG5', 'OK6', 'ERR', 'OK6']
valid_count = sum(1 for code in diagnostic_codes if code.startswith('OK'))

# Final optimization with hidden rounding logic
def optimize_harvest(climate, soils):
    raw_sum = sum(climate) * 1000
    adjustment = 0
    
    # Nested conditional decoy
    if len(soils) > 5:
        adjustment = 100
    elif len(soils) == 3:
        adjustment = -25
    else:
        adjustment = 50
    
    # Actual key calculation
    nutrient_total = 0
    for s in soils:
        nutrient_total += s['nutrients']
    
    # Critical step: integer division and comparison-based adjustment
    avg_nutrients = nutrient_total // len(soils)
    
    if avg_nutrients >= 3:
        modifier = 1.25
    else:
        modifier = 0.85
    
    # Apply modifier and subtract adjustment (misdirection)
    result = (raw_sum + base_yield) * modifier - abs(adjustment)
    
    # Final override based on string pattern match count
    if valid_count >= 3:
        result = result - 123  # Compensation factor
    
    return int(result)

# Execution point of interest
final_yield = optimize_harvest(climate_data, soil_profiles)

# Print result as required
print(f"Result: {final_yield}")