def main():
    # Simulate employee performance metrics
    base_productivity = 85
    overtime_hours = 12
    error_count = 3
    team_bonus = 5

    # Distractor: irrelevant health metrics
    heart_rate_avg = 72
    steps_taken = 8500
    sleep_quality = 0.78

    # Real computation begins
    adjusted_productivity = base_productivity + (overtime_hours * 2) - (error_count * 4)

    # Risk factor calculation using modular arithmetic and logical checks
    if error_count > 0:
        risk_category = 'moderate' if error_count < 5 else 'high'
    else:
        risk_category = 'low'

    risk_factor = 1.5 if risk_category == 'moderate' else (2.0 if risk_category == 'high' else 1.0)

    # Use of lambda for dynamic weighting
    weight_fn = lambda x: x * 0.9 if overtime_hours > 10 else x * 1.1
    productivity = weight_fn(adjusted_productivity)

    # Set operations to simulate task completion overlap
    core_tasks = {1, 2, 3, 4, 5}
    completed_tasks = {2, 4, 5, 6, 7}
    overlap = core_tasks & completed_tasks  # intersection
    coverage_ratio = len(overlap) / len(core_tasks)

    # More distractors: unused efficiency calculations
    cpu_efficiency = 0.94
    memory_utilization = 450
    temp_sensor_readings = [23.5, 24.1, 22.7]

    # Final evaluation function
    def evaluate_performance(prod, risk):
        base = prod * coverage_ratio
        penalty = base * (risk - 1.0)
        return int(base - penalty + team_bonus)

    final_score = evaluate_performance(productivity, risk_factor)

    # Print result as required
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()