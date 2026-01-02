import itertools
from collections import defaultdict, Counter

# Simulated system performance evaluation with multiple distractors
def analyze_component_load(logs):
    # Irrelevant function - dead code path
    return sum(len(log) for log in logs) * 0.5

def calculate_theoretical_limit(n):
    # Misleading computation - not actually used in final logic
    if n < 2:
        return 1
    return calculate_theoretical_limit(n-1) + calculate_theoretical_limit(n-2)

def filter_anomalies(data, threshold=0.95):
    # Unused function - red herring
    return [x for x in data if x > threshold]

def shift_cipher(text, shift=3):
    # Decoy function performing bit manipulation and string ops (not relevant)
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            shifted = (ord(char) - base + shift) % 26
            result += chr(base + shifted)
        else:
            result += char
    return result

def evaluate_performance(metrics, benchmarks):
    # Core logic embedded within distractions
    temp_results = defaultdict(float)
    adjustment_factor = 0
    
    # Real but obscured logic begins here
    for key in benchmarks:
        if key in metrics:
            raw_val = metrics[key]
            norm_val = raw_val / (len(key) + 1)
            temp_results[key] = round(norm_val, 4)
    
    # Bitwise interference mask - looks important but only affects unused branch
    mask = 0b101010
    masked_values = [mask ^ i for i in range(5)]  # Distractor list
    
    # Conditional branch that appears critical but leads nowhere
    if sum(temp_results.values()) > 10:
        backup_weights = [0.1, 0.2, 0.3]
        adjustment_factor = sum(w ** 2 for w in backup_weights)
    else:
        adjustment_factor = 0.8  # This branch actually taken
    
    # Real calculation hidden among decoys
    base_score = 0
    for k, v in temp_results.items():
        if len(k) % 2 == 0:
            base_score += v * 1.1
        else:
            base_score += v * 0.9
    
    # Spurious use of itertools - looks like complex processing
    combinations = list(itertools.combinations_with_replacement([1,2], 2))
    bonus = len(combinations) * 0.05  # Minor fixed addition
    
    # Another decoy structure
    stats_summary = Counter()
    for key in metrics.keys():
        stats_summary[len(key)] += 1  # Computed but never used
    
    # Critical line: final_score depends on base_score, adjustment_factor, and bonus
    final_score = (base_score * adjustment_factor) + bonus
    
    # Print required output
    print(f"Result: {final_score}")
    return final_score

# Simulated input data - realistic naming
metrics = {
    'latency': 44,
    'throughput': 88,
    'reliability': 66,
    'scalability': 55
}

benchmarks = ['latency', 'throughput', 'efficiency', 'security', 'scalability']

# Unused variables - red herrings
system_log = [['error', 'timeout'], ['retry', 'success']]
analysis_cache = set()
theoretical_max = calculate_theoretical_limit(10)
cipher_key = shift_cipher('benchmark', 5)

# Key execution point
final_score = evaluate_performance(metrics, benchmarks)