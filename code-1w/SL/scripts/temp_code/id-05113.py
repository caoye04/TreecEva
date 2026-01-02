import math

# Irrelevant helper function (dead code path)
def unused_helper(x):
    return x ** 2 + 3 * x - 7

# Decoy transformation chain
def decoy_transform(sequence):
    temp = [x % 7 for x in sequence if x > 5]
    return sorted(temp, reverse=True)

# Real processing pipeline components
def filter_valid_packets(stream):
    return [p for p in stream if p & 1 == 1 and p > 0]  # Keep only positive odd values

def apply_phase_shift(values, shift=3):
    return [(v << 1) ^ shift for v in values]

def compute_amplitude(signal):
    return sum(abs(s) for s in signal) // len(signal)

# Lambda-based envelope detection (critical component)
envelope_detector = lambda samples: max(samples) - min(samples)

# Complex data transformation pipeline
def analyze_signal_integrity(raw_data):
    stage1 = filter_valid_packets(raw_data)
    stage2 = apply_phase_shift(stage1)
    
    # Distractor: intermediate statistic with no impact
    avg_val = sum(stage2) / len(stage2) if stage2 else 0
    median_guess = stage2[len(stage2)//2] if stage2 else 0
    
    stage3 = [x for x in stage2 if x % 3 == 0]  # Only keep multiples of 3
    
    # Another red herring: frequency simulation
    freq_map = {}
    for val in stage3:
        bin_rep = bin(val).count('1')
        freq_map[val] = bin_rep
    
    if not stage3:
        return 0
        
    base_metric = compute_amplitude(stage3)
    spread = envelope_detector(stage3)
    
    # Final nonlinear transformation using bitwise blend
    result = (base_metric ^ spread) & 0xFFFF
    adjustment = (spread >> 4) + (base_metric % 16)
    return result - adjustment

# Main processing pipeline
def process_pipeline(input_seq):
    # Multiple assignment distraction
    n, m, k = len(input_seq), sum(input_seq) // len(input_seq), 0
    temp_cache = {}  # Unused caching structure
    
    # Tuple unpacking with irrelevant variables
    alpha, beta, gamma = 12, 24, 36
    
    # Real work begins
    filtered = [x for x in input_seq if x != 0 and abs(x) < 1000]
    
    # Conditional manipulation based on global pattern
    if sum(1 for x in filtered if x < 0) > len(filtered) // 3:
        filtered = [abs(x) for x in filtered]
    
    # Apply lambda-based transformation
    transform_fn = lambda z: z * 2 if z < 50 else z + 10
    enhanced = [transform_fn(x) for x in filtered]
    
    # Introduce misleading statistical measures
    mean_val = sum(enhanced) / len(enhanced)
    variance_proxy = sum((x - mean_val) ** 2 for x in enhanced) / len(enhanced)
    peak = max(enhanced)
    
    # Real logic continues: nested filtering and analysis
    integrity_score = analyze_signal_integrity(enhanced)
    
    # Secondary decoy calculation
    entropy_approx = 0.0
    for x in enhanced:
        if x > 0:
            entropy_approx += math.log(x) * (x / sum(enhanced))
    
    # Final computation involving multiple concepts
    scaling_factor = len(set(enhanced))  # Cardinality factor
    stability_bias = abs(integrity_score) // 10
    final_value = (integrity_score + peak) * scaling_factor - stability_bias
    
    # Key assignment point
    final_output = final_value & 0x7FFFFFFF  # Ensure positive 31-bit integer
    return final_output

# Simulated sensor data stream (contains noise and valid signals)
data_stream = [0, -5, 12, 9, 24, 15, 8, 3, 6, 21, 18, 7, 14, 10, 11, 13, 19, 22, 25, 26, 27, 28, 29, 30]

# Execution entry point
final_output = process_pipeline(data_stream)
print(f"Result: {final_output}")