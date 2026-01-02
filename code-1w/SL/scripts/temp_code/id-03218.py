def analyze_water_quality(samples, thresholds):
    temp_data = [s * 1.05 for s in samples]
    adjusted_samples = [max(s, 0.1) for s in temp_data]
    
    # Irrelevant transformation path (dead code)
    normalized = []
    total = sum(adjusted_samples)
    for val in adjusted_samples:
        if total > 0:
            normalized.append(val / total)
        else:
            normalized.append(0)
    
    # Distractor: unused complex calculation
    entropy = 0.0
    for p in normalized:
        if p > 0:
            entropy -= p * __import__('math').log(p)
    
    # Actual filtering logic
    filtered_samples = []
    for i, val in enumerate(adjusted_samples):
        if val >= thresholds[i % len(thresholds)]:
            filtered_samples.append(val)
    
    return filtered_samples

# Simulate sensor readings and threshold levels
raw_samples = [0.45, 0.67, 0.23, 0.89, 0.51, 0.34, 0.76, 0.55]
alert_levels = [0.4, 0.6, 0.3, 0.7]

# Initial analysis
filtered_samples = analyze_water_quality(raw_samples, alert_levels)

# Efficiency map based on time-of-day decay (only some entries are used)
efficiency_map = {i: 0.85 + 0.1 * __import__('math').sin(i) for i in range(10)}
efficiency_map[0] = 0.0  # Red herring: zeroed but never used in computation

# Decoy function that is defined but not used
def calculate_purity_index(data):
    if not data:
        return 0
    return sum(d**2 for d in data) / len(data)

# Real processing function
def process_contaminants(samples, efficiency_profile):
    base_score = 100.0
    decay_factor = efficiency_profile.get(len(samples), 0.75)
    
    for idx, reading in enumerate(samples):
        # Apply conditional adjustment based on magnitude
        adjustment = 1.1 if reading > 0.5 else 0.9
        
        # Use of slicing to simulate windowed history (even if artificial)
        history_window = samples[max(0, idx-2):idx]
        if len(history_window) >= 2 and history_window[-1] > history_window[0]:
            adjustment *= 1.05
        
        base_score = base_score * adjustment - 5
    
    # Complex but partially irrelevant bit manipulation mask
    mask = 0
    for i in range(len(samples)):
        if samples[i] > 0.6:
            mask |= (1 << i)
    bonus = bin(mask).count('1') * 3.5 if mask > 0 else 0
    
    # Final score influenced by both decay and bonus
    final_score = (base_score * decay_factor) + bonus
    
    # Unused intermediate result (distractor)
    avg_sample = sum(samples) / len(samples) if samples else 0
    variance = sum((x - avg_sample)**2 for x in samples) / len(samples) if samples else 0
    
    return final_score

# Key execution point
filtration_score = process_contaminants(filtered_samples, efficiency_map)

# Print result for evaluation
print(f"Result: {filtration_score}")