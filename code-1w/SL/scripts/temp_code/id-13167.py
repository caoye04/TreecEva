def analyze_readings(values):
    adjusted = [v * 1.05 for v in values]
    return [a for a in adjusted if a > 70]

# Irrelevant helper (dead function)
def dummy_normalize(data):
    return [x / max(data) for x in data]

# Unused transformation
def transform_case(strings):
    return [s.upper() if i % 2 else s.lower() for i, s in enumerate(strings)]

# Decoy metrics calculation
temp_analysis = {'peak': 98.6, 'baseline': 45.0, 'offset': 3.14}
scaling_factor = 2.5

# Real data pipeline
raw_readings = [65, 80, 75, 90, 60]
filtered_readings = list(filter(lambda x: x >= 70, raw_readings))

# Simulate sensor drift correction
corrected = [r * 1.1 for r in filtered_readings]
status_flags = [True if c > 80 else False for c in corrected]

# Auxiliary map with red herring data
diagnostic_map = {k: v * 0.1 for k, v in temp_analysis.items()}

# Dummy zip usage to add distraction
dummy_pairs = list(zip(['a', 'b', 'c'], [10, 20, 30]))

# Actual processing chain
def compute_baseline(signal):
    return sum(signal) / len(signal)

baseline = compute_baseline(corrected)

# Introduce misleading intermediate
aggregate_diagnostic = baseline * scaling_factor  # Not used later

# Core logic disguised among noise
metadata_log = [
    {'id': 'A', 'active': True},
    {'id': 'B', 'active': False},
    {'id': 'C', 'active': True}
]

# Conditional expression and enumerate distraction
activation_states = [
    item['id'].lower() if item['active'] else 'off' for idx, item in enumerate(metadata_log)
]

# Real computation begins here — hidden in plain sight
def extract_relevant_indices(flags):
    return [i for i, f in enumerate(flags) if f]

indices = extract_relevant_indices(status_flags)
subset = [corrected[i] for i in indices]

# Sorting irrelevant but plausible
sorted_subset = sorted(subset, reverse=True)

# Another decoy structure
temporary_buffer = [(x, x**2) for x in subset]

# Begin critical path
health_data = {
    'readings': corrected,
    'indices': indices,
    'base': baseline,
    'flags': status_flags
}

# Key function with conditional logic and distractors
def process_metrics(data):
    readings = data['readings']
    base = data['base']
    
    # Bit manipulation red herring
    magic_offset = (len(readings) << 2) ^ 5  # Unused later
    
    # Real adjustment
    adjusted_vals = [r - base for r in readings]
    
    # Conditional expression use
    scaling = 1.75 if sum(adjusted_vals) > 30 else 0.85
    
    # Weighted contribution
    weights = [1.0, 1.2, 1.5, 1.8]  # hypothetical time-based weights
    weighted = [w * adjusted_vals[i] if i < len(adjusted_vals) else 0 for i, w in enumerate(weights)]
    
    # Final aggregation
    raw_score = sum(weighted) * scaling
    
    # Normalization offset (constant)
    final_score = int(raw_score + 25.7)  # Deterministic integer result
    
    # Dead code branch (never reached due to prior logic)
    if len(readings) == 0:
        fallback = sum(data['flags'])
        return fallback * 10
        
    return final_score

# Execution point of interest
final_score = process_metrics(health_data)

# Print required output
print(f"Result: {final_score}")