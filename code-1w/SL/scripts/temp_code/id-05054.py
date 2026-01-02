import math

def analyze_pattern(sequence):
    # Irrelevant function: analyzes sequence but not used in final computation
    if len(sequence) < 5:
        return False
    trend = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
    return all(x > 0 for x in trend)

# Decoy data structures
trend_data = [12, 15, 23, 34, 45]
user_profile = {
    'id': 'USR789',
    'access_level': 'admin',
    'preferences': {'theme': 'dark', 'notifications': True}
}

# Unused transformation function
def transform_input(data):
    normalized = [round((x - min(data)) / (max(data) - min(data)) * 100) for x in data]
    return [math.sqrt(val) for val in normalized if val > 10]

# Real metric processing
metric_data = {
    'accuracy': 87.5,
    'latency_ms': 42.0,
    'throughput': 210,
    'consistency': 94.3,
    'coverage': 76
}

user_weights = {
    'accuracy': 0.30,
    'latency_ms': -0.10,  # negative weight: lower latency improves score
    'throughput': 0.25,
    'consistency': 0.20,
    'coverage': 0.15
}

# Distractor: fake normalization that isn't used
raw_values = list(metric_data.values())
fake_normalized = [(val - min(raw_values)) / (max(raw_values) - min(raw_values)) for val in raw_values]

# Dead code path: never called
obsolete_fields = ['reliability', 'bandwidth', 'failover']
legacy_mapping = {field: 0.0 for field in obsolete_fields}

# Bit manipulation red herring
config_flag = 0b10101010
mask = 0b11110000
masked_config = config_flag & mask
shifted = masked_config >> 4

# String-based decoy processing
diagnostic_log = "METRIC_EVAL_OK|STATUS=GREEN|NODE=42"
log_parts = diagnostic_log.split('|')
node_id = int(log_parts[2].split('=')[1])

# Actual scoring logic buried among distractions
def calculate_weighted_sum(metrics, weights):
    total = 0.0
    for key in metrics:
        if key == 'latency_ms':
            # Invert latency: lower is better
            normalized_latency = 100 - (metrics[key] / 100 * 50)
            total += normalized_latency * abs(weights[key])
        else:
            total += metrics[key] * weights[key]
    return total

def adjust_for_consistency(score, consistency):
    multiplier = 1 + (consistency - 90) * 0.005  # bonus/penalty based on 90 threshold
    return score * multiplier

def evaluate_redundancy_factor(data_dict):
    # Unused complexity: counts keys above arbitrary threshold
    threshold_count = sum(1 for v in data_dict.values() if isinstance(v, (int, float)) and v > 85)
    if threshold_count >= 3:
        return 1.1
    return 1.0

def evaluate_performance(metrics, weights):
    base = calculate_weighted_sum(metrics, weights)
    adjusted = adjust_for_consistency(base, metrics['consistency'])
    
    # Check redundancy (this call has no effect on output - red herring)
    factor = evaluate_redundancy_factor(metrics)
    
    # Additional irrelevant check
    if metrics['accuracy'] > 85 and metrics['coverage'] < 80:
        pass  # dead branch: no action taken
    
    # Final adjustment: clamp to reasonable bounds
    final = max(50, min(adjusted, 100))
    
    # Critical assignment point
    final_score = round(final, 4)
    
    # More distractions below
    audit_trail = []
    audit_trail.append(f"Evaluated at {math.pi:.2f} seconds")
    metadata_tag = f"V2-{len(audit_trail)}-{int(math.floor(sum(metrics.values())))}"
    
    return final_score

# Key execution point
final_score = evaluate_performance(metric_data, user_weights)

# Print result as required
print(f"Result: {final_score}")