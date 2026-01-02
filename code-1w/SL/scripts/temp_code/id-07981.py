import math

# Simulated sensor array data processing with diagnostic evaluation
def collect_readings():
    raw_samples = [145, 267, 189, 98, 312, 223, 176, 255]
    calibration_offset = 42
    adjusted = [x - calibration_offset for x in raw_samples]
    return adjusted

def filter_outliers(data, limit=200):
    # Irrelevant filtering path (not used in final computation)
    return [x for x in data if x < limit]

def compute_entropy(values):
    # Distractor function: looks important but unused
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log(p) for p in probs)

def generate_checksum(seq):
    # Misleading intermediate computation
    chk = 0
    for i, val in enumerate(seq):
        chk ^= (val + i) % 256
    return chk

def preprocess(signal):
    # Actual preprocessing path
    amplified = [int(x * 1.5) for x in signal]
    shifted = [x >> 2 for x in amplified]  # Bit shift as part of transformation
    normalized = [x for x in shifted if x % 2 == 0]  # Keep only even values
    return normalized

def build_threshold_map(config_level):
    # Creates a tuple-based mapping
    levels = ['low', 'medium', 'high']
    base = {'low': 80, 'medium': 120, 'high': 160}
    scale = {'low': 0.8, 'medium': 1.0, 'high': 1.3}
    return {lvl: int(base[lvl] * scale[lvl]) for lvl in levels}

def evaluate_peaks(data, ref_map):
    # Unused peak analysis (red herring)
    count = 0
    for x in data:
        if x > ref_map['high']:
            count += 1
    return count

def integrate_phases(components, mode='strict'):
    # Complex but irrelevant integration logic
    result = 0
    for idx, val in enumerate(components):
        if mode == 'strict' and val > 100:
            result += val // (idx + 1)
        else:
            result += val % 50
    return result

def analyze_signal(dataset, thresholds):
    # Core logic: count how many exceed medium threshold
    medium_limit = thresholds['medium']
    high_count = sum(1 for x in dataset if x > medium_limit)
    
    # Additional condition: must have at least one value divisible by 7
    has_divisible_by_7 = any(x % 7 == 0 for x in dataset)
    
    # Final decision logic
    if high_count >= 3 and has_divisible_by_7:
        return 867
    elif high_count >= 2:
        return 432
    else:
        return 119

# Main execution flow
if __name__ == '__main__':
    # Step 1: Collect raw data
    readings = collect_readings()
    
    # Step 2: Preprocess the signal (this is critical)
    processed_data = preprocess(readings)
    
    # Step 3: Build threshold configuration (used in analysis)
    threshold_map = build_threshold_map('high')
    
    # Distraction: execute irrelevant functions
    dummy_entropy = compute_entropy(readings)
    checksum_val = generate_checksum(processed_data)
    peak_tally = evaluate_peaks(processed_data, threshold_map)
    integrated_score = integrate_phases(processed_data)
    filtered_slice = filter_outliers(readings, limit=180)
    
    # Critical statement
    final_diagnostic = analyze_signal(processed_data, threshold_map)
    
    # Output result
    print(f"Result: {final_diagnostic}")