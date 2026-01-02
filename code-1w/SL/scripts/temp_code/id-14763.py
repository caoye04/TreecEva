from collections import defaultdict, Counter
import math

# Simulated system metrics from a distributed task scheduler
task_durations = [23, 45, 12, 67, 34, 22, 55, 31, 44, 39]
resource_usage = [0.67, 0.89, 0.45, 0.92, 0.54, 0.76, 0.81, 0.63, 0.77, 0.71]
failure_counts = [1, 0, 2, 1, 0, 1, 0, 3, 1, 0]

def analyze_trends(data):
    # Irrelevant trend analysis (distractor)
    diffs = [data[i+1] - data[i] for i in range(len(data)-1)]
    avg_change = sum(diffs) / len(diffs)
    volatility = sum((x - avg_change)**2 for x in diffs) / len(diffs)
    return volatility

def compute_entropy(values):
    # Unused entropy function (dead code path)
    counts = Counter(values)
    total = len(values)
    probs = [count/total for count in counts.values()]
    return -sum(p * math.log2(p) for p in probs if p > 0)

def filter_outliers(data, threshold=1.5):
    # Outlier filtering not actually used in main logic
    q1 = sorted(data)[len(data)//4]
    q3 = sorted(data)[3*len(data)//4]
    iqr = q3 - q1
    lower, upper = q1 - threshold * iqr, q3 + threshold * iqr
    return [x for x in data if lower <= x <= upper]

# Misleading intermediate computations
trend_volatility = analyze_trends(task_durations)
raw_entropy = compute_entropy([x//10 for x in task_durations])
cleaned_resources = filter_outliers(resource_usage, 2.0)

# Weight initialization with decoy assignments
weights = defaultdict(float)
weights['duration'] = 0.4
weights['usage'] = 0.35
weights['failures'] = 0.25
weights['reliability_bonus'] = 0.1  # Not actually used

# Auxiliary transformation functions
def normalize(data):
    min_val, max_val = min(data), max(data)
    if max_val == min_val:
        return [0.5 for _ in data]
    return [(x - min_val) / (max_val - min_val) for x in data]

def weighted_sum(values, weights):
    return sum(v * weights[i] for i, v in enumerate(values))

def calculate_efficiency(tasks, usage, failures):
    # Complex but partially irrelevant efficiency calculation
    norm_tasks = normalize(tasks)
    norm_usage = normalize(usage)
    
    base_scores = []
    for i in range(len(tasks)):
        raw_score = (0.6 * (1 - norm_tasks[i]) + 
                    0.3 * (1 - norm_usage[i]) + 
                    0.1 * (1 - failures[i]/3))
        if tasks[i] < 50:
            raw_score *= 1.1  # Performance bonus
        base_scores.append(max(raw_score, 0))
    
    # Additional distraction: clustering attempt
    cluster_bias = [1.05 if norm_usage[i] < 0.7 else 0.95 for i in range(len(norm_usage))]
    adjusted = [base_scores[i] * cluster_bias[i] for i in range(len(base_scores))]
    
    return sum(adjusted) / len(adjusted)

# Primary evaluation function
def evaluate_performance(metrics, weight_map):
    durations, usage, faults = metrics
    
    # Normalize relevant metrics
    norm_durations = normalize(durations)
    norm_usage = normalize(usage)
    
    # Compute failure penalty score (0 to 1 scale)
    total_failures = sum(faults)
    max_possible_failures = len(faults) * 3
    failure_rate = total_failures / max_possible_failures
    failure_penalty = 1 - failure_rate
    
    # Compute composite score using only duration, usage, and failures
    duration_component = sum(1 - d for d in norm_durations) / len(norm_durations)
    usage_component = sum(1 - u for u in norm_usage) / len(norm_usage)
    
    # Final weighted combination
    performance_score = (
        duration_component * weight_map['duration'] +
        usage_component * weight_map['usage'] +
        failure_penalty * weight_map['failures']
    )
    
    # Apply non-linear boost (sigmoid-like)
    boosted_score = 100 * (1 / (1 + math.exp(-10 * (performance_score - 0.5))))
    
    # Dead code branch - never executed due to logic
    if False and weight_map['reliability_bonus'] > 0.05:
        boosted_score += 10 * weight_map['reliability_bonus']
    
    return boosted_score

# Unused alternative scoring method (red herring)
def legacy_scorer(logs):
    score = 0
    for entry in logs:
        score += entry[0] * 0.1
        if entry[1] > 0.8:
            score -= 5
    return max(score, 0)

# Data aggregation (mostly relevant)
metrics = (task_durations, resource_usage, failure_counts)

# Secondary analysis creating misleading variables
avg_duration = sum(task_durations) / len(task_durations)
peak_usage = max(resource_usage)
zero_failure_tasks = len([f for f in failure_counts if f == 0])

# Actual efficiency score (not used in final calculation)
irrelevant_efficiency = calculate_efficiency(task_durations, resource_usage, failure_counts)

# Critical execution point
final_score = evaluate_performance(metrics, weights)

# Print result as required
print(f"Result: {final_score}")