def evaluate_performance(items_produced, defects):
    base_efficiency = items_produced / (defects + 1)
    penalty = 0
    if defects > 5:
        penalty += defects * 2
    elif defects == 0:
        penalty -= 10  # Bonus for zero defects

    # Distractor: Irrelevant tracking of idle time
    idle_periods = [5, 10, 15]
    total_idle = sum(idle_periods)
    adjusted_efficiency = base_efficiency - (penalty / 2)

    # More distraction: Simulating unrelated maintenance cycles
    maintenance_log = [m * 1.5 for m in range(3) if m % 2 == 0]
    maintenance_impact = len(maintenance_log) * 0.5

    return int(adjusted_efficiency - maintenance_impact)

# Main workflow
hours_worked = 8
productivity = 97
errors = 3

# Distractor: unused calculation of theoretical max
max_possible = hours_worked * 15
theoretical_limit = max_possible * 1.1

# Distractor: Redundant list slicing to simulate data filtering
raw_data = [1, 2, 3, 4, 5, 6, 7, 8]
filtered_data = raw_data[2:6]
processed_count = len(filtered_data)

# Key computation chain
interim_result = productivity - (errors * 3)
scaled_output = interim_result / hours_worked

# Conditional adjustment with no real effect (dead branch)
if scaled_output < 10:
    scaled_output += 2
else:
    dummy_var = scaled_output * 0.1  # Unused variable

# Final evaluation
final_score = evaluate_performance(productivity, errors)

# Output result
print(f"Result: {final_score}")