from collections import defaultdict
from itertools import combinations
import math

# Simulated system metrics from a distributed service
def get_raw_metrics():
    return {
        'latency_ms': 142.5,
        'req_per_sec': 893,
        'error_rate': 0.012,
        'memory_util': 0.67,
        'cpu_temp_c': 73.2
    }

# Irrelevant helper - looks important but unused in final logic
def calculate_health_index(data):
    score = 0
    for k, v in data.items():
        if 'util' in k:
            score += (1 - v) * 10
        elif 'rate' in k:
            score -= v * 5
        else:
            score += 1 / (1 + v)
    return round(score, 2)

# Decoy weight set - not used in final calculation
decoy_weights = defaultdict(lambda: 1.0)
decoy_weights.update({
    'latency_ms': -0.3,
    'req_per_sec': 0.4,
    'missing_metric': 0.5
})

# Core evaluation function with red herrings
def preprocess_metrics(raw):
    processed = {}
    # Real transformations
    processed['latency_norm'] = max(0, 200 - raw['latency_ms']) / 200
    processed['throughput_score'] = min(1, raw['req_per_sec'] / 1000)
    processed['reliability'] = 1 - raw['error_rate']
    
    # Distractor computations
    thermal_factor = math.log(raw['cpu_temp_c'] + 273.15)  # Kelvin conversion noise
    phantom_var = (raw['memory_util'] ** 2) * 100  # Unused derived metric
    
    # Fake aggregation that isn't used
    shadow_score = 0
    for val in [processed['latency_norm'], processed['throughput_score']]:
        shadow_score += val * 0.5
    processed['ghost_aggregate'] = shadow_score
    
    return processed

# Weight configuration - only this one matters
FINAL_WEIGHTS = {
    'latency_norm': 0.4,
    'throughput_score': 0.35,
    'reliability': 0.25
}

# Higher-order function returning scorer - distraction via abstraction
def create_scorer(base_weights):
    def scorer(features):
        return sum(features[key] * w for key, w in base_weights.items())
    return scorer

# Unused recursive path - dead code to mislead
def recursive_dampen(value, depth=3):
    if depth <= 0 or value < 0.1:
        return value
    return 0.9 * recursive_dampen(value, depth - 1)

# Main scoring logic buried among distractions
def evaluate_performance(metrics, weights):
    # Intermediate mapping
    temp_map = lambda d: {k: v for k, v in d.items() if v > 0.2}
    filtered = temp_map(metrics)
    
    # Real score computation
    raw_score = 0
    for key, weight in weights.items():
        if key in filtered:
            raw_score += filtered[key] * weight
    
    # Apply meaningless nonlinearity (but doesn't affect result because already normalized)
    saturated = math.tanh(raw_score) if raw_score > 0 else raw_score
    
    # Final scaling - deterministic and critical
    final_scaled = int(saturated * 1000)  # Convert to integer score
    
    # Dead branch - never executes due to logic
    if final_scaled < 0 or math.isnan(saturated):
        final_scaled = 500  # Recovery that never triggers
    
    return final_scaled

# Red herring data structure
candidate_configs = [
    {'strategy': 'aggressive', 'threshold': 0.8},
    {'strategy': 'conservative', 'threshold': 0.3}
]

# Generate irrelevant combinations
config_pairs = list(combinations(candidate_configs, 2))

# Primary execution flow
if __name__ == "__main__":
    raw_data = get_raw_metrics()
    
    # Unused health check
    health = calculate_health_index(raw_data)  # Computed but ignored
    
    # Transform to evaluation-ready features
    engineered_features = preprocess_metrics(raw_data)
    
    # Create scorer function (not used - direct eval instead)
    evaluator = create_scorer(FINAL_WEIGHTS)
    
    # Critical statement
    final_score = evaluate_performance(engineered_features, FINAL_WEIGHTS)
    
    # Print result as required
    print(f"Target result: {final_score}")