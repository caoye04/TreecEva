import itertools

# Simulated system diagnostics with mixed signal types
def analyze_signals(raw_readings):
    filtered = [x for x in raw_readings if x > 0.1]
    normalized = [round(x / sum(filtered), 3) for x in filtered]
    return normalized

# Irrelevant helper - distractor function
def legacy_calibrate(x):
    return (x + 2) * 0.9 if x < 5 else x

# Core logic disguised among red herrings
def evaluate_thresholds(values, limit):
    count = 0
    for v in values:
        if v < limit:
            count += 1
            if count > 2:
                break
    return count >= 3

# Unused diagnostic mode - dead code path
def run_diagnostics(mode='basic'):
    if mode == 'advanced':
        return [i ** 2 for i in range(10)]
    return []

# Key transformation function with embedded logic chain
def extract_features(data_stream):
    chunks = [data_stream[i:i+4] for i in range(0, len(data_stream), 4)]
    features = []
    for chunk in chunks:
        if len(chunk) == 4:
            # Meaningful computation
            product = chunk[0] * chunk[2]
            sum_sq = chunk[1] ** 2 + chunk[3] ** 2
            features.append(product - sum_sq)
    return features

# Secondary processing with conditional masking
def apply_mask(features, mask_signal):
    result = []
    for f, m in zip(features, itertools.cycle(mask_signal)):
        if m > 0.5:
            result.append(f * 1.1)
        else:
            result.append(f - 0.5)  # Distractor operation
    return result

# Main metric processor - critical path
def process_metrics(flags, dataset):
    temp_state = 0
    for flag in flags:
        if flag == 'OPTIMAL':
            temp_state += 2
        elif flag == 'DEGRADED':
            temp_state -= 1
    
    # Real computation interwoven with noise
    base_value = sum(dataset) / len(dataset)
    deviation = abs(base_value - 0.5)
    
    # This branch is never taken - misleading path
    if deviation > 1.0:
        adjusted = base_value * 0.1
    else:
        adjusted = base_value * 4.2  # Actual used path
    
    # Complex interaction across multiple concepts
    final_modifier = 1.0
    if temp_state >= 3:
        final_modifier = 1.75
    elif temp_state == 2:
        final_modifier = 1.2
    else:
        final_modifier = 0.8  # Dead assignment - not used due to later override
    
    final_modifier = 1.4  # Overrides previous logic - subtle but valid
    
    intermediate = adjusted * final_modifier
    
    # Final step with deterministic outcome
    final_score = int(intermediate * 100) + 37
    
    # Unused cleanup - red herring
    def cleanup():
        nonlocal final_score
        final_score = max(0, final_score - 100)
    
    return final_score

# Simulated input data - realistic context
raw_sensor_data = [0.15, 0.22, 0.08, 0.31, 0.27, 0.19, 0.03, 0.36]
analyzed = analyze_signals(raw_sensor_data)

# Generate feature set from processed data
binary_pattern = [int(x * 10) % 2 for x in analyzed]
expanded = [x * 10 for x in analyzed]
features_raw = extract_features(expanded)

# Apply irrelevant transformation
masked_features = apply_mask(features_raw, binary_pattern)

# Define execution-critical variables
quality_flags = ['OPTIMAL', 'OPTIMAL', 'DEGRADED', 'OPTIMAL']
performance_data = [0.48, 0.52, 0.45, 0.55, 0.49]

# Execute main logic
final_score = process_metrics(quality_flags, performance_data)

# Output result as required
print(f"Result: {final_score}")