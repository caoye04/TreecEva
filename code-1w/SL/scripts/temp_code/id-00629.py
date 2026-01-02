import math

# Simulated sensor data processing with diagnostic analysis
def collect_samples():
    raw_readings = [127, 255, 192, 64, 224, 32, 168, 96]
    scale_factor = 0.75
    adjusted = [r * scale_factor for r in raw_readings]
    return adjusted

# Irrelevant helper: string-based status formatting (distractor)
def format_status(code):
    states = {0: 'OK', 1: 'WARN', 2: 'ERROR'}
    suffix = '_DIAG' if code > 0 else '_NORM'
    return states.get(code, 'UNKNOWN') + suffix

# Decoy function: never called in execution path
def legacy_calibrate(data):
    return [int(x / 1.2) for x in data if x > 50]

# Signal preprocessing with bit manipulation red herring
def preprocess_signal(samples):
    shifted = []
    bit_noise = 0
    for s in samples:
        # Bit manipulation distraction
        binary_rep = bin(int(s))[2:]
        if len(binary_rep) > 7:
            bit_noise += int(binary_rep[-3:], 2)
        # Actual relevant transformation
        normalized = s / 255.0
        shifted.append(round(normalized, 4))
    # Dead computation: bit_noise is never used again
    checksum = bit_noise ^ 255  # Distractor
    return shifted

# Threshold system with dictionary mapping (core logic)
def build_threshold_map():
    categories = ['low', 'medium', 'high']
    levels = [0.3, 0.6, 0.85]
    # Set operation used meaningfully but with extra elements
    exclusion_zone = {0.6, 0.7, 0.8}
    valid_levels = set(levels) - exclusion_zone
    # Reconstruct ordered mapping
    thresholds = {}
    for i, cat in enumerate(categories):
        if levels[i] in valid_levels:
            thresholds[cat] = levels[i] * 1.1  # adjustment
        else:
            thresholds[cat] = levels[i] * 0.9
    # Add irrelevant category
    thresholds['debug'] = 0.0  # dead entry
    return thresholds

# Core analysis with control flow and data structure use
def analyze_signal(data, tmap):
    high_count = 0
    medium_count = 0
    for val in data:
        if val >= tmap['high']:
            high_count += 1
        elif val >= tmap['medium']:
            medium_count += 1
    # Compute composite score
    raw_score = (high_count * 3.5) + (medium_count * 1.2)
    
    # String method distractor: unused metadata tagging
    tags = ['anomalous', 'stable', 'noisy']
    tag_summary = ''.join(tags).upper().replace('E', 'X')  # irrelevant
    
    # Final diagnostic calculation (answer point)
    baseline = len(data) * 0.5
    adjustment = abs(raw_score - baseline) * 0.7
    final_diagnostic = raw_score - adjustment
    
    # Multiple decoy variables
    temp_result = final_diagnostic ** 2  # unused
    validation_key = hash(str(temp_result)) % 1000  # unused
    
    return round(final_diagnostic, 6)

# Main execution flow
if __name__ == '__main__':
    # Step 1: Collect raw data
    sensor_output = collect_samples()
    
    # Step 2: Preprocess signal (bit manipulation side track)
    processed_data = preprocess_signal(sensor_output)
    
    # Step 3: Build dynamic threshold map (set operations)
    threshold_map = build_threshold_map()
    
    # Step 4: Perform final diagnostic analysis
    final_diagnostic = analyze_signal(processed_data, threshold_map)
    
    # Output result as required
    print(f"Result: {final_diagnostic}")