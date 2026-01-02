import itertools

def preprocess_constraints(bounds):
    adjusted = []
    for x in bounds:
        if x % 2 == 0:
            adjusted.append(x * 1.5)
        else:
            adjusted.append(x - 1)
    return [val for val in adjusted if val > 0]

def generate_phase_shifts(n):
    shifts = []
    for i in range(n):
        shifts.append((i ** 2) % 7)
    return shifts

def filter_resonance(peaks):
    result = []
    for p in peaks:
        if p in {3, 5, 6}:
            result.append(p * 2)
    return result

def calculate_thermal_output(config):
    base = 0
    temp_val = 0
    
    # Irrelevant signal processing chain (distractor)
    signals = [config[i] ^ (i * 3) for i in range(len(config))]
    filtered_signals = [s for s in signals if s % 4 == 0]
    if len(filtered_signals) > 3:
        temp_val = sum(filtered_signals[:3])
    else:
        temp_val = max(signals) * 2
    
    # Core logic disguised among distractions
    segment_a = config[1:6]
    segment_b = config[4:9]
    intersection = set(segment_a) & set(segment_b)
    
    # Misleading entropy calculation (dead path)
    entropy_score = 0
    for val in config:
        if val > 5:
            entropy_score += (val % 3) * 0.5
    entropy_score = round(entropy_score, 2)
    
    # Actual relevant transformation
    transformed = []
    for x in intersection:
        if x % 2 == 0:
            transformed.append(x ** 2)
        else:
            transformed.append(x + 1)
    
    # Use of itertools to add complexity
    combos = list(itertools.combinations(transformed, 2))
    combo_sums = [sum(c) for c in combos]
    
    # Red herring: unused complex structure
    metadata_cache = {}
    for idx, cs in enumerate(combo_sums):
        metadata_cache[f'entry_{idx}'] = {
            'value': cs,
            'flagged': cs % 6 == 0,
            'origin': 'unknown'
        }
    
    # Key computation hidden among noise
    base = sum(transformed)
    modifier = len([c for c in combo_sums if c > 10])
    
    # Early return red herring (never taken due to data)
    if base < 0:
        return -1
    
    # Real answer computation
    thermal_output = base + modifier * 3
    
    # Decoy assignment
    diagnostic_trace = [base, modifier, temp_val, entropy_score]
    
    return thermal_output

# Simulated sensor readings (input data)
sensor_readings = [2, 4, 5, 6, 4, 7, 8, 4, 9]

# Dead preprocessing path (not used in final calculation)
processed_bounds = preprocess_constraints(sensor_readings)
phase_data = generate_phase_shifts(5)
resonance_filtered = filter_resonance(phase_data)

# Critical execution point
logistical_matrix = [r ^ 1 for r in sensor_readings]
thermal_capacity = calculate_thermal_output(logistical_matrix)

print(f"Result: {thermal_capacity}")