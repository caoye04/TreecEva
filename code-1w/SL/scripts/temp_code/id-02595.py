from collections import defaultdict, Counter
import math

# Simulated sensor data processing with diagnostic analysis
def acquire_signal_data():
    raw_samples = [3, 5, 7, 11, 13, 17, 19, 23]
    metadata_map = defaultdict(lambda: 'unknown')
    for i, val in enumerate(raw_samples):
        metadata_map[f'sensor_{i}'] = f'region_{i % 4}'
    return raw_samples, metadata_map

def filter_outliers(data, threshold=15):
    filtered = [x for x in data if x <= threshold]
    outlier_count = len(data) - len(filtered)
    # Distractor: irrelevant transformation
    temp_analysis = [x ** 0.5 for x in data if x % 2 == 0]
    return filtered

def transform_magnitude(x):
    if x < 5:
        return x * 3
    elif x < 10:
        return x * 2 + 1
    else:
        return x + 5

def process_signal_set(samples):
    # Real processing path
    stage1 = [transform_magnitude(x) for x in samples]
    stage2 = [x for x in stage1 if x % 2 == 1]  # Keep only odd values
    
    # Distractor: dead code path (never used)
    debug_stats = {}
    if len(stage2) > 100:
        debug_stats['peak'] = max(stage2)
        debug_stats['entropy'] = sum([x * math.log(x) for x in stage2])
    
    # Distractor: irrelevant string operation
    status_flag = 'normal'
    status_flag = status_flag.replace('normal', 'verified').upper().strip()
    
    # Real computation
    shift_key = 3
    shifted = [((x << 1) ^ 5) & 63 for x in stage2]  # Bit manipulation
    return shifted

def generate_synthetic_references(base_list):
    # Distractor function: generates unused synthetic data
    ref_grid = []
    for i in range(4):
        row = [(i * 8) + j for j in range(8)]
        ref_grid.append(row)
    checksum = sum(sum(row) for row in ref_grid) % 1000
    return checksum  # Unused later

def count_pattern_occurrences(signal):
    # Distractor: counts patterns that aren't relevant to final result
    pairs = [(signal[i], signal[i+1]) for i in range(len(signal)-1)]
    pair_counter = Counter(pairs)
    rare_pairs = [p for p, cnt in pair_counter.items() if cnt == 1]
    return len(rare_pairs)  # Not used in main logic

def analyze_readings(processed):
    # Core logic begins here
    base_score = sum(processed)
    length_factor = len(processed) if len(processed) > 0 else 1
    
    # Apply decay based on sequence properties
    decay_modifier = 1.0
    if any(x > 50 for x in processed):
        decay_modifier *= 0.9
    if all(x % 3 != 0 for x in processed):
        decay_modifier *= 1.1
    
    # Real branching logic
    if base_score > 300:
        intermediate = base_score * 0.85
    else:
        intermediate = base_score * 1.05
    
    # Additional transformation
    temp_result = math.floor(intermediate / length_factor)
    adjustment = 7 if temp_result % 2 == 0 else 11
    final_diagnostic = temp_result + adjustment
    
    # Distractor: unused conditional with complex logic
    if final_diagnostic < 100 and any(x in [17, 23, 41] for x in processed):
        alt_path = lambda a, b: (a ** b) % 19
        fallback = alt_path(final_diagnostic, 3)
    
    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    # Step 1: Acquire data
    samples, meta = acquire_signal_data()
    
    # Step 2: Filter outliers (removes 17, 19, 23)
    cleaned = filter_outliers(samples)
    
    # Step 3: Process signal (applies magnitude transform)
    processed_signals = process_signal_set(cleaned)
    
    # Irrelevant side computations (distractors)
    synthetic_ref = generate_synthetic_references(processed_signals)
    pattern_count = count_pattern_occurrences(processed_signals)
    
    # Key statement: this determines the answer
    final_diagnostic = analyze_readings(processed_signals)
    
    # Output result
    print(f"Result: {final_diagnostic}")