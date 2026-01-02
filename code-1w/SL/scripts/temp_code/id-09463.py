def analyze_workload(efficiency, overhead):
    if efficiency > 0.8:
        return efficiency * (1 - overhead)
    else:
        return efficiency * 0.75

base_load = 480
temp_ratio = 0.67
surge_factor = 1.35
idle_cores = 12
utilization_history = [0.78, 0.82, 0.75, 0.88, 0.91]

# Simulate dynamic adjustment logic with red herrings
adjusted_utilization = [u for u in utilization_history if u > 0.8]
efficiency_score = len(adjusted_utilization) / 5.0

# Distractor: irrelevant string processing
log_entry = "System overload detected at t=124"
detected_issues = len([c for c in log_entry if c.isdigit()])
ignored_warning = log_entry.upper().replace("OVERLOAD", "WARNING")

# Simulated overhead calculation (some steps are misleading)
raw_overhead = sum([int(x) for x in str(idle_cores)]) * 0.01
normalized_overhead = raw_overhead if raw_overhead < 0.1 else 0.09

# Core analysis with conditional expression
processed_efficiency = analyze_workload(efficiency_score, normalized_overhead)
scaled_demand = base_load * processed_efficiency if processed_efficiency > 0.5 else base_load * 0.5

# Surge adjustment with distractor variables
peak_buffer = idle_cores * 8  # unused but plausible
fallback_mode = False
override_threshold = temp_ratio > 0.6 and surge_factor > 1.2

if override_threshold:
    adjusted_demand = scaled_demand * surge_factor
else:
    adjusted_demand = scaled_demand * 1.1

# Final capacity adjustment function
def adjust_capacity(load, factor):
    intermediate = load * factor
    if intermediate > 500:
        return int(intermediate * 0.95)
    else:
        return int(intermediate)

final_capacity = adjust_capacity(base_load, surge_factor)
print(f"Result: {final_capacity}")