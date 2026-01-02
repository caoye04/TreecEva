import math

# Sensor simulation and diagnostic analysis system
def generate_signals(baseline, noise_level, count):
    return [baseline + ((i * 0.7) % 2.5) * noise_level for i in range(count)]

# Irrelevant helper - looks useful but unused in critical path
def deprecated_normalizer(x):
    return [val / max(x) for val in x]

# Data transformation pipeline
def filter_outliers(data, threshold=1.5):
    median_val = sorted(data)[len(data)//2]
    deviation = [abs(x - median_val) for x in data]
    mad = sorted(deviation)[len(deviation)//2]  # Median absolute deviation
    limit = threshold * mad
    return [x for x in data if abs(x - median_val) <= limit], median_val, mad

# Signal conditioning with red herring computation
def condition_signal(raw):
    shifted = [x * 1.03 + 0.5 for x in raw]
    adjusted = [math.sin(x) * math.cos(x) for x in shifted]  # Distractor trig chain
    envelope = [abs(x) for x in adjusted[:len(adjusted)//2]]  # Partial use - misleading
    return shifted[:len(raw)]  # Only 'shifted' portion matters

# Metric extractor - combines multiple concepts
def extract_features(signal):
    stats = {
        'mean': sum(signal) / len(signal),
        'peak': max(signal),
        'energy': sum(x**2 for x in signal),
        'entropy': -sum(p * math.log(p + 1e-9) for p in [x/sum(signal) for x in signal])
    }
    # Decoy dictionary entry
    stats['ghost_metric'] = sum(math.tan(x + 0.1) for x in signal if x > 1)  # Dead-end calc
    return stats

# Higher-order function with lambda abstraction layer
def create_transformer(factor):
    return lambda op: [op(x, factor) for x in range(1, 6)]
calibration_curve = create_transformer(2.5)(lambda a, b: a * b)  # Irrelevant calibrated values

# Set-based interference: simulate redundant system checks
system_codes = {f'ERR{i}' for i in [101, 205, 307, 410, 503]}
diag_flags = {f'FLG{j}' for j in [11, 22, 33, 44]}  
active_alerts = system_codes & {f'ERR{k}' for k in [205, 307, 999]}  # Misleading intersection

# Core processing with nested logic and distractors
def process_diagnostics(raw_readings):
    # Step 1: Apply conditioning
    conditioned = condition_signal(raw_readings)
    
    # Step 2: Filter with intermediate unpacking (mad not used later)
    clean_data, median_val, mad = filter_outliers(conditioned, threshold=1.8)
    
    # Step 3: Extract feature set
    features = extract_features(clean_data)
    
    # Step 4: Simulate redundant health check (distractor block)
    health_index = 0
    for i, val in enumerate(clean_data):
        if val > median_val:
            health_index += int(math.sqrt(abs(val)) * 1.3)
        else:
            health_index -= 1  # Red herring decrement
    # health_index never used again
    
    # Step 5: Construct processed metric with decoy fields
    processed = {
        'timestamp': 1698765432,
        'readings_count': len(clean_data),
        'primary_signal': features['mean'] * 0.87,
        'secondary_signal': features['peak'] * 0.42,
        'tertiary_signal': features['energy'] * 0.03,
        'spurious_flag': 'ERR205' in active_alerts,  # False, irrelevant
        'version': 'v2.1'
    }
    
    return processed

# Analysis engine with complex control flow
def analyze_readings(metrics_dict):
    primary = metrics_dict['primary_signal']
    secondary = metrics_dict['secondary_signal']
    tertiary = metrics_dict['tertiary_signal']
    
    # Multi-level decision tree with decoy branches
    if primary > 2.0:
        if secondary > 1.5:
            base_score = primary * secondary
        else:
            base_score = primary * 1.2
    elif primary > 1.0:
        temp_factor = math.log(primary + 1)
        if tertiary > 0.5:
            base_score = (primary + temp_factor) * tertiary
        else:
            # This branch contains dead computation
            shadow_calc = sum(math.exp(-i*0.1) for i in range(10)) * tertiary
            base_score = primary * 0.9
    else:
        fallback_map = {i: i**2 for i in range(5)}  # Unused dict
        base_score = 0.5
    
    # Final adjustment using set operation red herring
    flag_adjustment = len(diag_flags | {f'FLG{x}' for x in [55, 66]}) * 0.05  # Constant 7 * 0.05
    final_score = base_score + flag_adjustment
    
    # Critical output derived from prior logic
    final_diagnostic = int((final_score * 1000) // 1)  # Scale and truncate
    
    return final_diagnostic

# Generate input data
sensor_baseline = generate_signals(baseline=1.8, noise_level=0.65, count=12)

# Process the pipeline
processed_metrics = process_diagnostics(sensor_baseline)

# Execute key statement
final_diagnostic = analyze_readings(processed_metrics)

# Output result
print(f"Target result: {final_diagnostic}")