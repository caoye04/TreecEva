import math

# Simulated system health metrics (irrelevant to final result)
system_uptime = [99.1, 98.7, 99.5, 97.2, 100.0]
error_count = 12
decoy_weights = [0.1, 0.3, 0.2, 0.4]

# Core data for evaluation
benchmark_data = [
    {'name': 'latency', 'value': 42, 'active': True},
    {'name': 'throughput', 'value': 86, 'active': True},
    {'name': 'jitter', 'value': 14, 'active': False},
    {'name': 'bandwidth', 'value': 91, 'active': True}
]

# Secondary decoy dataset with misleading calculations
temp_analysis = {
    'fahrenheit': [32, 212, 98.6],
    'celsius': [],
    'converted': False
}

for f in temp_analysis['fahrenheit']:
    c = round((f - 32) * 5/9, 2)
    temp_analysis['celsius'].append(c)

temp_analysis['converted'] = True

# Unused recursive function - red herring
def calculate_entropy(data, base=2):
    if len(data) <= 1:
        return 0
    mid = len(data) // 2
    return 1 + max(
        calculate_entropy(data[:mid], base),
        calculate_entropy(data[mid:], base)
    )

# Irrelevant string processing with distraction
raw_logs = "ERROR|INFO|WARNING|INFO|DEBUG|INFO"
log_list = raw_logs.split('|')
log_counts = {}
for entry in log_list:
    log_counts[entry] = log_counts.get(entry, 0) + 1

summary_tag = ""
if log_counts.get('ERROR') > 0:
    summary_tag += "CRITICAL_"
if log_counts.get('WARNING') > 1:
    summary_tag += "STABILITY_ISSUE_"
summary_tag += "OK"
summary_tag = summary_tag.lower()

# Real metric weights (key part hidden among noise)
metric_importance = {
    'latency': 0.4,
    'throughput': 0.35,
    'bandwidth': 0.25
    # 'jitter' intentionally excluded due to inactive status
}

# Distractor: fake normalization using bitwise ops (not used)
fake_normalized = 0
for i in range(1, 6):
    fake_normalized |= (i << 2)

# Actual logic buried in distractions
def preprocess_value(val, name):
    if name == 'latency':
        return 100 - val  # invert since lower latency is better
    return val

def evaluate_performance(metrics, data):
    total_weighted = 0.0
    total_influence = 0.0
    
    # Process each metric with conditional activation
    for item in data:
        name = item['name']
        value = item['value']
        active = item['active']
        
        if not active or name not in metric_importance:
            continue
            
        weight = metric_importance[name]
        processed = preprocess_value(value, name)
        total_weighted += processed * weight
        total_influence += weight
    
    # Normalize by total influence (in case weights don't sum to 1.0 exactly)
    if total_influence == 0:
        return 0.0
        
    base_result = total_weighted / total_influence
    
    # Final adjustment using string-derived condition (subtle but valid)
    adjustment_factor = 1.0
    if 'ok' in summary_tag:
        adjustment_factor = 1.05
    
    adjusted = base_result * adjustment_factor
    
    # One more check: if any temp is near freezing, reduce score (decoy condition - never triggers)
    for c_val in temp_analysis['celsius']:
        if abs(c_val - 0.0) < 0.1:
            adjusted *= 0.9  # this block never executes
    
    return round(adjusted, 4)

# Misleading intermediate call (no side effects)
entropy_value = calculate_entropy(decoy_weights)

# Critical execution point
final_score = evaluate_performance(metric_importance, benchmark_data)

# Output the target result
print(f"Target result: {final_score}")