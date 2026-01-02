import math

# Sensor simulation and diagnostic analysis system
def generate_signals(baseline, noise_factor, count):
    """Generate synthetic sensor readings (distraction function)"""
    signals = []
    for i in range(count):
        noise = math.sin(i * 0.5) * noise_factor
        signals.append(baseline + noise + i * 0.1)
    return signals

# Irrelevant data transformation (dead path)
def encrypt_sequence(seq):
    return [((x * 7) + 3) % 256 for x in seq]

# Unused utility (distractor)
def validate_checksum(data):
    total = sum(data)
    return total % 17 == 0

# Core processing pipeline
def filter_outliers(values, limit):
    """Remove values beyond limit using symmetric threshold"""
    return [v for v in values if abs(v) <= limit]

# Data normalization (partially relevant)
def normalize_readings(raw):
    min_val, max_val = min(raw), max(raw)
    if min_val == max_val:
        return [0.5] * len(raw)
    return [(x - min_val) / (max_val - min_val) for x in raw]

# Bit manipulation for status encoding (red herring)
def encode_status(flags):
    result = 0
    for i, flag in enumerate(flags):
        result |= (flag << i)
    return result ^ 0b1010

# Real-time windowed averaging (misleading intermediate)
def sliding_average(data, window_size=3):
    if len(data) < window_size:
        return [0]
    averages = []
    for i in range(len(data) - window_size + 1):
        averages.append(sum(data[i:i+window_size]) / window_size)
    return averages

# Main transformation logic
def transform_sensor_data(raw_input, mode='standard'):
    processed = []
    for val in raw_input:
        if mode == 'boost':
            processed.append(math.log(abs(val) + 1) * 2.1)
        else:
            processed.append(math.sqrt(abs(val)) + 0.5)
    return processed

# Critical diagnostic analyzer (target function)
def analyze_readings(data_list, thresholds):
    score = 0
    categories = ['alpha', 'beta', 'gamma', 'delta']
    
    # Destructuring assignment (relevant concept)
    a_lim, b_lim, g_lim, d_lim = [thresholds[k] for k in categories]
    
    # Conditional expression with string method distraction
    modifier = 1.25 if 'adjust' in ''.join(thresholds.keys()).lower() else 0.85
    
    # Real computation begins
    counts = {cat: 0 for cat in categories}
    for val in data_list:
        label = 'unknown'
        if val < a_lim:
            label = 'alpha'
        elif val < b_lim:
            label = 'beta'
        elif val < g_lim:
            label = 'gamma'
        else:
            label = 'delta'
        counts[label] += 1
    
    # Weighted scoring with conditional branches
    weights = {'alpha': 1, 'beta': 2, 'gamma': 4, 'delta': 8}
    for key in counts:
        contribution = counts[key] * weights[key]
        if key == 'delta' and counts['alpha'] == 0:
            contribution *= modifier  # Special penalty boost
        score += contribution
    
    # Final nonlinear adjustment (key step)
    if score > 0:
        score = math.log(score) * score ** 0.5
    
    # Decoy dictionary operation
    stats = {
        'total': sum(counts.values()),
        'peak': max(counts.values()),
        'entropy': sum(-v/len(data_list)*math.log(v/len(data_list)+1e-9) for v in counts.values())
    }
    
    # Actual answer derivation (non-obvious)
    final_score = int(score + 0.5)  # Round to nearest integer
    return final_score

# Simulate input generation (with distractions)
def main():
    # Generate base readings (irrelevant to final answer but looks important)
    raw_sensor_data = generate_signals(baseline=12.5, noise_factor=3.2, count=50)
    encrypted_tag = encrypt_sequence([12, 34, 56, 78])  # Dead code path
    
    # Actual relevant input (hidden among noise)
    input_sequence = [2.3, 4.7, 1.1, 8.9, 5.2, 3.3, 9.1, 7.6, 6.4, 5.8]
    
    # Filtering (partially used)
    cleaned_data = filter_outliers(input_sequence, limit=10.0)
    
    # Normalization (looks important but not used in final path)
    normalized = normalize_readings(cleaned_data)
    smoothed = sliding_average(normalized, 2)
    
    # Transform using correct path
    processed_data = transform_sensor_data(cleaned_data, mode='standard')
    
    # Threshold configuration map (critical)
    threshold_map = {
        'alpha': 1.5,
        'beta': 2.5,
        'gamma': 6.0,
        'delta': 10.0,
        'fallback': 'gamma'
    }
    
    # Status encoding (complete red herring)
    flags = [True, False, True, False]
    status_code = encode_status(flags)
    
    # The critical execution point
    final_diagnostic = analyze_readings(processed_data, threshold_map)
    
    # Output result as required
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()