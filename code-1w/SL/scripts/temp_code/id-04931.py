import math

def analyze_signal(data, config):
    # Irrelevant preprocessing steps
    normalized = [x / max(data) for x in data]
    filtered = [x for x in normalized if x > 0.1]
    stats = {
        'mean': sum(filtered) / len(filtered),
        'variance': sum((x - sum(filtered)/len(filtered))**2 for x in filtered) / len(filtered)
    }

    # Distractor: unused transformation
    def frequency_shift(val, shift=2):
        return val * (1 + math.sin(shift))

    enhanced = list(map(lambda x: x * 1.5 if x < 0.5 else x, filtered))

    # Meaningless recursive smoothing (dead path)
    def smooth_recursive(vals, depth=0):
        if depth >= 2 or len(vals) < 2:
            return vals
        smoothed = [(vals[i] + vals[i+1]) / 2 for i in range(len(vals)-1)]
        return smooth_recursive(smoothed, depth + 1)

    dummy_smooth = smooth_recursive(enhanced)

    # Real processing branch
    clipped = [min(x, 0.8) for x in enhanced]
    scaled = [int(x * 100) for x in clipped]  # Convert to integer scale

    # Bit manipulation red herring
    bit_noise = [num ^ 0b1010 for num in scaled[:5]]  # Unused
    parity_check = sum(1 for num in scaled if bin(num).count('1') % 2 == 0)

    # Core logic disguised among distractors
    if config['mode'] == 'diagnostic':
        offset = config.get('offset', 10)
        processed = []
        for val in scaled:
            if val > 50:
                processed.append(val - offset)
            else:
                processed.append(val + (offset // 2))
        
        # Decoy aggregation
        avg_len = sum(len(str(x)) for x in processed) / len(processed)  # Misleading metric
        
        # Actual relevant transformation
        transformed = [round(math.log(x + 1) * 3) for x in processed]
        
        # Conditional mutation based on distractor
        if parity_check > 3:  # Depends on earlier unused bit op result
            transformed = [x + 1 for x in transformed]

        return transformed

# Unused function - decoy
def legacy_calibrate(x):
    return (x >> 1) ^ (x << 2)

# Threshold logic with lambda
threshold_func = lambda x: x > 7.5

# Main diagnostic pipeline
raw_data = [120, 45, 89, 23, 67, 91, 150, 73]
config_params = {'mode': 'diagnostic', 'offset': 12}

def process_metrics(data_list, threshold_rule):
    count_valid = 0
    total_score = 0.0
    
    # Simulated historical baseline (irrelevant)
    baseline_ref = {i: round(math.cos(i * 0.1), 2) for i in range(10)}
    adjustment_factor = 1.0
    
    # Another decoy structure
    metadata_log = []
    for idx, val in enumerate(data_list):
        entry = {
            'id': f"M{idx:03}",
            'flagged': val < 5 or val > 25,
            'checksum': (val * 3) % 17
        }
        metadata_log.append(entry)
    
    # Real scoring logic
    for value in data_list:
        if threshold_rule(value):
            count_valid += 1
            total_score += value * 1.2
        else:
            total_score += value * 0.8
    
    # Final computation buried in noise
    raw_average = total_score / len(data_list)
    adjustment_factor = 0.95 if count_valid < 4 else 1.05
    final_score = raw_average * adjustment_factor
    
    # Critical assignment
    final_diagnostic = int(round(final_score))
    
    # Dead code path
    if final_diagnostic < 0:
        recovery_state = (final_diagnostic ^ 0xFF) + 1
        final_diagnostic = abs(recovery_state)
    
    return final_diagnostic

# Execute transformations
transformed_data = analyze_signal(raw_data, config_params)
final_diagnostic = process_metrics(transformed_data, threshold_func)
print(f"Target result: {final_diagnostic}")