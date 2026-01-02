def analyze_growth_cycle(phases):
    peak = max(phases)
    trough = min(phases)
    deviation = (peak - trough) / len(phases)
    return deviation > 0.5

# Irrelevant meteorological simulation
def simulate_rainfall(days):
    total = 0
    for d in range(days):
        if d % 7 == 0:
            total += d * 0.3
    return total

# Distractor function - unused but plausible
def calc_root_spread(depth, soil_type):
    spread = 0
    for i in range(1, depth + 1):
        if soil_type == 'clay':
            spread += i * 0.7
        else:
            spread += i * 1.2
    return spread

# Core logic with distractors embedded
def calculate_harvest(fluctuations, index):
    baseline = 100
    adjustment = 0
    stress_factor = 0
    temp_buffer = []

    for val in fluctuations:
        if val > 0:
            adjustment += val ** 0.5
        elif val < 0:
            adjustment -= abs(val) * 0.3
        
        # Red herring: accumulates values but mostly unused
        temp_buffer.append(val * 1.5 if val > 0 else val * 0.8)

    # Meaningful conditional expression using python idiom
    stress_factor = 2.5 if index > 6 else (1.8 if index > 3 else 1.1)

    # Real computation path
    raw_yield = baseline + adjustment
    
    # Multiple layers of logic
    if raw_yield > 120:
        raw_yield = 120 - (raw_yield - 120) * stress_factor
    elif raw_yield < 80:
        raw_yield = 80 + (80 - raw_yield) * (stress_factor / 2)
    
    # Decoy transformation
    transformed = [x * stress_factor for x in temp_buffer if x > 1]
    sum_transformed = sum(transformed)  # Unused distraction

    # Final adjustment based on cycle analysis (only called once)
    if analyze_growth_cycle(fluctuations):
        raw_yield *= 0.95
    
    final_yield = int(raw_yield)  # Critical assignment point
    
    return final_yield

# Simulated environmental data
fluctuations = [2.1, -1.3, 4.5, 0.2, -3.1, 5.0, -2.4, 1.8]
stress_index = 7

# Unused variables to increase interference
baseline_moisture = 65.4
optimal_ph = 6.8
seasonal_shift = True
rain_accum = simulate_rainfall(30)
root_depth = calc_root_spread(12, 'loam')

# Key execution point
final_yield = calculate_harvest(fluctuations, stress_index)

print(f"Result: {final_yield}")