import math

# Irrelevant helper function (dead code path)
def unused_analysis(x):
    return sum(i ** 2 for i in x if i % 3 == 0)

# Distractor data structures
temp_readings = [23.5, 24.1, 22.9, 25.0, 26.3]
cpu_load_log = [(1, 0.45), (2, 0.67), (3, 0.55), (4, 0.89), (5, 0.72)]

# Core input datadata = [
    {'name': 'sensor_A', 'values': [1, 4, 7, 10]},
    {'name': 'sensor_B', 'values': [2, 5, 8]},
    {'name': 'sensor_C', 'values': [3, 6, 9, 12, 15]}
]

# Weight configuration with decoy entries
weights = {
    'base': 1.5,
    'bonus': 0.25,
    'penalty': 0.1,
    'irrelevant_factor': 999,  # red herring
    'debug_mode': True  # misleading flag
}

# Misleading intermediate calculation
def apply_mask(values, mask=[1, 0, 1, 0, 1]):
    return [v for i, v in enumerate(values) if i < len(mask) and mask[i]]

# Real processing begins here
def compute_stat(values):
    avg = sum(values) / len(values)
    deviation = math.sqrt(sum((x - avg) ** 2 for x in values) / len(values))
    return avg + (deviation * 0.1)

# Higher-order function with lambda (required feature)
def create_scorer(scale):
    return lambda val: val * scale if val > 0 else abs(val) * 0.5

scorer = create_scorer(weights['base'])

# Conditional expression used (required feature)
adjustment = 1.1 if len(data) > 2 else 0.9

# Main processing pipeline
def process_metrics(entries, config):
    results = []
    
    for entry in entries:
        raw_vals = entry['values']
        
        # Apply actual transformation (not the mask one)
        filtered = [x for x in raw_vals if x % 2 == 1]  # keep only odd numbers
        
        stat_val = compute_stat(filtered)
        scaled_val = scorer(stat_val)
        
        # Conditional adjustment
        adjusted = scaled_val * adjustment if 'C' in entry['name'] else scaled_val * 0.8
        
        # Simulate bit manipulation side-channel (distractor)
        noise = 0
        for x in raw_vals[:3]:
            noise ^= (x << 1) | 1  # irrelevant bitwise chain
        
        # Final per-entry score
        final_entry_score = adjusted + config.get('bonus', 0) - config.get('penalty', 0)
        results.append(final_entry_score)
    
    # Aggregate using complex reduction
    aggregate = 0
    for i, r in enumerate(results):
        if i % 2 == 0:
            aggregate += r * (i + 1)
        else:
            aggregate -= r * 0.5
    
    # Final nonlinear transformation
    return math.floor(aggregate * 1.05)

# Key execution point
final_score = process_metrics(data, weights)

# Print result as required
print(f"Result: {final_score}")