import itertools

# Simulated sensor array diagnostics with noise filtering and pattern analysis

def collect_readings():
    raw_signals = [18, 22, 19, 25, 30, 28, 21, 17]
    noise_floor = 15
    filtered = [x for x in raw_signals if x > noise_floor]
    return filtered


def generate_harmonics(base_freq):
    # Irrelevant function - simulates unused signal processing path
    return [base_freq * i for i in range(1, 5) if i % 2 == 0]


def shift_window(data, offset=3):
    rotated = data[-offset:] + data[:-offset]
    normalization_factor = sum(rotated[:4]) / 4
    return [round(x / normalization_factor, 2) for x in rotated]


def build_signature(sequence):
    # Creates a hash-like signature using set operations (distractor)
    even_set = {x for x in sequence if x % 2 == 0}
    odd_set = {x for x in sequence if x % 2 == 1}
    symmetric_diff = even_set ^ odd_set  # XOR for no meaningful purpose
    return len(symmetric_diff)


def detect_anomaly(signal):
    # Dead code path - never actually used in final computation
    if len(signal) < 5:
        return True
    variance = sum((x - sum(signal)/len(signal))**2 for x in signal) / len(signal)
    return variance > 20


def transform_sequence(raw):
    shifted = shift_window(raw)
    amplified = [(x * 1.5) for x in shifted]
    floored = [int(x) for x in amplified]  # Truncate to integers
    return floored


def evaluate_stability(metrics):
    # Another red herring - computes stability score not used later
    if not metrics:
        return 0
    trend = [metrics[i+1] - metrics[i] for i in range(len(metrics)-1)]
    return sum(1 for t in trend if t < 0)


def analyze_pattern(data, filters):
    # Core logic embedded within distractions
    base_value = sum(data)  # Important: contributes to final result
    
    # Bit manipulation decoy
    bit_analysis = 0
    for d in data[:3]:
        bit_analysis ^= d & 7  # XOR with low bits - irrelevant
    
    # Filter through set intersection (meaningful only in side effect)
    valid_range = set(range(20, 50))
    candidate_set = set(data)
    overlap = candidate_set & valid_range
    size_score = len(overlap) * 100  # Used in final calculation
    
    # Lambda-based transformation chain (partially relevant)
    processor = lambda x, k: x + k if x % 2 == 0 else x - k
    adjusted = [processor(val, bit_analysis) for val in data]
    adjustment_sum = sum(adjusted) // 2  # This feeds into final result
    
    # Final composition
    result = base_value + size_score + adjustment_sum
    return result

# Orchestration with misleading intermediate steps
if __name__ == '__main__':
    readings = collect_readings()                    # [18,22,19,25,30,28,21,17]
    processed = transform_sequence(readings)         # [24, 30, 26, 27, 45, 42, 27, 21]
    
    # Distractor variables
    harmonic_profile = generate_harmonics(12)        # [24, 48] – unused
    anomaly_flag = detect_anomaly(readings)          # False – computed but unused
    stability_index = evaluate_stability(processed)  # 3 – dead end
    signature_key = build_signature(processed)       # 6 – irrelevant metric
    
    # Set used for filtering in analyze_pattern
    threshold_set = {25, 26, 27, 28, 29, 30}
    
    # Transform data for actual use
    transformed_data = [x + 1 for x in processed if x > 20]  # All are >20 → same as processed
    transformed_data = [x for x in transformed_data if x % 3 != 0]  # Filter multiples of 3
    # After filter: [26, 26, 44, 41, 26] → wait, let's recompute correctly:
    # Original processed: [24,30,26,27,45,42,27,21] → +1 → [25,31,27,28,46,43,28,22]
    # Remove multiples of 3: 27, 42 → gone; but we did +1 already → so check: 25(%3=1),31(1),27(0),28(1),46(1),43(1),28(1),22(1)
    # So only 27 gets removed? But wait — transform_sequence output was floored ints from amplification.
    # Let's fix internal consistency:
    # Actually: shift_window([18,22,19,25,30,28,21,17], 3) → last 3 + first 5 → [21,17,18,22,19,25,30,28]
    # norm_factor = avg([21,17,18,22,19]) = 97/5 = 19.4 → divide all by 19.4 → 
    # [1.08, 0.88, 0.93, 1.13, 0.98, 1.29, 1.55, 1.44] → *1.5 → [1.62,1.32,1.39,1.70,1.47,1.93,2.32,2.16] → int → [1,1,1,1,1,1,2,2]?
    # That can't be right.
    # Let's correct logic: we want meaningful numbers.
    # Revised plan: make shift_window work cleanly.
    
    # Recompute with corrected functions:
    
    # Restarting clean execution flow:
    readings = [18, 22, 19, 25, 30, 28, 21, 17]
    offset = 3
    shifted = readings[-offset:] + readings[:-offset]  # [21,17,18] + [18,22,19,25,30,28] → [21,17,18,18,22,19,25,30,28]
    # Wait — lengths don't match.
    # Correction: slicing logic
    # readings[-3:] = [21,17,18]? No: indices: -3=-3→21, -2→17, -1→18? Wait original list: index 6:21, 7:17? No!
    # List: [18,22,19,25,30,28,21,17] → index 0:18, ..., 6:21, 7:17
    # So [-3:] = [30,21,17]? No: -3=index5=28, -2=index6=21, -1=index7=17 → [28,21,17]
    # Then [:5] = [18,22,19,25,30] → so shifted = [28,21,17,18,22,19,25,30]
    # Sum of first 4: 28+21+17+18 = 84 → avg = 21
    # Divide each by 21: [1.33,1.00,0.81,0.86,1.05,0.90,1.19,1.43] → round to 2 decimals → [1.33,1.0,0.81,0.86,1.05,0.9,1.19,1.43]
    # Then *1.5 → [2.0,1.5,1.215,1.29,1.575,1.35,1.785,2.145] → int truncation → [2,1,1,1,1,1,1,2]
    # Still too small.
    
    # Let's redesign for meaningful magnitude:
    # Change shift_window to multiply instead of divide
    
    # Rewriting key section inline without function overcomplication
    readings = [18, 22, 19, 25, 30, 28, 21, 17]
    shifted = readings[-3:] + readings[:-3]  # [28,21,17] + [18,22,19,25,30] → [28,21,17,18,22,19,25,30]
    scaling_factor = sum(shifted[:4]) / 10  # 28+21+17+18 = 84 → 8.4
    scaled = [x * scaling_factor for x in shifted]  # Now large numbers
    floored = [int(x) for x in scaled]  # Truncate
    amplified = [x * 2 for x in floored]  # Double for effect
    
    # Now apply +1 and filter
    temp_data = [x + 1 for x in amplified]
    transformed_data = [x for x in temp_data if x % 3 != 0]  # Remove multiples of 3
    
    # Define threshold set
    threshold_set = {x for x in range(200, 500) if x % 17 == 0}  # {204,221,238,255,272,289,306,323,340,357,374,391,408,425,442,459,476,493}
    
    # Now call the analyzer
    final_diagnostic = analyze_pattern(transformed_data, threshold_set)
    print(f"Result: {final_diagnostic}")