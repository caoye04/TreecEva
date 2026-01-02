from collections import defaultdict
import math

# Irrelevant helper function (dead code path)
def unused_diagnostic(data):
    return sum(x ** 2 for x in data if x > 0) / len(data)

# Distractor variables
temp_cache = [0] * 100
buffer_overflow_sim = 2 ** 16
dummy_flag = True
useless_threshold = 0.0001
offset_correction = 3.14159

# Real data structures
metrics = {
    'latency': 120,
    'throughput': 850,
    'error_rate': 0.02,
    'jitter': 15,
    'bandwidth': 92
}

baseline = {
    'latency': 100,
    'throughput': 1000,
    'error_rate': 0.01,
    'jitter': 10
}

# Misleading intermediate calculation (not used in final result)
phantom_score = 0
for k in metrics:
    if k in ['latency', 'jitter']:
        phantom_score += metrics[k] // 10
    elif k == 'bandwidth':
        phantom_score += int(math.sqrt(metrics[k]))

# Unused lambda (red herring)
complexity_weight = lambda x: x ** 0.5 if x > 5 else x

# Core logic disguised among distractors
def normalize(value, base):
    return (base - value) / base if value < base else -abs(value - base) / base

def calculate_deviation_score(data, base):
    score = 0.0
    for key in base:
        if key in data:
            deviation = normalize(data[key], base[key])
            if key == 'throughput':
                score += deviation * 1.5
            elif key == 'error_rate':
                score += deviation * 2.0
            else:
                score += deviation
    return score

# Recursive adjustment (minor relevance)
def recursive_adjust(val, depth):
    if depth <= 0 or val > 1e-5:
        return val
    return recursive_adjust(val * 2, depth - 1)

# Another decoy function
def analyze_outliers(seq):
    count = 0
    for i in range(1, len(seq)-1):
        if seq[i] > seq[i-1] and seq[i] > seq[i+1]:
            count += 1
    return count

# Main evaluation logic buried in noise
def evaluate_performance(met, base):
    raw_score = calculate_deviation_score(met, base)
    
    # Redundant dictionary processing (distractor)
    summary = defaultdict(int)
    for k, v in met.items():
        if isinstance(v, int):
            summary['ints'] += 1
        elif isinstance(v, float):
            summary['floats'] += 1
    
    # Key adjustment using lambda (actual use)
    modifier = (lambda x: x * 100)(recursive_adjust(abs(raw_score), 5))
    
    # Hidden critical operation: bandwidth is NOT in baseline, so it's extra credit
    bonus = 0
    if 'bandwidth' in met and 'bandwidth' not in base:
        bonus = met['bandwidth'] // 100  # 92 // 100 = 0? No — wait, 92//100=0, but let's fake complexity
        bonus = int(round(met['bandwidth'] / 115 * 10))  # Normalized to max possible 10
    
    # Actual formula: -raw_score * 100 + bonus
    result = abs(modifier) + bonus  # But modifier is positive due to abs()
    
    # Final twist: we actually return the negative of expected direction
    return int(round(-result * 10))  # Inverted scale for penalty-based system

# Critical execution point
final_score = evaluate_performance(metrics, baseline)

# Print required output
print(f"Target result: {final_score}")