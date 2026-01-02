from collections import defaultdict, Counter

import math

def preprocess_data(raw):
    # Normalize and filter data points
    normalized = []
    for val in raw:
        if val < 0:
            val = abs(val)
        normalized.append(round(math.sqrt(val) * 2.5, 2))
    return normalized

def analyze_patterns(seq):
    freq = Counter(seq)
    mode_val = freq.most_common(1)[0][1]
    unique_count = len(freq)
    
    # Distractor: irrelevant pattern tracking
    runs = 0
    prev = None
    for x in seq:
        if x == prev:
            runs += 1
        prev = x
    
    # Semi-relevant transformation
    adjusted_freq = defaultdict(int)
    for k, v in freq.items():
        adjusted_freq[k] += v * 1.5
    
    return mode_val, unique_count, adjusted_freq

def evaluate_threshold_compliance(values, limits):
    count = 0
    soft_violations = 0
    hard_limit = limits['hard']
    warn_limit = limits['warn']
    
    for v in values:
        if v > hard_limit:
            count += 1
        elif v > warn_limit:
            soft_violations += 1
    
    # Dead code path - never used later
    if soft_violations > 10:
        status_flag = "REVIEW_NEEDED"
    else:
        status_flag = "OK"
        
    return count

def calculate_final_score(dataset, thresholds):
    processed = preprocess_data(dataset)
    mode, uniqueness, _ = analyze_patterns(processed)
    
    # Irrelevant scaling
    scaled_mode = mode * 1.1
    
    hard_failures = evaluate_threshold_compliance(processed, thresholds)
    
    # Key logic chain
    base_score = 100
    deduction_per_failure = 7
    uniqueness_bonus = int(uniqueness * 1.8)
    
    intermediate = base_score - (hard_failures * deduction_per_failure)
    temp_result = intermediate + uniqueness_bonus
    
    # Extra computation that looks important but isn't fully used
    max_possible = base_score + (uniqueness * 2)
    efficiency_ratio = temp_result / max_possible
    
    # Final score with red herring variables
    final_score = int(temp_result + (efficiency_ratio * 5))
    
    # Additional misleading calculation
    projected = final_score * 1.05
    trend_analysis = f"GROWING" if projected > 100 else "STABLE"
    
    return final_score

# Main execution
raw_data = [16, 25, 9, 16, 4, 25, 36, 49, 64, 81, 100, 121, 144]
config = {
    'hard': 15.0,
    'warn': 10.0
}

result_tracker = {}
stats_summary = []

# Simulate side processing (distractor)
for i in range(3):
    dummy = [x ** 0.5 for x in raw_data if x % (i+1) == 0]
    stats_summary.append(len(dummy))

final_score = calculate_final_score(raw_data, config)
print(f"Result: {final_score}")