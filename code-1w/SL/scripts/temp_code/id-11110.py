import math

# System configuration parameters (some are red herrings)
base_frequency = 440.0
modulation_depth = 0.75
reference_phase = 1.33

def analyze_signal_strength(signal, noise_floor):
    # Irrelevant signal processing function
    return sum(s ** 2 for s in signal if s > noise_floor) / len(signal)

def generate_combinations(n, r):
    # Simple combinatorics helper - appears relevant but used minimally
    if r > n or r < 0:
        return 0
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

def evaluate_threshold_consistency(readings, limit):
    # Dead code path - never called
    count = 0
    for val in readings:
        if abs(val - limit) < 0.01:
            count += 1
    return count > len(readings) // 2

def preprocess_units(data, mode='strict'):
    # Distractor-heavy preprocessing with conditional expressions
    filtered = []
    scaling_factor = 1.5 if mode == 'loose' else (0.8 if mode == 'strict' else 1.0)
    offset_correction = 0.05 if len(data) > 10 else (-0.02 if len(data) > 5 else 0)
    
    temp_cache = []  # Unused cache (distractor)
    for item in data:
        adjusted = item * scaling_factor + offset_correction
        if adjusted > 0.1:
            filtered.append(int(round(adjusted)))
    
    # Extra misleading logic
    if len(filtered) % 2 == 0 and scaling_factor > 1:
        filtered = [x + 1 for x in filtered]

    return filtered

def calculate_entropy(values):
    # Decoy function - simulates information theory computation
    total = sum(values)
    if total == 0:
        return 0.0
    probabilities = [v / total for v in values if v > 0]
    return -sum(p * math.log(p) for p in probabilities if p > 0)

def optimize_allocation(units, threshold):
    # Core logic buried in distractions
    processed = [u for u in units if u >= threshold]
    
    # Red herring variables
    peak_utilization = max(processed) if processed else 0
    avg_utilization = sum(processed) / len(processed) if processed else 0
    volatility_index = peak_utilization - avg_utilization
    
    # Critical branching with conditional expression
    base_capacity = sum(processed) if len(processed) > 3 else sum(p**2 for p in processed)
    
    # Secondary adjustment using bit manipulation (seemingly complex but deterministic)
    shift_level = 2 if base_capacity > 50 else (1 if base_capacity > 20 else 0)
    shifted_capacity = base_capacity << shift_level
    
    # Final adjustment based on combinatorics side-calculation (distractor use)
    combo_score = generate_combinations(len(processed), 2)
    final_capacity = shifted_capacity - combo_score
    
    # Irrelevant logging
    debug_flag = False
    if debug_flag:  # Never true
        print(f'Debug: {volatility_index=}, {combo_score=}')
    
    return final_capacity

# Main execution flow
raw_input_data = [3, 5, 7, 9, 2, 8, 6, 4]
threshold = 5

# Preprocessing with irrelevant mode
units = preprocess_units(raw_input_data, mode='strict')

# Call to target function
final_capacity = optimize_allocation(units, threshold)

# Print result as required
print(f"Target result: {final_capacity}")