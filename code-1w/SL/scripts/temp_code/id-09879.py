import itertools

def analyze_workload(inputs):
    # Irrelevant function - dead code path
    return sum([x ** 2 for x in inputs if x > 5])

def compute_entropy(data):
    # Distractor: looks important but unused
    from math import log
    total = sum(data)
    if total == 0:
        return 0
    probs = [d / total for d in data]
    return -sum(p * log(p) for p in probs if p > 0)

def transform_sequence(seq):
    # Unused transformation with misleading intermediate values
    shifted = [(x << 2) & 0xFF for x in seq]
    inverted = [~x & 0xFF for x in shifted]
    return [inverted[i] ^ 0xAA for i in range(len(inverted)) if i % 3 == 0]

def filter_outliers(values, threshold=3.5):
    # Looks useful, but not actually used in main logic
    mean_val = sum(values) / len(values)
    std_dev = (sum((x - mean_val) ** 2 for x in values) / len(values)) ** 0.5
    return [v for v in values if abs(v - mean_val) / std_dev < threshold]

def evaluate_performance(metrics, base):
    # Core logic hidden among distractions
    adjusted = [m * 1.5 if m > base else m * 0.8 for m in metrics]
    
    # Bit manipulation red herring
    magic_flag = (len(adjusted) << 3) ^ 0x1F
    temp_result = 0
    for a in adjusted:
        temp_result += int(a) & 0x7F | (magic_flag >> 2)
    
    # Real computation buried here
    valid_entries = [x for x in adjusted if x > base * 0.9]
    
    # Conditional expression and itertools usage
    grouped = list(itertools.groupby(sorted(valid_entries), key=lambda x: int(x)))
    counts = [len(list(group)) for _, group in grouped]
    
    # More distraction: set operations on irrelevant derived values
    unique_caps = set(counts + [len(adjusted), len(valid_entries)])
    decoy_sum = sum({c ** 2 for c in unique_caps if c % 2 == 0})
    
    # Actual answer derivation
    primary_weight = len(valid_entries) > 4 else 0.6
    secondary_factor = 1.4 if sum(counts) > 8 else 1.1
    
    # Final calculation
    final_score = (sum(valid_entries) / len(valid_entries)) * primary_weight * secondary_factor
    
    # Print required output
    print(f"Result: {final_score}")
    return final_score

# Simulated telemetry data (distraction)
data_log = [23, 45, 12, 67, 89, 34, 56]
analyze_workload(data_log)

# Main input - only this matters
metrics = [10, 20, 30, 25, 35, 40]
baseline = 22

# Key execution point
final_score = evaluate_performance(metrics, baseline)