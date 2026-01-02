from itertools import compress, count

# Simulate employee performance metrics across departments
def analyze_department_efficiency(base_metrics, adjustment_factor):
    adjusted = [x * adjustment_factor for x in base_metrics]
    outliers = list(filter(lambda x: x > 85, adjusted))
    return sum(outliers) / len(outliers) if outliers else 0

# Auxiliary function to compute risk based on workload distribution
def calculate_workload_risk(metrics):
    sorted_vals = sorted(metrics)
    median = sorted_vals[len(sorted_vals) // 2]
    variance_proxy = sum((x - median) ** 2 for x in sorted_vals) / len(sorted_vals)
    risk_factor = 1 + (variance_proxy / 100)
    return risk_factor, median

# Core evaluation logic
def evaluate_performance(productivity, risk_factor):
    # Apply diminishing returns using lambda transformation
    diminishing_fn = lambda x: x / (1 + 0.1 * x)
    adjusted_productivity = sum(map(diminishing_fn, productivity))

    # Normalize by risk factor
    score = adjusted_productivity / risk_factor

    # Irrelevant intermediate computation (distractor)
    temp_analysis = [x for x in productivity if x > 70]
    avg_high_performer = sum(temp_analysis) / len(temp_analysis) if temp_analysis else 0
    normalized_avg = avg_high_performer / (max(productivity) or 1)

    # Final scoring with offset
    final_score = int(score + 10)  # Offset added for calibration

    # Dead code path (never executed but looks relevant)
    if False:
        fallback = analyze_department_efficiency(productivity, 1.1)
        final_score = max(final_score, fallback)

    return final_score

# Main simulation setup
total_employees = 12
department_id = "DEV-7"
productivity = [78, 85, 90, 67, 88, 92, 75, 84, 79, 81, 87, 83]
risk_factor, median_load = calculate_workload_risk(productivity)

# Tracking auxiliary stats (unused in final result)
employee_ids = [f"EMP-{str(i).zfill(3)}" for i in range(total_employees)]
names_stream = count(1000)
assigned_codes = list(zip(employee_ids, names_stream))

# Key execution point
debug_mode = False
if debug_mode:
    print(f"Processing department: {department_id}")

final_score = evaluate_performance(productivity, risk_factor)
print(f"Result: {final_score}")