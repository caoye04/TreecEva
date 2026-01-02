import math

def analyze_signal(x):
    return math.sin(x) * math.cos(x)

def dummy_transform(data):
    # Irrelevant transformation (dead function)
    return [d ** 3 for d in data]

def validate_readings(readings):
    # Distractor logic: checks but doesn't alter main flow
    if all(r > -100 and r < 100 for r in readings):
        status = 'valid'
    else:
        status = 'invalid'
    return status

def compute_entropy(data):
    # Misleading computation: not used in final result
    total = sum(abs(x) for x in data)
    entropy = 0.0
    for x in data:
        p = abs(x) / total
        if p > 0:
            entropy -= p * math.log(p)
    return round(entropy, 4)

def extract_features(raw_data):
    # Real processing step: extracts every third element
    features = raw_data[::3]
    # Adds irrelevant offset
    adjusted = [f + 10 for f in features]  # red herring
    return features  # only features used

def apply_filter(seq, threshold):
    # Real filtering logic
    return [x for x in seq if x > threshold]

def merge_dicts(dict_list):
    # Distractor: complex dictionary operation with no impact
    merged = {}
    for i, d in enumerate(dict_list):
        for k, v in d.items():
            merged[f'{k}_{i}'] = v * 2
    return merged

def process_readings(data, factor):
    # Core logic begins
    subset = extract_features(data)
    
    # Apply real transformation
    scaled = [x * factor for x in subset]
    
    # Introduce decoy variables
    temp_result = sum(scaled) / len(scaled) if scaled else 0
    baseline = 42.0
    adjustment = math.tanh(temp_result)  # unused distraction
    
    # Real conditional branch
    if len(scaled) > 2:
        filtered = apply_filter(scaled, baseline)
        if filtered:
            max_val = max(filtered)
            min_val = min(filtered)
            # Critical computation
            diagnostic_score = (max_val - min_val) * math.sqrt(len(filtered))
        else:
            diagnostic_score = 0.0
    else:
        diagnostic_score = 0.0
    
    # Decoy dictionary operations
    stats = {
        'count': len(data),
        'raw_sum': sum(data),
        'peak': max(data),
        'noise_floor': min(data)
    }
    metadata = {
        'version': '2.1',
        'mode': 'diagnostic'
    }
    info_bundle = merge_dicts([stats, metadata])  # irrelevant
    
    # Final computation (depends on filtered result)
    final_diagnostic = int(diagnostic_score + 0.5)  # round to nearest int
    
    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Main execution
sensor_data = [15, -88, 107, 42, 93, -12, 67, 38, 150, 22, 74, 81]
calibration_factor = 1.75

# Irrelevant pre-processing
normalized = [x / max(sensor_data) for x in sensor_data]
denoised = [x for x in normalized if abs(x) > 0.1]

# Red herring: unused signal analysis
signal_analysis = [analyze_signal(x) for x in denoised]

# Actual entry point
final_diagnostic = process_readings(sensor_data, calibration_factor)