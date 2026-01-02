import math

# Simulated system telemetry data
telemetry_logs = [
    {'timestamp': 100, 'load': 45.2, 'errors': 3, 'response_time': 120},
    {'timestamp': 101, 'load': 62.8, 'errors': 1, 'response_time': 95},
    {'timestamp': 102, 'load': 78.1, 'errors': 5, 'response_time': 200},
    {'timestamp': 103, 'load': 88.9, 'errors': 8, 'response_time': 310},
    {'timestamp': 104, 'load': 56.4, 'errors': 2, 'response_time': 110}
]

# Irrelevant auxiliary data (distractor)
user_sessions = [{'id': i, 'active': True} for i in range(15)]
session_counter = len(user_sessions)  # Dead computation

# Preprocessing function with side distractions
def normalize_load(logs):
    max_load = max(entry['load'] for entry in logs)
    min_load = min(entry['load'] for entry in logs)
    range_load = max_load - min_load or 1
    
    # Extra unnecessary transformation
    squared_sum = sum((entry['load'] ** 2 for entry in logs))
    avg_sq = squared_sum / len(logs)
    
    return [(entry['load'] - min_load) / range_load for entry in logs], avg_sq

# Filtering logic using lambda (required feature)
threshold_func = lambda x: x['response_time'] > 100 and x['errors'] > 2

# Secondary distractor function (never called)
def calculate_uptime(records):
    total = sum(r['timestamp'] for r in records)
    penalty = 0
    for r in records:
        if r['errors'] > 4:
            penalty += 10
    return total - penalty  # Unused result

# Core processing with multiple concepts
baseline_reference = 0.75
efficiency_units = []
penalty_factor = 0

for log in telemetry_logs:
    # Compute normalized metrics
    raw_load = log['load']
    response_time = log['response_time']
    error_count = log['errors']
    
    # Intermediate irrelevant calculation (distractor)
    adjusted_time = response_time * (1 + error_count * 0.05)
    
    # Conditional logic with nesting (2-3 levels)
    if raw_load > 70:
        if error_count > 4:
            penalty_factor += 15
        else:
            penalty_factor += 5
    elif raw_load > 50:
        if response_time > 150:
            penalty_factor += 10
    
    # Compute efficiency unit (semi-relevant)
    base_efficiency = (raw_load / 100) * (100 - response_time * 0.5) / 100
    efficiency_units.append(max(base_efficiency, 0))

# Use of set for deduplication (concept inclusion) - minor role
unique_error_counts = set(log['errors'] for log in telemetry_logs)
error_boost = len(unique_error_counts) * 0.05 if len(unique_error_counts) > 3 else 0

# Main aggregation using lambda and list comprehension
aggregate_efficiency = sum(map(lambda x: round(x, 3), efficiency_units))

# Final processing step with key variable assignment
def process_metrics(data, filter_fn):
    filtered_count = len([d for d in data if filter_fn(d)])
    global penalty_factor
    
    # Complex conditional expression
    adjustment = 0.9 if filtered_count >= 3 else (0.95 if filtered_count == 2 else 1.0)
    
    # Final score computation
    raw_score = aggregate_efficiency + error_boost
    adjusted_score = raw_score * adjustment
    final_penalty = penalty_factor * 0.01
    
    # Key variable: efficiency_score
    efficiency_score = round(adjusted_score - final_penalty, 4)
    
    # Distractor variables
    diagnostic_flag = efficiency_score < 0.5
    audit_trail = [diagnostic_flag, filtered_count, adjustment]
    
    return {
        'score': efficiency_score,
        'audit': audit_trail
    }

# Execution point of interest
final_output = process_metrics(telemetry_logs, threshold_func)
efficiency_score = final_output['score']

# Output result as required
print(f"Result: {efficiency_score}")