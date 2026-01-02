from collections import defaultdict
import math

# Irrelevant helper function (decoy)
def analyze_sentiment(text):
    return sum(ord(c) for c in text) % 7

def process_user_data(raw_logs):
    # Distractor: unused data transformation
    user_stats = defaultdict(int)
    temp_cache = []
    for log in raw_logs:
        parts = log.split('-')
        event = parts[0]
        value = int(parts[1])
        user_stats[event] += value
        if value > 50:
            temp_cache.append(math.sqrt(value))  # Dead-end computation

    # Misleading intermediate
    aggregate = sum(user_stats.values()) * 0.85
    normalized = [x / (aggregate + 1e-6) for x in user_stats.values()]

    return user_stats

# Another red herring function
def validate_checksum(data_str):
    chk = 0
    for i, c in enumerate(data_str):
        chk ^= (ord(c) + i) % 256
    return chk % 10 == 0

# Core logic disguised among noise
def transform_features(features):
    # Complex but partially irrelevant transformation
    transformed = {}
    for k, v in features.items():
        if k.startswith('feat_'):
            transformed[k] = math.log(v + 1) * 2.3
        elif k == 'legacy_flag':
            continue  # Silent skip
        else:
            transformed[k] = v ** 0.5

    # List comprehension with decoy effect
    squares = [i*i for i in range(1, 10) if i % 3 != 0]

    return transformed

# Main evaluation with nested distractions
def evaluate_performance(metrics, weights):
    # Step 1: Filter relevant metrics
    valid_keys = [k for k in weights.keys() if k in metrics]
    
    # Step 2: Apply weights (core logic)
    weighted_sum = 0.0
    total_weight = 0.0
    
    for k in valid_keys:
        if k == 'latency_ms' and metrics[k] > 1000:  # Conditional penalty
            continue  # Skip poor performers
        weight = weights[k]
        weighted_sum += metrics[k] * weight
        total_weight += weight
    
    base_score = weighted_sum / (total_weight + 1e-8)
    
    # Distractor: unused bonus calculation
    bonus_pool = 0
    for m in metrics:
        if 'throughput' in m:
            bonus_pool += metrics[m] // 100
    adjustment = math.sin(bonus_pool)  # Never applied
    
    # Step 3: Apply non-linear scaling (key step)
    scaled_score = 100 * (1 - math.exp(-base_score / 50))
    
    # Step 4: Final adjustment based on hidden rule
    if 'errors' in metrics and metrics['errors'] == 0:
        scaled_score *= 1.1
    
    # Critical result
    final_score = int(round(scaled_score))
    
    # Unused complex structure
    debug_info = {
        'raw': {k: metrics[k] for k in metrics if k not in ['temp_debug', 'aux_val']},
        'flags': [k for k, v in metrics.items() if isinstance(v, bool) and v]
    }
    
    return final_score

# Simulated input data
if __name__ == '__main__':
    # Real input with noise
    system_metrics = {
        'latency_ms': 450,
        'throughput_rps': 230,
        'memory_usage_mb': 1024,
        'cpu_load_pct': 75,
        'errors': 0,
        'temp_debug': 999,  # Obvious decoy
        'aux_val': 'N/A'
    }
    
    weighting_scheme = {
        'latency_ms': 0.3,
        'throughput_rps': 0.4,
        'memory_usage_mb': 0.2,
        'cpu_load_pct': 0.1
    }
    
    # Call process_user_data with dummy data (dead path)
    dummy_logs = ['req-120', 'err-5', 'req-80']
    _ = process_user_data(dummy_logs)
    
    # Irrelevant string operation
    config_key = "auth|verify|encrypt"
    segments = config_key.split('|')
    key_hash = sum(len(s) for s in segments)
    
    # Actual target execution point
    final_score = evaluate_performance(system_metrics, weighting_scheme)
    
    # Print required output
    print(f"Result: {final_score}")