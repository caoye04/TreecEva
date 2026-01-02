from collections import defaultdict, Counter
import math

# Simulated sensor data preprocessing with red herrings
def preprocess_readings(raw):    adjusted = []    noise_floor = 0.02    scaling_factor = 1.87    offset = -0.3    for val in raw:        if val < 0.1:            continue        corrected = (val + offset) * scaling_factor        if corrected > 1.0:            adjusted.append(round(corrected, 3))    return adjusted

# Irrelevant transformation - decoy function
def spectral_transform(seq):    transformed = []    for i in range(len(seq)):        transformed.append(seq[i] * math.sin(i + 0.5))    return [round(x, 3) for x in transformed]

# Core pattern extraction (relevant)
def extract_signature(data):    freq_map = Counter(data)    dominant = freq_map.most_common(1)[0][1]    total = len(data)    entropy = 0.0    for count in freq_map.values():        p = count / total        entropy -= p * math.log2(p)    return round(entropy, 4), dominant

# Data enhancement with distractors
def augment_sequence(base):    enhanced = []    temp_store = defaultdict(list)    cumulative = 0    for idx, item in enumerate(base):        temp_store['type_a'].append(item * 2)  # red herring
        temp_store['type_b'].append(item ** 0.5)  # irrelevant
        cumulative += item        if cumulative > 5:            enhanced.append(item)            cumulative = 0  # reset logic    return enhanced

# Primary transformation chain (partially relevant)
def transform_signal(sequence):    intermediate = []    shift_register = [0, 0, 0]    for val in sequence:        shifted = val * 1.1 + shift_register[2] * 0.1        shift_register = [shift_register[1], shift_register[2], shifted]        intermediate.append(round(shifted, 3))    filtered = [x for x in intermediate if x > 0.5]    return filtered

# Misleading analysis path - dead end
def compute_resonance(pattern):    if not pattern:        return 0    resonance_score = 0    for i in range(1, len(pattern)):        diff = pattern[i] - pattern[i-1]        if diff > 0.2:            resonance_score += diff * 1.5    return round(resonance_score, 3)

# Real analytical core
def analyze_pattern(seq):    if len(seq) == 0:        return 0    
    # Key computation steps
    length_flag = len(seq) > 3
    sum_val = sum(seq)
    avg = sum_val / len(seq)
    variance = sum((x - avg) ** 2 for x in seq) / len(seq)
    std_dev = math.sqrt(variance)
    normalized_peak = max(seq) / (std_dev + 1e-8)
    
    # Critical intermediate calculation
    adjustment_curve = []    for x in seq:
        if x < avg:
            adjustment_curve.append((avg - x) * 0.3)
        else:
            adjustment_curve.append((x - avg) * 0.7)
    
    # Final diagnostic computation
    base_score = normalized_peak * 100
    correction_factor = sum(adjustment_curve) * 1.25
    final_diagnostic = base_score - correction_factor
    
    # Irrelevant post-processing
    diagnostics_log = defaultdict(int)
    diagnostics_log['entries'] = len(seq)
    diagnostics_log['base'] = round(base_score, 2)
    diagnostics_log['correction'] = round(correction_factor, 2)
    
    return int(round(final_diagnostic))

# Unused function - deliberate distraction
def legacy_calibrate(arr):
    return [x * 0.95 for x in arr if x > 0.3]

# Main execution flow
if __name__ == '__main__':
    raw_sensor_data = [0.15, 0.22, 0.08, 0.33, 0.41, 0.19, 0.27, 0.52, 0.09]
    
    # Step 1: Preprocess (relevant)
    cleaned = preprocess_readings(raw_sensor_data)
    
    # Step 2: Augment (partial relevance)
    extended_data = augment_sequence(cleaned)
    
    # Step 3: Transform signal (relevant)
    transformed_data = transform_signal(extended_data)
    
    # Step 4: Extract signature (distractor)
    entropy_metric, peak_count = extract_signature(transformed_data)
    
    # Step 5: Spectral transform (red herring)
    spectral_output = spectral_transform(transformed_data)
    
    # Step 6: Compute resonance (dead end)
    dummy_resonance = compute_resonance(spectral_output)
    
    # Step 7: Actual analysis (key step)
    final_diagnostic = analyze_pattern(transformed_data)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")