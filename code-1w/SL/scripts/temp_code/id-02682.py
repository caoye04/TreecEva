import itertools

def analyze_component_health(health_signals):
    # Irrelevant function: analyzes health but not used in final computation
    weights = [0.1, 0.3, 0.4, 0.2]
    weighted_sum = sum(h * w for h, w in zip(health_signals, weights))
    return weighted_sum > 0.6

def compute_entropy(values):
    # Distractor function: computes entropy but unused
    from math import log
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * log(p) for p in probs)

def transform_sequence(seq):
    # Unused transformation path
    shifted = [(x >> 1) ^ 0b101 for x in seq]
    return [y + 2 for y in shifted if y % 3 != 0]

def filter_outliers(data, threshold=3.5):
    # Dead code path — looks useful but not used
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    return [x for x in data if abs(x - mean_val) / std_dev < threshold]

def generate_synthetic_metrics(n):
    # Generates unused synthetic data
    return [(i * 17) % 19 + (i // 5) for i in range(n)]

def validate_stability_log(log_entries):
    # Misleading validation logic
    for entry in log_entries:
        if 'ERROR' in entry:
            return False
    return True

def recursive_reduce(n, acc=1):
    # Decoy recursive function
    if n <= 1:
        return acc
    return recursive_reduce(n - 2, acc * (n % 7 + 1))

def evaluate_performance(metrics, ref_data):
    # Core logic hidden among distractions
    base = sum(m * 0.5 for m in metrics if m > 4)
    
    # Real manipulation using lambda and itertools
    paired = list(itertools.zip_longest(metrics, ref_data, fillvalue=1))
    adjustments = map(lambda x: (x[0] ** 0.5) - (x[1] // 4), paired)
    
    # Key intermediate calculation
    adjusted_total = base + sum(a for a in adjustments if a > -2)
    
    # Conditional bit manipulation relevant to final result
    flag = len(metrics) & 7
    if flag > 4:
        adjusted_total = adjusted_total ^ 0b1101
    else:
        adjusted_total = adjusted_total | 0b101
    
    # Final scaling based on actual logic chain
    scale_factor = len(list(itertools.takewhile(lambda x: x < 10, ref_data)))
    final_value = int(adjusted_total * scale_factor) + 13
    
    # Red herring: another variable with similar name
    final_score_temp = final_value + 999  # Not used
    
    return final_value

# --- Main execution ---
if __name__ == "__main__":
    # Real input data
    metrics = [8, 6, 5, 9, 3, 7]
    benchmark_data = [12, 5, 8, 3, 15, 7, 2]
    
    # Irrelevant variables and operations
    system_status = [True, False, True]
    config_flags = {'debug': False, 'trace': 1, 'mode': 'prod'}
    temp_results = [compute_entropy([4, 5, 6]), compute_entropy([1, 1, 1])]
    
    # Fake pipeline that does nothing
    synthetic_metrics = generate_synthetic_metrics(10)
    filtered_metrics = filter_outliers(synthetic_metrics)
    
    # Actual critical call
    final_score = evaluate_performance(metrics, benchmark_data)
    
    # Unused complex structure
    log_stream = ['INFO:OK', 'DEBUG:LOW', 'INFO:OK']
    is_stable = validate_stability_log(log_stream)
    
    # Output only the target result
    print(f"Target result: {final_score}")