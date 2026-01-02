import itertools

# Simulated sensor array data from environmental monitoring system
def acquire_sensor_data():
    raw_values = [127, 255, 192, 64, 96, 159]
    return raw_values

# Irrelevant transformation - acts as red herring
def encrypt_data(data):
    return [d ^ 42 for d in data]

# Decoy function - never called but looks important
def calibrate_sensors(units='metric'):
    adjustments = {i: (i * 0.92 + 3) for i in range(10)}
    return adjustments

# Signal processor with multiple distractor paths
def process_signal(raw_val, mode='standard'):
    if mode == 'invalid':
        return raw_val >> 3
    elif mode == 'legacy':
        temp = raw_val & 0x7F
        temp = (temp << 1) | (temp >> 6)
        return temp
    else:
        # Actual relevant path
        processed = ((raw_val >> 2) ^ 15) & 63
        if processed > 32:
            processed = 65 - processed
        return processed

# Data enhancer - contains dead logic branches
def enhance_resolution(data_list):
    enhanced = []
    for val in data_list:
        if val < 10:  # Dead condition - never true
            val *= 100
        elif val > 1000:  # Another dead condition
            val -= 500
        base_enhanced = val * 1.5 + 2.5
        enhanced.append(int(base_enhanced))
    return enhanced

# Redundant validation check that doesn't affect outcome
def validate_consistency(signal_set):
    total = sum(signal_set)
    checksum = total % 256
    expected = 128
    deviation = abs(checksum - expected)
    return deviation < 30

# Core analysis function - key to final answer
def analyze_readings(signals):
    cumulative_score = 0
    
    # Real computation begins
    for idx, s in enumerate(signals):
        if idx % 2 == 0:
            cumulative_score += s * 3
        else:
            cumulative_score -= s * 2
    
    # Final adjustment based on pattern matching
    pair_patterns = list(itertools.combinations(signals, 2))
    high_pairs = [p for p in pair_patterns if sum(p) > 40]
    
    # Conditional expression used meaningfully
    bonus = len(high_pairs) * 4 if len(high_pairs) > 5 else len(high_pairs) * 2
    
    cumulative_score += bonus
    return cumulative_score

# Main execution flow
if __name__ == '__main__':
    # Step 1: Acquire real data
    sensor_output = acquire_sensor_data()
    
    # Step 2: Apply irrelevant encryption (distractor)
    encrypted = encrypt_data(sensor_output)
    
    # Step 3: Process each signal through correct pathway
    processed_signals = [process_signal(v) for v in sensor_output]
    
    # Step 4: Enhance resolution (has no effect on integer logic)
    enhanced_signals = enhance_resolution(processed_signals)
    
    # Step 5: Validate (distractor - result unused)
    is_valid = validate_consistency(processed_signals)
    
    # Step 6: Analyze readings - this triggers the key statement
    final_diagnostic = analyze_readings(processed_signals)
    
    # Print final result as required
    print(f"Result: {final_diagnostic}")