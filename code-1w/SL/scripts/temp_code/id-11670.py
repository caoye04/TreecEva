from itertools import compress, count

def analyze_sequence(seq):
    # Irrelevant transformation: counts vowels in string representations (distractor)
    vowel_count = sum(1 for c in str(seq) if c.lower() in 'aeiou')
    
    # Semi-relevant processing: filter even-indexed elements
    indices = range(len(seq))
    filtered = list(compress(seq, [i % 2 == 0 for i in indices]))
    
    # Secondary distraction: reverse but don't use
    reversed_seq = seq[::-1]
    temp_sum = sum(filtered) * 0.5  # Used later but scaled down
    
    return temp_sum

def validate_stability(data):
    # Distractor function: computes variance but only returns a flag
    mean_val = sum(data) / len(data) if data else 0
    variance = sum((x - mean_val) ** 2 for x in data) / len(data) if data else 0
    is_stable = variance < 50
    
    # Fake complexity: simulate threshold adjustments
    thresholds = [mean_val * 0.1 * i for i in range(1, 6)]
    active_thresholds = [t for t in thresholds if t > 5]
    
    return is_stable  # unused in final logic

def calculate_performance(raw):
    # Core logic begins
    base_values = [x for x in raw if x > 0]  # Filter positives
    shifted = [x << 1 for x in base_values]  # Bitwise left shift by 1 (×2)
    
    # Use slicing to take middle portion
    mid_section = shifted[len(shifted)//4 : len(shifted)*3//4]
    
    # Analyze sequence returns half-sum of even indices from original
    partial = analyze_sequence(base_values)
    
    # Conditional adjustment based on length (dummy check)
    adjustment = 0
    if len(mid_section) > 3:
        adjustment = 5
        extra_calc = sum(mid_section[i] for i in range(0, len(mid_section), 3)) // 2
        adjustment += extra_calc % 7
    
    # Accumulate score
    raw_score = sum(mid_section) + partial
    scaling_factor = 1.25
    
    # Final computation
    final_score = int((raw_score + adjustment) * scaling_factor)
    
    # Dead code: this block is never reached (red herring)
    if False:
        backup = sum(base_values) * 2
        final_score = backup
    
    return final_score

# Main execution
benchmark_data = [3, 8, -2, 12, 7, 4, 9, 1, 0, 6]
dummy_mask = [True, False, True]
ignored_result = validate_stability(benchmark_data)

final_score = calculate_performance(benchmark_data)
print(f"Target result: {final_score}")