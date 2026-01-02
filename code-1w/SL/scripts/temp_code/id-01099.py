from collections import defaultdict, Counter
import math

# Simulated system metrics from distributed nodes
data = [
    {'node': 'A', 'load': 0.4, 'errors': 2, 'latency': 120, 'active': True},
    {'node': 'B', 'load': 0.8, 'errors': 5, 'latency': 190, 'active': True},
    {'node': 'C', 'load': 0.3, 'errors': 1, 'latency': 95, 'active': False},
    {'node': 'D', 'load': 0.9, 'errors': 8, 'latency': 210, 'active': True},
    {'node': 'E', 'load': 0.6, 'errors': 3, 'latency': 150, 'active': True}
]

# Irrelevant historical thresholds (distractor)
historical_thresholds = {
    'load_peak': 0.95,
    'max_errors': 10,
    'latency_spike': 250
}

# Configuration with mixed relevant and irrelevant fields
config = {
    'weight_load': 0.4,
    'weight_errors': 0.35,
    'weight_latency': 0.25,
    'activation_required': True,
    'debug_mode': False,
    'log_path': '/tmp/debug.log',
    'timeout': 30
}

# Decoy function that is never called
def analyze_trend(history):
    trend_score = 0
    for i in range(len(history) - 1):
        trend_score += (history[i+1] - history[i]) * 1.5
    return abs(trend_score) // 2

# Auxiliary transformation (partially used)
def normalize_value(val, min_val, max_val):
    if val < min_val: return 0
    if val > max_val: return 1
    return (val - min_val) / (max_val - min_val)

# Heavily distracted processing pipeline
def process_metrics(metrics, cfg):
    # Irrelevant counters (distractors)
    debug_counter = defaultdict(int)
    node_status_log = []

    # Relevant accumulators
    total_weighted_score = 0.0
    active_node_count = 0
    error_penalties = []

    # Misleading intermediate structure (only partially used)
    node_analysis = {}
    for entry in metrics:
        node_id = entry['node']
        load = entry['load']
        errors = entry['errors']
        latency = entry['latency']
        active = entry['active']

        # Irrelevant logging (dead path)
        debug_counter[node_id] += 1
        node_status_log.append(f"Node {node_id}: {'ON' if active else 'OFF'}")

        # Real logic begins: only process active nodes
        if not cfg.get('activation_required') or active:
            normalized_load = normalize_value(load, 0.0, 1.0)
            normalized_errors = normalize_value(errors, 0, 10)
            normalized_latency = normalize_value(latency, 50, 250)

            # Weighted health score (lower is better)
            health_score = (
                normalized_load * cfg['weight_load'] +
                normalized_errors * cfg['weight_errors'] +
                normalized_latency * cfg['weight_latency']
            )

            # Invert for 'score' (higher is better)
            node_score = (1 - health_score) * 100

            # Track penalties for debugging (not used in final score)
            if errors > 4:
                error_penalties.append((node_id, errors))

            # Store analysis (partial use)
            node_analysis[node_id] = {
                'raw': entry,
                'score': node_score,
                'penalized': errors > 4
            }

            total_weighted_score += node_score
            active_node_count += 1
        else:
            # Inactive node handling (no-op with side distraction)
            node_analysis[node_id] = {'status': 'excluded', 'reason': 'inactive'}

    # Compute average score of eligible nodes
    avg_score = total_weighted_score / active_node_count if active_node_count > 0 else 0

    # Apply arbitrary stability bonus (based on active node count)
    stability_bonus = 5 if active_node_count >= 3 else 2

    # Final manipulation: XOR-based obfuscation of bonus (bitwise distractor)
    bonus_int = int(stability_bonus)
    magic_shift = (bonus_int << 2) ^ 7  # Irrelevant transformation
    decoy_value = (magic_shift + len(error_penalties)) % 11  # Dead-end calc

    # Actual final score computation
    final_score = avg_score + stability_bonus

    # Red herring: adjust based on phantom condition
    if decoy_value > 8 and debug_counter['Z'] > 0:  # Never true
        final_score *= 0.9

    # Return final result
    return final_score

# Execution point of interest
final_score = process_metrics(data, config)
print(f"Result: {final_score}")