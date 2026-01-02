def analyze_purity(samples):
    # Irrelevant purity analysis (dead function)
    return all(s < 0.5 for s in samples)

# Simulated water contaminant levels (mg/L)
water_samples = [0.2, 1.8, 3.1, 0.9, 2.4, 5.0, 1.2]

# Environmental safety thresholds
toxicity_threshold = 2.0
ph_level = 7.4  # Neutral pH, irrelevant to logic
oxygen_level = 8.1  # Dissolved oxygen, not used

# Supporting metrics (distraction variables)
acceptable_range = (0.0, 2.0)
violation_count = 0
exceedance_log = []

# Complex data transformation pipeline (some steps are red herrings)
scaling_factor = 1.5
temp_transformed = list(map(lambda x: round(x * scaling_factor, 2), water_samples))
shifted_values = [v - 0.5 for v in temp_transformed if v > 1.0]  # Partial filtering

# Decoy statistical summary
mean_shifted = sum(shifted_values) / len(shifted_values) if shifted_values else 0
median_like = sorted(shifted_values)[len(shifted_values)//2] if shifted_values else 0

# Actual critical processing function
def process_contaminants(readings, limit):
    global violation_count, exceedance_log
    
    # Initialize tracking
    indices_above = []
    cumulative_toxicity = 0.0
    spike_magnitude = 0
    
    # Real logic begins: track violations
    for idx, level in enumerate(readings):
        if level >= limit:
            indices_above.append(idx)
            cumulative_toxicity += level
            # Bit manipulation red herring
            spike_magnitude |= int(level) << 1
    
    # Distractor: unused nested structure
    stats_bundle = {
        'high_readings': readings[:],
        'meta': {
            'scale': scaling_factor,
            'adjusted': [x * 0.9 for x in readings if x < 4.0]
        }
    }
    
    # More distractions: unused transformations
    clipped = [min(x, limit) for x in readings]
    derived_key = sum(clipped[i] for i in indices_above) if indices_above else 0
    
    # Core calculation disguised among noise
    base_penalty = len(indices_above) * 100
    bonus_reduction = sum(1 for x in readings if x < 1.0) * 10
    raw_score = base_penalty - bonus_reduction + int(cumulative_toxicity)
    
    # Final adjustment using slicing and dictionary lookup distraction
    adjustment_map = {0: 5, 1: -3, 2: 0, 3: 2, 4: 1}
    adjustment_key = min(len(indices_above), 4)
    final_adjustment = adjustment_map.get(adjustment_key, 0)
    
    # The real answer computation
    filtration_score = raw_score + final_adjustment
    
    # Dead code path (never accessed)
    if ph_level < 6.0:
        filtration_score *= 1.2
    
    return filtration_score

# Secondary decoy function
def normalize_sample(sample_list):
    total = sum(sample_list)
    return [s / total for s in sample_list] if total > 0 else sample_list

# Unused set operations for distraction
measured_elements = {'lead', 'arsenic', 'mercury', 'nitrates'}
regulated_elements = {'lead', 'arsenic', 'cadmium', 'pesticides'}
overlap = measured_elements & regulated_elements
non_regulated = measured_elements - regulated_elements

# Critical execution point
filtration_score = process_contaminants(water_samples, toxicity_threshold)

# Additional red herring computations
aggregated_risk = sum(water_samples[i]**2 for i in range(len(water_samples)) if i % 2 == 0)
dummy_flag = any(x > 4.0 for x in temp_transformed)

# Output the target result
print(f"Result: {filtration_score}")