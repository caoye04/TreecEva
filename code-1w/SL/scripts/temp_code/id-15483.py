from collections import defaultdict, Counter
import math

# Simulated system metrics from a distributed task scheduler
task_durations = [120, 150, 130, 90, 200, 180, 160, 140, 110, 170]
node_loads = [0.45, 0.67, 0.33, 0.89, 0.56, 0.78, 0.21, 0.91, 0.49, 0.63]
packet_loss_rates = [0.001, 0.003, 0.002, 0.01, 0.005, 0.007, 0.0008, 0.012, 0.004, 0.009]

def calculate_efficiency(durations):
    avg = sum(durations) / len(durations)
    variance = sum((x - avg) ** 2 for x in durations) / len(durations)
    return 100 * math.exp(-variance / 1000)

def normalize(data):
    min_val, max_val = min(data), max(data)
    if max_val == min_val:
        return [0.5 for _ in data]
    return [(x - min_val) / (max_val - min_val) for x in data]

def analyze_outliers(data):
    # Irrelevant analysis: counts outliers but not used later
    threshold = 2 * sum(data) / len(data)
    count = 0
    for x in data:
        if x > threshold:
            count += 1
    return count  # Dead-end return

def compute_stability(load_history):
    changes = [abs(a - b) for a, b in zip(load_history, load_history[1:])]
    stability_score = 100 - (sum(changes) / len(changes)) * 50
    return max(stability_score, 0)

def assess_reliability(loss_rates):
    total_impact = sum(-math.log(1 - rate) for rate in loss_rates if rate < 1)
    return 100 / (1 + total_impact)

def filter_anomalies(data, threshold=0.95):
    # Unused function - red herring
    upper = threshold * max(data)
    return [x for x in data if x <= upper]

def legacy_weight_adjustment(w):
    # Obsolete logic, never called
    return [x * 0.9 for x in w]

def aggregate_metrics(durations, loads, losses):
    efficiency = calculate_efficiency(durations)
    normalized_loads = normalize(loads)
    avg_normalized_load = sum(normalized_loads) / len(normalized_loads)
    load_penalty = 10 * (avg_normalized_load ** 2)  # Heuristic penalty
    
    # Distraction: complex outlier count with no impact
    outlier_count_durations = analyze_outliers(durations)
    outlier_count_loads = analyze_outliers(loads)
    dummy_counter = Counter([outlier_count_durations, outlier_count_loads])
    
    stability = compute_stability(loads)
    reliability = assess_reliability(losses)
    
    # Real metric computation
    base_score = efficiency + stability + reliability
    adjustment_factor = 1.0
    
    # Simulate conditional weighting (only one branch matters)
    if len(durations) > 5:
        adjustment_factor *= 1.05
    if max(losses) > 0.01:
        adjustment_factor *= 0.95
    else:
        adjustment_factor *= 1.02  # This branch triggers
    
    adjusted_score = base_score * adjustment_factor
    
    # Store intermediate results in dictionary — some keys unused later
    metrics = {
        'efficiency': efficiency,
        'stability': stability,
        'reliability': reliability,
        'load_balance': 1 - avg_normalized_load,
        'raw_duration_avg': sum(durations)/len(durations),
        'phantom_metric': float(dummy_counter[0]),  # Distractor
        'adjusted_score': adjusted_score
    }
    
    return metrics

def evaluate_performance(metrics, weights):
    weighted_sum = 0.0
    weight_total = 0.0
    
    # Use only specific metrics; others are distractions
    relevant_keys = ['efficiency', 'stability', 'reliability', 'adjusted_score']
    
    for key, weight in weights.items():
        if key in metrics and key in relevant_keys:
            weighted_sum += metrics[key] * weight
            weight_total += weight
    
    # Dead code: unreachable due to logic above
    if 'phantom_metric' in metrics and metrics['phantom_metric'] > 100:
        weighted_sum -= 50
    
    if weight_total == 0:
        return 0.0
    
    final_normalized = weighted_sum / weight_total
    
    # Final adjustment based on arbitrary heuristic
    duration_proxy = metrics.get('raw_duration_avg', 0)
    if duration_proxy < 150:
        final_normalized += 3.5  # Small bonus
    
    return final_normalized

def debug_print_state(data_dict):
    # Debug function never called — decoy
    for k, v in data_dict.items():
        print(f'[DEBUG] {k}: {v}')

# Main execution path
if __name__ == '__main__':
    # Irrelevant preprocessing block
    processed_durations = [d for d in task_durations if d >= 90]
    filtered_losses = [x for x in packet_loss_rates if x <= 0.01]
    
    # Create auxiliary tracking structure (not fully used)
    node_stats = defaultdict(dict)
    for i, (load, loss) in enumerate(zip(node_loads, packet_loss_rates)):
        node_stats[i]['load'] = load
        node_stats[i]['loss'] = loss
        node_stats[i]['risk_flag'] = load > 0.8 or loss > 0.01
    
    # Compute core metrics
    metrics = aggregate_metrics(task_durations, node_loads, packet_loss_rates)
    
    # Define weighting scheme
    weights = {
        'efficiency': 0.3,
        'stability': 0.25,
        'reliability': 0.35,
        'load_balance': 0.1,      # Weighted key NOT in relevant_keys → ignored
        'phantom_metric': 0.05,   # Another ignored weight
        'adjusted_score': 0.4
    }
    
    # Critical statement
    final_score = evaluate_performance(metrics, weights)
    
    # Print result as required
    print(f"Target result: {final_score}")