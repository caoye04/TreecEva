import math

# Simulated sensor array data processing with diagnostic evaluation
def collect_sensor_readings():
    raw_samples = [14.2, 17.5, 9.8, 23.1, 15.6, 18.3, 12.7, 20.4]
    scaling_factor = 1.8
    adjusted = [round(x * scaling_factor, 2) for x in raw_samples]
    return adjusted

# Irrelevant auxiliary function (dead code path)
def deprecated_normalization(data):
    mean_val = sum(data) / len(data)
    return [x - mean_val for x in data]

# Signal conditioning with multiple transformation layers
def filter_noise(signal_batch):
    filtered = []
    noise_floor = 15.0
    suppression_rate = 0.85
    for val in signal_batch:
        if val > noise_floor:
            val = val * suppression_rate
        else:
            val = val * 1.05
        filtered.append(round(val, 2))
    return filtered

# Advanced feature extraction using lambda and set operations
def extract_features(datum):
    categorize = lambda x: 'HIGH' if x > 18 else 'MEDIUM' if x > 12 else 'LOW'
    base_category = categorize(datum)
    
    # Distractor: complex but unused set logic
    universe = {'A', 'B', 'C', 'D', 'E'}
    active_set = {'A', 'C', 'E'}
    inactive_set = universe - active_set  # Unused
    priority_flags = active_set & {f'B', 'C', 'D'}  # Partially misleading
    
    return base_category

# Composite data enrichment (mixes relevant and irrelevant steps)
def enrich_dataset(cleaned):
    enhanced = []
    stats_tracker = {"peak": 0, "baseline": 0, "outliers": 0}
    cumulative_shift = 0
    
    for item in cleaned:
        category_hint = extract_features(item)
        shift_comp = math.sin(math.pi / 4) * cumulative_shift
        adjusted_item = item + shift_comp
        
        # Real transformation
        if category_hint == 'HIGH':
            adjusted_item += 1.2
        elif category_hint == 'MEDIUM':
            adjusted_item += 0.5
        
        enhanced.append(round(adjusted_item, 2))
        
        # Tracking logic with red herring updates
        if item > 20:
            stats_tracker["outliers"] += 1
        cumulative_shift += 0.3  # Used only in shift_comp, not critical
    
    # Irrelevant aggregation
    temp_snapshot = set(enhanced)
    outlier_set = {x for x in temp_snapshot if x > 22}
    ignored_summary = len(outlier_set.intersection({x for x in temp_snapshot if x < 10}))
    
    return enhanced

# Core analysis logic with conditional weighting
threshold_map = {
    'LOW': (0, 14),
    'MEDIUM': (14, 19),
    'HIGH': (19, 30)
}

def evaluate_stability(value, limits):
    low_bound, high_bound = limits
    if value < low_bound:
        return -1
    elif value > high_bound:
        return 1
    else:
        return 0

# Misleading diagnostic chain (decoy function)
def legacy_evaluation(seq):
    score = 0
    for x in seq:
        if x % 2 == 0:
            score += 1
    return score * 100  # Never called

# Main analysis engine
def analyze_signal(dataset, thresholds):
    diagnosis_code = 0
    trend_sequence = []
    
    for entry in dataset:
        cat = extract_features(entry)
        bounds = thresholds[cat]
        stability = evaluate_stability(entry, bounds)
        trend_sequence.append(stability)
        
        # Critical accumulation
        diagnosis_code += entry * (stability + 2)  # stability: -1,0,1 => weights: 1,2,3
    
    # Final transformation
    final_weight = len(set(trend_sequence))  # Number of unique stability states
    refined_diagnosis = int(diagnosis_code / (final_weight + 1))
    
    # Decoy computation (never used)
    phantom_index = sum(trend_sequence) ** 2 if len(trend_sequence) > 5 else 0
    
    return refined_diagnosis

# Orchestration with hidden dependencies
if __name__ == '__main__':
    # Step 1: Collect raw data
    raw_data = collect_sensor_readings()
    
    # Step 2: Apply noise filtering
    denoised_signal = filter_noise(raw_data)
    
    # Step 3: Enrich with contextual features
    processed_data = enrich_dataset(denoised_signal)
    
    # Irrelevant intermediate check
    validation_hash = sum([int(x) for x in processed_data[::2]]) % 17
    
    # Critical execution point
    final_diagnostic = analyze_signal(processed_data, threshold_map)
    
    # Output required result
    print(f"Target result: {final_diagnostic}")