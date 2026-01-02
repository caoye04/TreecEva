from collections import defaultdict
from itertools import combinations
import math

# Simulated system metrics with irrelevant and relevant data
def generate_metrics():
    data = defaultdict(float)
    data['latency_ms'] = 120.5
    data['throughput_ops'] = 850
    data['error_rate'] = 0.034
    data['memory_mb'] = 420.8
    data['cpu_temp_c'] = 68.2  # Irrelevant
    data['disk_reads'] = 1200  # Irrelevant
    data['cache_hit_ratio'] = 0.88
    data['packet_loss'] = 0.002
    data['context_switches'] = 987  # Irrelevant
    data['thread_count'] = 32  # Irrelevant
    return data

# Weight configuration (some weights are decoys)
def get_weights():
    w = {}
    w['latency_ms'] = -0.3
    w['throughput_ops'] = 0.4
    w['error_rate'] = -0.25
    w['cache_hit_ratio'] = 0.35
    w['packet_loss'] = -0.1
    # Below weights are for non-existent metrics (red herrings)
    w['bandwidth_mbps'] = 0.2  # Not in data
    w['gpu_util'] = 0.15  # Not in data
    w['swap_usage'] = -0.05  # Not in data
    return w

# Auxiliary function – calculates entropy of a sequence (distractor)
def calculate_entropy(seq):
    freq = defaultdict(int)
    for item in seq:
        freq[item] += 1
    total = len(seq)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

# Another red herring: generates Fibonacci-like sequence up to n
def fib_sequence(n):
    if n <= 0:
        return []
    seq = [1, 1]
    while seq[-1] < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:-1]

# Decoy function that appears related but isn't used in final calculation
def normalize(value, min_val=0, max_val=100):
    return (value - min_val) / (max_val - min_val) if max_val > min_val else 0

# Real evaluation logic with interference from unused branches
def score_component(value, weight, ideal_range=None):
    base_score = value * weight
    
    # Irrelevant adjustment branch (never triggered in practice)
    if isinstance(ideal_range, tuple) and len(ideal_range) == 2:
        low, high = ideal_range
        if value < low:
            base_score *= 0.9
        elif value > high:
            base_score *= 0.85
    
    # This branch is also unreachable due to input types
    if math.isinf(base_score) or math.isnan(base_score):
        return 0.0  # Dead code
    
    return base_score

# Main evaluation function with misleading complexity
def evaluate_performance(metrics, weights):
    raw_contributions = []
    missing_penalty = 0.0
    
    # Real components (subset of all metrics)
    relevant_keys = [
        'latency_ms',
        'throughput_ops',
        'error_rate',
        'cache_hit_ratio',
        'packet_loss'
    ]
    
    # Spurious use of set operations (has no effect on result)
    provided_set = set(metrics.keys())
    required_set = set(relevant_keys)
    extra_keys = provided_set - required_set  # Unused
    missing_keys = required_set - provided_set  # Used only for show
    
    # Fake validation that doesn't alter flow
    if len(missing_keys) > 0:
        missing_penalty = -0.5 * len(missing_keys)  # Never applied
    
    # Use of itertools: generate meaningless pairs (distraction)
    combo_sum = 0.0
    for a, b in combinations([metrics[k] for k in ['latency_ms', 'error_rate', 'packet_loss']], 2):
        combo_sum += abs(a - b) * 0.01  # Minor distraction
    
    # Actual scoring happens here, but buried in noise
    component_total = 0.0
    for key in relevant_keys:
        if key in metrics and key in weights:
            comp = score_component(metrics[key], weights[key])
            raw_contributions.append(comp)
            component_total += comp
    
    # Final aggregation with irrelevant transformations
    aggregate = sum(raw_contributions)
    
    # Apply irrelevant transformation chain
    temp_result = aggregate * 100
    temp_result = round(temp_result, 2)
    temp_result = max(temp_result, -500)  # Artificial bound (not needed)
    temp_result = min(temp_result, 500)   # Artificial bound (not needed)
    
    # Add unrelated combinatorial offset (evaluates to constant)
    chars = ['a', 'b', 'c', 'd']
    anagram_count = len(list(combinations(chars, 2)))  # Always 6
    anagram_score = anagram_count * 0.1  # 0.6, looks meaningful
    
    # Real answer formation
    final_normalized = temp_result + anagram_score + combo_sum
    
    # Dead code path based on impossible condition
    sentinel_flag = False
    if math.sqrt(-1) == 1j:  # Never true in real float math
        final_normalized = complex(final_normalized, 1)
    
    # Key output variable
    final_score = int(round(final_normalized))
    
    # Print required at end
    print(f"Result: {final_score}")
    return final_score

# Execution flow
if __name__ == "__main__":
    # Generate realistic data
    metrics = generate_metrics()
    weights = get_weights()
    
    # Irrelevant pre-processing step
    sorted_keys = sorted(metrics.keys())
    avg_metric = sum(metrics.values()) / len(metrics)  # Unused
    
    # Additional distraction: entropy of key lengths
    key_lengths = [len(k) for k in metrics.keys()]
    entropy = calculate_entropy(key_lengths)  # Not used
    
    # Fibonacci of something (decoy)
    fib_vals = fib_sequence(100)  # Unused
    
    # Critical execution point
    final_score = evaluate_performance(metrics, weights)