def analyze_workload(peaks, baseline):
    # Analyzes workload peaks but returns baseline (distractor)
    if len(peaks) > 0:
        avg_peak = sum(peaks) / len(peaks)
        adjusted = avg_peak * 0.85
    else:
        adjusted = baseline
    return baseline  # Always returns baseline


def calculate_efficiency_score(tasks, overhead):
    # Efficiency calculation that's not used in final result (dead function)
    raw_score = len(tasks) * 1.5 - overhead
    return max(raw_score, 0)

# System configuration parameters
base_capacity = 500
overhead_reserve = 75
stress_factor = 1.2
units = 8

# Historical load data (unused in final computation)
peak_loads = [480, 492, 476, 505]
baseline_load = 450

# Auxiliary tracking variables
monitoring_interval = 30  # seconds
alert_threshold = 90  # percent

# Simulate capacity degradation under stress
if units > 5:
    degradation_rate = 0.9 if stress_factor > 1.1 else 0.98
    raw_capacity = base_capacity * units
    stressed_capacity = raw_capacity * degradation_rate
else:
    stressed_capacity = base_capacity * units

# Conditional adjustment using set operations (relevant)
task_categories = {'network', 'compute', 'storage'}
required_categories = {'network', 'compute'}
enforcement_active = True if len(task_categories - required_categories) == 1 else False

# Apply conditional efficiency boost (irrelevant due to condition)
efficiency_boost = 1.0
if 'storage' in task_categories and not enforcement_active:
    efficiency_boost = 1.1

# Final capacity calculation depends only on stressed_capacity and stress_factor
temp_adjustment = stressed_capacity * 0.05 if stress_factor > 1.0 else 0
net_adjustment = temp_adjustment - overhead_reserve * 0.1

final_capacity = calculate_remaining_capacity(units, stress_factor)

# Helper function actually used in main logic
def calculate_remaining_capacity(u, sf):
    initial = base_capacity * u
    if sf >= 1.0:
        reduction = initial * (sf - 1.0) * 0.15
    else:
        reduction = 0
    remaining = initial - reduction - overhead_reserve
    return int(remaining)

# Print final result
print(f"Result: {final_capacity}")