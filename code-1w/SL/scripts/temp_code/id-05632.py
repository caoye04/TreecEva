from collections import defaultdict, Counter
import math

# Simulated system metrics for a distributed task scheduler
task_loads = [12, 15, 8, 20, 14, 17, 9, 11]
response_times = [0.23, 0.31, 0.18, 0.41, 0.29, 0.34, 0.20, 0.25]
error_rates = [0.02, 0.05, 0.01, 0.08, 0.03, 0.07, 0.01, 0.04]
uptime_hours = [99.1, 98.7, 99.5, 97.2, 98.9, 97.8, 99.4, 98.5]

# Irrelevant auxiliary data (distractor)
city_temperatures = {'New York': 23, 'Tokyo': 27, 'Paris': 20, 'Sydney': 19}
user_preferences = defaultdict(lambda: 'unknown')
user_preferences.update({'theme': 'dark', 'notifications': 'enabled'})

# Decoy function that looks relevant but isn't used in final calculation
def analyze_city_data(temp_data):
    avg = sum(temp_data.values()) / len(temp_data)
    return {city: temp - avg for city, temp in temp_data.items()}

# Unused transformation (dead code path)
normalized_loads = [load / max(task_loads) for load in task_loads]
filtered_tasks = [load for load in task_loads if load > 10]

# Core metric preprocessing
normalized_response = [1 - (rt / 0.5) for rt in response_times]  # Normalize to 0-1 scale
stability_scores = [1 - err for err in error_rates]
efficiency_metrics = [load * norm_resp for load, norm_resp in zip(task_loads, normalized_response)]

# Weight assignment (some weights are red herrings)
weights = {
    'efficiency': 0.4,
    'stability': 0.3,
    'reliability': 0.2,  # not used
    'availability': 0.1   # not used
}

# Historical benchmark (irrelevant comparison)
historical_avg_efficiency = 11.2
recent_trend = [10.8, 11.1, 11.3, 11.0, 11.4]

# Aggregation using list comprehension and Counter (real usage)
metric_aggregates = [
    sum(efficiency_metrics) / len(efficiency_metrics),
    sum(stability_scores) / len(stability_scores)
]

# Simulated redundancy check (misleading intermediate result)
duplicate_checker = Counter(efficiency_metrics)
duplicates_found = sum(1 for count in duplicate_checker.values() if count > 1)

# Conditional adjustment based on threshold (actually affects result)
base_efficiency = metric_aggregates[0]
if base_efficiency > 12.0:
    adjusted_efficiency = base_efficiency * 0.95
else:
    adjusted_efficiency = base_efficiency * 1.02  # This branch is taken

# Final performance evaluation
def evaluate_performance(metrics, weight_map):
    efficiency_part = adjusted_efficiency * weight_map['efficiency']
    stability_part = metric_aggregates[1] * weight_map['stability']
    
    # Deliberately unused components (distraction)
    hypothetical_reliability = 95.7 * weight_map['reliability']
    dummy_availability = sum(uptime_hours) / len(uptime_hours) * weight_map['availability']
    
    total = efficiency_part + stability_part  # Only two components actually contribute
    
    # Final nonlinear adjustment (critical step)
    final_value = math.log(total * 10 + 1)
    return final_value

# Execution point of interest
final_score = evaluate_performance(metric_aggregates, weights)

# Output result as required
print(f"Result: {final_score}")