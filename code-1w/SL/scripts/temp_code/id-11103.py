from collections import defaultdict
import itertools

# Simulated material stress-response analysis with red herrings and complex control flow
def generate_stress_profile(base_load, cycles):
    profile = []
    for i in range(cycles):
        if i % 4 == 0:
            profile.append(base_load * 1.2)
        elif i % 3 == 0:
            profile.append(base_load * 0.85)
        else:
            profile.append(base_load)
    return profile

# Irrelevant transformation - decoy function
def transform_coordinates(coords):
    transformed = []
    for x, y in coords:
        transformed.append((x * 0.9 + 2, y * 1.1 - 1))
    return transformed

# Unused but plausible data structure
class MaterialCache:
    def __init__(self):
        self.entries = defaultdict(list)
        self.access_log = []

    def add_entry(self, key, value):
        self.entries[key].append(value)

    def get_latest(self, key):
        return self.entries[key][-1] if self.entries[key] else None

# Misleading intermediate calculation
def compute_fallback_magnitude(arr):
    total = 0
    for val in arr:
        if val > 50:
            total += val * 0.05
        else:
            total += val * 0.01
    return total * 1.5

# Core logic disguised among distractors
def evaluate_threshold_compliance(stress_vals, limits):
    violations = 0
    temp_buffer = []
    for idx, val in enumerate(stress_vals):
        # Red herring: populating unused buffer
        temp_buffer.append(val * 0.95 if idx % 5 == 0 else val * 1.05)
        limit_key = idx % len(limits)
        if val > limits[limit_key]:
            violations += 1
    return violations

# Real computation buried in complexity
def calculate_strain_response(sequence, thresholds):
    cumulative = 0
    history = []
    factor_map = defaultdict(lambda: 0.1)
    
    # Initialize with some plausible defaults (only a subset is used)
    for i in range(7):
        if i % 3 == 0:
            factor_map[f'level_{i}'] = 0.1 + i * 0.02
        else:
            factor_map[f'level_{i}'] = 0.08
    
    # Real processing begins
    compliance_check = evaluate_threshold_compliance(sequence, list(thresholds.values()))
    adjustment_factor = 1.0
    
    # Dead code path - looks important but unused
    if compliance_check > 10:
        adjustment_factor = 0.85
    elif compliance_check > 5:
        adjustment_factor = 0.9
    else:
        adjustment_factor = 1.0  # This always executes
    
    # Actual critical computation
    for val in sequence:
        if val < 60:
            cumulative += val * factor_map['level_0']
        elif val < 80:
            cumulative += val * factor_map['level_3']  # Uses level_3 = 0.16
        else:
            cumulative += val * factor_map['level_6']  # Uses level_6 = 0.1 + 6*0.02 = 0.22
    
    # Apply adjustment (neutral in this case)
    result = cumulative * adjustment_factor
    
    # Populate history (unused later)
    for _ in itertools.repeat(None, 3):
        history.append(result * 0.99)
    
    return int(result)  # Final conversion to integer

# Main execution block with distractions
if __name__ == '__main__':
    # Generate realistic input data
    stress_sequence = generate_stress_profile(base_load=55, cycles=12)
    
    # Unused coordinate transformation
    coords = [(1.2, 3.4), (2.5, 4.1), (3.8, 2.9)]
    transformed_coords = transform_coordinates(coords)
    
    # Create and populate cache (not used in final calculation)
    cache = MaterialCache()
    for s in stress_sequence:
        cache.add_entry('stress', s)
    
    # Define threshold map - only the values are used in core logic
    threshold_map = defaultdict(int)
    threshold_map.update({
        'tension': 75,
        'shear': 65,
        'torsion': 55,
        'bend': 70
    })
    
    # Compute fallback metric (never used)
    fallback_score = compute_fallback_magnitude(stress_sequence)
    
    # REAL ANSWER COMPUTATION HERE
    final_yield = calculate_strain_response(stress_sequence, threshold_map)
    
    # Print required result
    print(f"Result: {final_yield}")