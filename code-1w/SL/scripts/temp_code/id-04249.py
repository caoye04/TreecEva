import itertools

# Domain: Agricultural yield modeling with sensor data filtering

def collect_sensor_readings():
    # Simulated sensor array readings (moisture levels)
    return [0.68, 0.72, 0.74, 0.65, 0.85, 0.91, 0.89, 0.63, 0.77]


def filter_outliers(readings, threshold=0.8):
    # Irrelevant helper: filters extreme values (not actually used in final path)
    return [r for r in readings if r <= threshold]


def calculate_base_index(vals):
    # Calculates vegetation index from sensor values
    avg = sum(vals) / len(vals)
    return avg * 100


def apply_growth_factor(index, factor=1.2):
    # Applies seasonal growth adjustment
    adjusted = index * factor
    if adjusted > 75:
        adjusted = 75 + (adjusted - 75) / 2  # Diminishing returns
    return adjusted

# Decoy function - looks important but unused
def simulate_rainfall_effect(base, days=7):
    result = base
    for _ in range(days):
        result *= 1.05
        if result > 90:
            result = 85
    return result

# Another red herring: complex but irrelevant combinatorics
def generate_field_zones(combinations=3):
    zones = ['north', 'south', 'east', 'west', 'center']
    return list(itertools.combinations(zones, combinations))

# Data transformation pipeline
processed_data = []
def preprocess_data(raw):
    global processed_data
    temp_store = []
    for val in raw:
        normalized = (val - 0.6) / 0.4  # Normalize to 0-1 scale
        if normalized < 0:
            normalized = 0
        elif normalized > 1:
            normalized = 1
        temp_store.append(normalized * 100)
    
    # Additional distraction: sorting and slicing that isn't used later
    sorted_vals = sorted(temp_store, reverse=True)
    trimmed = sorted_vals[1:-1]  # Remove extremes
    
    # Actual relevant processing
    mean_val = sum(temp_store) / len(temp_store)
    processed_data = [mean_val]

    # Dead code path: never executed but looks plausible
    if len(trimmed) == 0:
        processed_data = [0]

# Core calculation chain
def compute_stress_factor(data):
    # Environmental stress modeled from average moisture
    base = data[0]
    stress = 0
    if base < 65:
        stress = 15
    elif base < 70:
        stress = 8
    else:
        stress = 3
    return stress


def adjust_for_pests(stress_factor):
    # Pesticide efficacy reduces stress
    reduction = 5
    efficacy_rate = 0.7
    return stress_factor - (reduction * efficacy_rate)


def integrate_nutrient_levels(adj_stress):
    # Nutrient enrichment adds buffer
    return adj_stress - 2.5


def derive_resilience_score(integrated):
    # Resilience increases yield potential
    return max(0, 10 - integrated)


def calculate_final_multiplier(resilience):
    # Convert resilience to multiplicative factor
    return 1 + (resilience / 100)


def harvest_results(data):
    # Final aggregation function
    index = calculate_base_index(collect_sensor_readings())
    growth_applied = apply_growth_factor(index)
    
    # Critical execution point: begin actual dependency chain
    preprocess_data(collect_sensor_readings())
    stress = compute_stress_factor(processed_data)
    adjusted = adjust_for_pests(stress)
    integrated = integrate_nutrient_levels(adjusted)
    resilience = derive_resilience_score(integrated)
    multiplier = calculate_final_multiplier(resilience)
    
    # Final computation
    base_yield = 8400
    final_yield = int(base_yield * multiplier)  # Truncated to integer
    
    # Distractor: unused alternative calculation
    potential_max = base_yield * (1 + (10 / 100))
    if final_yield > potential_max:
        final_yield = int(potential_max)
        
    return final_yield

# Execute
result = harvest_results(processed_data)
print(f"Target result: {result}")