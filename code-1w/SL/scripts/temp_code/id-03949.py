import math

def analyze_signal(x):
    # Irrelevant signal processing function (dead end)
    return sum([math.sin(x + i) for i in range(5)])

def transform_value(n):
    # Complex but irrelevant transformation chain
    temp_a = (n ** 2 + 3 * n) % 17
    temp_b = (n * 5 - 12) & 0xFF
    temp_c = (temp_a ^ temp_b) >> 1
    return temp_c if temp_c > 10 else temp_b

def compute_entropy(seq):
    # Distractor: computes entropy but unused in final logic
    total = sum(seq)
    if total == 0:
        return 0.0
    probs = [v / total for v in seq if v > 0]
    return -sum(p * math.log2(p) for p in probs)

def evaluate_threshold(val, limit=100):
    # Misleading threshold logic that looks important
    if val < 0:
        return False
    return (val % 7 == 0) or (val > limit and (val & 1))

def extract_features(data):
    # Real feature extraction used later
    magnitude = sum(abs(x) for x in data)
    parity_flag = len([x for x in data if x % 2 == 0]) > 2
    peak = max(data)
    adjusted_peak = peak * 2 if parity_flag else peak
    return magnitude, adjusted_peak, parity_flag

def filter_candidates(items):
    # Unused filtering path (red herring)
    return [x for x in items if x % 3 != 0 and x > 0]

def process_pipeline(stream):
    # Core logic with embedded distractors
    base_score = 0
    offset = 13
    
    # Irrelevant pre-processing block
    noise_floor = [transform_value(i) for i in range(len(stream))]
    average_noise = sum(noise_floor) / len(noise_floor) if noise_floor else 0
    
    # Actual relevant computation begins
    raw_magnitude, enhanced_peak, has_even_bias = extract_features(stream)
    
    # Conditional expression (required language feature)
    adjustment_factor = 1.5 if has_even_bias and enhanced_peak > 50 else 0.8
    
    # Accumulation with conditional influence
    base_score += raw_magnitude
    
    # Simulate feedback loop (only some parts matter)
    feedback_gain = 0
    for i in range(3):
        if i == 0:
            feedback_gain += enhanced_peak // 4
        elif i == 1:
            # Dead branch - never executed due to logic
            feedback_gain += analyze_signal(enhanced_peak)  # Unused result
        else:
            feedback_gain += len(stream) * 2
    
    # Combine real components
    intermediate = base_score * adjustment_factor + feedback_gain + offset
    
    # Final decision with bit manipulation (core concept)
    temp_result = int(intermediate) ^ 0xAA  # XOR mask
    temp_result = (temp_result + 17) & 0xFFFF  # Wrap in 16-bit range
    
    # One last conditional refinement
    final_modifier = 21 if temp_result % 5 == 0 else 9
    final_output = temp_result - final_modifier
    
    # Print required at end
    return final_output

# Main execution
if __name__ == '__main__':
    # Input data with domain meaning (sensor readings)
    data_stream = [4, -8, 15, 16, 23, -42, 108]
    
    # Call to key function
    final_output = process_pipeline(data_stream)
    
    # Additional irrelevant variables (distractors)
    calibration_sequence = [transform_value(x) for x in data_stream]
    system_entropy = compute_entropy(calibration_sequence)
    valid_candidates = filter_candidates(data_stream)
    
    # Output the target result
    print(f"Target result: {final_output}")