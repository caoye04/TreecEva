import math

def analyze_redundant_stats(data):
    # Distractor function: looks important but unused
    total = sum(data)
    return [x / total for x in data if x > 0]

def compute_legacy_weighting(x, y):
    # Dead code path — never called
    return (x * 0.3) + (y * 0.7)

def utility_checksum(arr):
    # Irrelevant computation with misleading name
    checksum = 0
    for i, val in enumerate(arr):
        checksum ^= (val + i) % 256
    return checksum

def filter_outliers(sequence, threshold=2):
    mean_val = sum(sequence) / len(sequence)
    std_dev = (sum((x - mean_val) ** 2 for x in sequence) / len(sequence)) ** 0.5
    return [x for x in sequence if abs(x - mean_val) <= threshold * std_dev]

def transform_metrics(raw_entries):
    # Mix of relevant and irrelevant transformations
    transformed = {}
    temp_store = []
    
    for key, values in raw_entries.items():
        if key == 'latency':
            cleaned = filter_outliers([v for v in values if v > 0])
            avg_latency = sum(cleaned) / len(cleaned) if cleaned else 0
            transformed['response_time'] = 1 / (avg_latency + 1e-6)
        elif key == 'throughput':
            capped = [min(v, 1000) for v in values]
            transformed['bandwidth_efficiency'] = sum(capped) / 100.0
        elif key == 'errors':
            error_rate = sum(1 for e in values if e != 0) / len(values)
            transformed['stability_index'] = (1 - error_rate) * 100
    
    # Red herring dictionary update
    transformed['placeholder_metric'] = 42  
    transformed['debug_flag'] = False
    
    # Real dependency: used later
    transformed['size_factor'] = len(temp_store) + 5
    
    return transformed

def generate_synthetic_trace(n):
    # Unused complex generator — distractor
    trace = [1]
    for i in range(1, n):
        trace.append(trace[-1] + (i % 3))
    return trace

def evaluate_performance(log, config):
    # Core logic embedded in noise
    base_weight = config.get('base_weight', 0.5)
    penalty_factor = config.get('penalty', 1.2)
    
    score_components = []
    
    # Real calculation chain
    rt = log.get('response_time', 0)
    be = log.get('bandwidth_efficiency', 0)
    si = log.get('stability_index', 0)
    sf = log.get('size_factor', 1)
    
    intermediate = (rt * 2.1) + (be * 1.7)
    adjusted = intermediate * (si / 100.0)
    
    # Misleading normalization that isn't actually applied
    fake_norm = adjusted / (math.sqrt(rt**2 + be**2) + 1e-8)
    
    # Actual scoring formula
    raw_score = adjusted * sf
    
    # Conditional penalty based on decoy flag
    if log.get('debug_flag'):  # Always False — red herring
        raw_score *= 0.8
    
    # Final transformation
    final = int(base_weight * raw_score) - int(penalty_factor * 10)
    
    # Unused variables to increase confusion
    dummy_map = {i: chr(97 + (i % 26)) for i in range(20)}
    temp_result = [math.log(abs(final) + 1)] * 3
    
    return final

# Main execution flow
if __name__ == '__main__':
    # Simulated system metrics log (real input)
    metrics_log = {
        'latency': [120, 115, 130, 150, 90, 200, 110],  # 200 is outlier
        'throughput': [800, 850, 900, 950, 1000, 1100],     # capped at 1000
        'errors': [0, 1, 0, 0, 2, 0, 0, 1]
    }
    
    # Baseline configuration with subtle influence
    baseline_config = {
        'base_weight': 0.6,
        'penalty': 1.5,
        'activation_threshold': 0.8,
        'legacy_mode': False
    }
    
    # Irrelevant preprocessing steps
    flattened = [item for sublist in [metrics_log[k] for k in ['latency', 'throughput', 'errors']] for item in sublist]
    checksum_value = utility_checksum(flattened[:10])
    
    # Another decoy structure
    audit_trail = set()
    audit_trail.add('stage_1')
    audit_trail.add('stage_2')
    
    processed_metrics = transform_metrics(metrics_log)
    
    # Critical execution point
    final_score = evaluate_performance(processed_metrics, baseline_config)
    
    # Additional distraction
    history_stack = [{'action': 'init'}, {'action': 'transform'}]
    for entry in history_stack:
        entry['timestamp'] = 1623456789
    
    print(f"Result: {final_score}")