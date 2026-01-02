import math

# Simulated system metrics from a distributed computing environment
task_completion_times = [12.5, 8.3, 15.7, 6.2, 9.8, 14.1, 5.5, 11.9]
resource_utilization = {'cpu': 0.78, 'memory': 0.85, 'disk_io': 0.45, 'network': 0.62}
node_health_status = [True, True, False, True, True, False, True, True]

def calculate_efficiency_index(times):
    avg_time = sum(times) / len(times)
    variance = sum((t - avg_time) ** 2 for t in times) / len(times)
    return 100 * (1 - (variance / (avg_time ** 2 + 1)))

def assess_reliability(status_list):
    operational_nodes = sum(1 for s in status_list if s)
    total_nodes = len(status_list)
    return operational_nodes / total_nodes

def compute_load_balance_score(util_dict):
    # Irrelevant transformation
    normalized = {k: v**2 for k, v in util_dict.items()}
    balanced_score = 1 - abs(util_dict['cpu'] - util_dict['memory'])
    return balanced_score * 100

def analyze_response_distribution(times):
    sorted_times = sorted(times)
    q1 = sorted_times[len(sorted_times)//4]
    q3 = sorted_times[3*len(sorted_times)//4]
    iqr = q3 - q1
    lower_fence = q1 - 1.5 * iqr
    upper_fence = q3 + 1.5 * iqr
    outliers = [t for t in times if t < lower_fence or t > upper_fence]
    outlier_ratio = len(outliers) / len(times)
    penalty = 10 * outlier_ratio
    return 90 - penalty  # Base score reduced by outlier presence

def generate_diagnostic_report(data):
    # Dead function - never used but looks important
    report = {
        'timestamp': '2023-11-05',
        'anomalies_detected': 0,
        'recommended_actions': []
    }
    for val in data:
        if val > 14.0:
            report['anomalies_detected'] += 1
    return report

def normalize_metrics(raw_times):
    min_t, max_t = min(raw_times), max(raw_times)
    return [(t - min_t) / (max_t - min_t) for t in raw_times]

def evaluate_stability_index(norm_times, health_list):
    weighted_sum = 0.0
    for i, t in enumerate(norm_times):
        if i < len(health_list) and health_list[i]:
            weighted_sum += t * 1.1  # Slight boost for healthy nodes
        else:
            weighted_sum += t * 1.5  # Higher weight if node failed (distraction)
    return 100 - (weighted_sum * 10)

# Decoy variables and irrelevant preprocessing
decoy_matrix = [[i*j for j in range(5)] for i in range(5)]
accumulated_bias = 0
for row in decoy_matrix:
    for elem in row:
        accumulated_bias += math.sin(elem) % 0.3

# Intermediate metric calculations (some used, some not)
efficiency = calculate_efficiency_index(task_completion_times)
reliability = assess_reliability(node_health_status)
load_balance = compute_load_balance_score(resource_utilization)
response_quality = analyze_response_distribution(task_completion_times)
normalized_times = normalize_metrics(task_completion_times)
stability = evaluate_stability_index(normalized_times, node_health_status)

# Unused but plausible intermediate result
theoretical_capacity = efficiency * reliability * 1.25

# Key dictionary combining relevant metrics
metrics_dict = {
    'efficiency': efficiency,
    'reliability': reliability,
    'response_quality': response_quality,
    'stability': stability,
    'load_balance': load_balance  # Included but not used in final formula
}

baseline = {
    'target_efficiency': 75.0,
    'min_reliability': 0.8,
    'expected_stability': 60.0
}

# Core evaluation logic with conditional expression and dictionary operations
def evaluate_performance(metrics, base):
    score = 0.0
    
    # Weighted contribution based on deviation from baseline
    if metrics['efficiency'] >= base['target_efficiency']:
        score += 40  # Max efficiency points
    else:
        score += 20 + (metrics['efficiency'] - 60)  # Assume minimum expected is ~60
    
    if metrics['reliability'] >= base['min_reliability']:
        score += 30
    else:
        score += 15
    
    # Stability contributes conditionally
    stability_bonus = 10 if metrics['stability'] > base['expected_stability'] else 5
    score += stability_bonus
    
    # Response quality: top up to 15 points
    score += min(15, metrics['response_quality'] * 0.15)
    
    # Red herring: XOR-based adjustment (never actually affects result)
    temp_debug = int(score) ^ int(metrics['efficiency'])
    debug_flag = temp_debug & 1
    
    # Final nonlinear transformation (distractor-looking but score remains linear)
    final_adjustment = 0.98 if debug_flag else 1.02
    score *= final_adjustment  # This line seems complex but has minimal real impact
    
    # ACTUAL key operation: modular correction based on tuple unpacking
    multiplier_tuple = (1.05, 1.0, 0.95)  # performance tiers
    tier_index = 0
    if metrics['reliability'] >= 0.9:
        tier_index = 0
    elif metrics['reliability'] >= 0.7:
        tier_index = 1
    else:
        tier_index = 2
    
    selected_multiplier = multiplier_tuple[tier_index]
    score *= selected_multiplier
    
    # Final cap and round to nearest integer
    score = min(100, score)
    return round(score)

# Execute key statement
target_result = evaluate_performance(metrics_dict, baseline)
final_score = target_result

# Print result as required
print(f"Result: {final_score}")