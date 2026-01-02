import itertools

# Simulated sensor data processing with red herrings and distractions
def preprocess_stream(raw_signal):
    filtered = [x for x in raw_signal if x > -50 and x < 50]
    shifted = [x - 7 for x in filtered]
    return shifted

# Irrelevant transformation - dead end function (distractor)
def obsolete_filter(sequence):
    return [x for x in sequence if x % 3 == 0]

# Core pattern analysis function
def analyze_pattern(data, limit):
    # Step 1: Compute moving average over window size 3
    moving_averages = []
    for i in range(len(data) - 2):
        avg = sum(data[i:i+3]) / 3
        moving_averages.append(round(avg, 2))
    
    # Step 2: Identify peaks above threshold
    peaks = [val for val in moving_averages if val > limit]
    
    # Step 3: Apply bitmask filter based on peak parity (bit manipulation red herring)
    masked_peaks = []
    mask = 0b101
    for p in peaks:
        int_part = int(abs(p))
        if bin(int_part & mask).count('1') >= 2:  # Real but subtle influence
            masked_peaks.append(p)
    
    # Step 4: Accumulate weighted contribution
    total = 0.0
    weights = itertools.cycle([0.8, 1.1, 0.9])
    for val, w in zip(masked_peaks, weights):
        total += val * w
    
    # Step 5: Final adjustment using distractor variables
    adjustment_factor = 1.0
    decoy_sum = sum([i**2 for i in range(6)])  # 55 - looks important
    phantom_offset = len([x for x in data if x < 0]) * 0.01  # Minor red herring
    final_score = total - phantom_offset  # Not actually used
    
    # ACTUAL result computation
    base_result = sum(masked_peaks) + len(peaks)
    return round(base_result, 4)

# Unused diagnostic functions (dead code paths)
def legacy_diagnostic(x):
    return (x >> 2) ^ 0xFF

def compute_entropy(seq):
    from math import log
    freq = {}
    for s in seq:
        freq[s] = freq.get(s, 0) + 1
    entropy = 0
    for f in freq.values():
        p = f / len(seq)
        entropy -= p * log(p, 2)
    return entropy

# Main execution flow
if __name__ == '__main__':
    # Initial dataset
    sensor_readings = [12, 15, 9, -8, 23, 27, 30, 11, -4, 19, 22, 25, 7, 3]
    
    # Distractor variables
    calibration_sequence = list(itertools.accumulate([1, -2, 3, -1, 2]))  # [1, -1, 2, 1, 3]
    reference_key = {i: i*3 for i in range(7)}  # Unused mapping
    temp_buffer = preprocess_stream(sensor_readings)  # [-8, 23, 27, 30, 11, -4, 19, 22, 25, 7, 3]
    
    # Real data transformation path
    amplified = [x * 1.5 for x in sensor_readings if x > 10]  # Only high signals
    normalized = [round(x / 1.5, 1) for x in amplified]  # Should reconstruct original
    
    # Critical transformation
    transformed_data = [int(x * 1.1) for x in amplified]  # Subtle distortion
    
    # Threshold computed via irrelevant logic chain
    baseline = sum(normalized) / len(normalized)
    noise_floor = max(transformed_data) * 0.1
    threshold = baseline * 0.4 + noise_floor  # ~13.5
    
    # Decoy operations
    _ = obsolete_filter(transformed_data)
    _ = [legacy_diagnostic(x) for x in transformed_data]
    
    # Key statement
    final_diagnostic = analyze_pattern(transformed_data, threshold)
    
    # Output target
    print(f"Result: {final_diagnostic}")