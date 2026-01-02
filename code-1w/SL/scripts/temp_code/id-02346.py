from collections import defaultdict
import math

def analyze_event_frequency(log_entries):
    # Counts frequency of event types (distractor: not directly used in final score)
    freq_counter = defaultdict(int)
    for entry in log_entries:
        freq_counter[entry['event']] += 1
    return freq_counter

def validate_thresholds(thresh_dict):
    # Validates and normalizes thresholds (some relevant, some misleading)
    normalized = {}
    total_weight = 0
    for k, v in thresh_dict.items():
        if v < 0:
            v = 0.1  # correction
        normalized[k] = round(v, 2)
        total_weight += v
    avg_weight = total_weight / len(normalized) if normalized else 1.0
    
    # Dead computation: average not used later
    adjusted_avg = avg_weight * 1.05 if avg_weight > 0.5 else avg_weight * 0.95
    
    return normalized

def calculate_stability_metric(log):
    # Computes time variance between entries (semi-relevant)
    if len(log) < 2:
        return 0.0
    time_diffs = []
    for i in range(1, len(log)):
        diff = log[i]['timestamp'] - log[i-1]['timestamp']
        time_diffs.append(diff)
    mean_diff = sum(time_diffs) / len(time_diffs)
    variance = sum((x - mean_diff) ** 2 for x in time_diffs) / len(time_diffs)
    return round(math.sqrt(variance), 4)

def calculate_final_score(log_entries, thresholds):
    # Core logic begins
    category_sum = defaultdict(float)
    event_count = 0
    
    for entry in log_entries:
        cat = entry['category']
        value = entry['value']
        category_sum[cat] += value
        event_count += 1
    
    # Intermediate distractor variables
    avg_per_event = category_sum['primary'] / event_count if event_count else 0
    peak_value = max(entry['value'] for entry in log_entries)
    
    # Key calculation: weighted sum based on thresholds
    raw_score = 0
    for cat, total in category_sum.items():
        if cat in thresholds:
            raw_score += total * thresholds[cat]
    
    # Apply penalty if instability detected
    stability = calculate_stability_metric(log_entries)
    penalty_factor = 0.8 if stability > 100 else 1.0
    
    # Distractor: unused risk assessment
    risk_flag = 'high' if stability > 200 and peak_value > 500 else 'low'
    
    final_score = int(raw_score * penalty_factor)
    
    # One more red herring: secondary adjustment not applied
    if avg_per_event > 100:
        projected = raw_score * 1.2
    else:
        projected = raw_score * 0.9
    
    return final_score

# Simulated input data
thresholds = {
    'primary': 1.2,
    'secondary': 0.8,
    'auxiliary': 0.3
}

data_log = [
    {'event': 'init', 'category': 'primary', 'value': 150, 'timestamp': 1000},
    {'event': 'step', 'category': 'secondary', 'value': 90, 'timestamp': 1150},
    {'event': 'step', 'category': 'primary', 'value': 200, 'timestamp': 1300},
    {'event': 'update', 'category': 'auxiliary', 'value': 60, 'timestamp': 1600},
    {'event': 'final', 'category': 'primary', 'value': 300, 'timestamp': 1900}
]

# Analyze frequency (irrelevant to final score)
freq_analysis = analyze_event_frequency(data_log)

# Validate thresholds (partially relevant, but only the dict matters)
normalized_thresholds = validate_thresholds(thresholds)

# Calculate final score
final_score = calculate_final_score(data_log, normalized_thresholds)
print(f"Result: {final_score}")