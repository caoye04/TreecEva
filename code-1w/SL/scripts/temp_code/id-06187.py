from collections import defaultdict, Counter
import math

# Simulated dataset for multi-criteria evaluation
data_set = [
    {'performance': 85, 'reliability': 70, 'efficiency': 90, 'usability': 65},
    {'performance': 90, 'reliability': 80, 'efficiency': 88, 'usability': 75},
    {'performance': 78, 'reliability': 85, 'efficiency': 80, 'usability': 82},
    {'performance': 92, 'reliability': 60, 'efficiency': 94, 'usability': 60}
]

# Weight configuration for scoring (normalized later)
weights = {'performance': 0.4, 'reliability': 0.3, 'efficiency': 0.2, 'usability': 0.1}

# Irrelevant statistical counters (distractor)
stat_tracker = defaultdict(int)
dimension_counts = Counter()

for entry in data_set:
    for key in entry:
        dimension_counts[key] += 1
        stat_tracker['total_entries'] += 1
        stat_tracker['sum_' + key] += entry[key]

# Dead computation path: computes averages but not used in final logic
average_metrics = {}
for key in dimension_counts:
    average_metrics[key] = stat_tracker['sum_' + key] / dimension_counts[key]

# Misleading transformation: applies sigmoid-like scaling (unused)
scaled_data = []
for entry in data_set:
    scaled_entry = {}
    for k, v in entry.items():
        scaled_entry[k] = 100 * (1 / (1 + math.exp(-v / 100)))  # red herring
    scaled_data.append(scaled_entry)

# Auxiliary function that looks important but is only partially used
def compute_normalized_ranks(data_list, field):
    values = [item[field] for item in data_list]
    sorted_vals = sorted(values)
    ranks = {val: idx + 1 for idx, val in enumerate(sorted_vals)}
    return [ranks[v] for v in values]

# Another unused helper (decoy)
def analyze_variance(data_list, field):
    values = [item[field] for item in data_list]
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    return variance

# Core processing function with relevant logic buried among distractions
def calculate_final_score(dataset, weight_dict):
    raw_scores = []
    
    # Normalize weights to ensure they sum to 1.0 (actual use)
    total_weight = sum(weight_dict.values())
    normalized_weights = {k: v / total_weight for k, v in weight_dict.items()}
    
    # Compute weighted score for each entry
    for entry in dataset:
        weighted_sum = 0.0
        max_possible = 0.0
        
        for criterion, value in entry.items():
            if criterion in normalized_weights:
                weighted_sum += value * normalized_weights[criterion]
                max_possible += 100 * normalized_weights[criterion]  # theoretical max
        
        # Normalize score to percentage of maximum possible
        raw_scores.append(weighted_sum / max_possible * 100)
    
    # Apply non-linear adjustment based on reliability threshold (key logic)
    adjusted_scores = []
    for i, entry in enumerate(dataset):
        base = raw_scores[i]
        reliability_factor = entry['reliability'] / 100
        if reliability_factor < 0.7:
            adjustment = 0.9
        elif reliability_factor >= 0.8:
            adjustment = 1.05
        else:
            adjustment = 1.0
        adjusted_scores.append(base * adjustment)
    
    # Aggregate using trimmed mean (remove highest and lowest)
    sorted_adjusted = sorted(adjusted_scores)
    trimmed = sorted_adjusted[1:-1]  # remove outliers
    
    # Final aggregation
    final_aggregate = sum(trimmed) / len(trimmed)
    
    # Irrelevant set operation (distraction)
    unique_dimensions = set()
    for d in dataset:
        unique_dimensions.update(d.keys())
    expected_dims = {'performance', 'reliability', 'efficiency', 'usability'}
    missing = expected_dims - unique_dimensions
    
    return round(final_aggregate, 4)

# Execution point of interest
final_score = calculate_final_score(data_set, weights)

# Print result as required
print(f"Result: {final_score}")