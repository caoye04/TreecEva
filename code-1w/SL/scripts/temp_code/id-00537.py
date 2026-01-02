from itertools import compress

def evaluate_performance(hours_worked, error_rate):
    base_efficiency = sum(hours_worked) / len(hours_worked)
    penalty = 0
    if any(e > 0.1 for e in error_rate):
        penalty = sum(1 for e in error_rate if e > 0.1) * 0.05
    adjusted_efficiency = max(base_efficiency - penalty, 0)
    return int(adjusted_efficiency * 100)

# Simulate daily productivity and quality metrics over a workweek
daily_hours = [7.5, 8.0, 6.5, 9.0, 8.5]
daily_errors = [0.03, 0.01, 0.12, 0.08, 0.15]  # Error rates per day

# Filter high-error days using itertools
high_error_days = list(compress(daily_hours, (e > 0.1 for e in daily_errors)))
total_high_error_hours = sum(high_error_days)

# Compute average without high-error days for diagnostic purposes
filtered_hours = [h for h, e in zip(daily_hours, daily_errors) if e <= 0.1]
avg_clean_hours = sum(filtered_hours) / len(filtered_hours) if filtered_hours else 0

# Core evaluation parameters
productivity = daily_hours
risk_factor = daily_errors
final_score = evaluate_performance(productivity, risk_factor)

print(f"Result: {final_score}")