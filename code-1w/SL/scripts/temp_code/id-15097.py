def apply_calibration(data):
    baseline = sum(data) / len(data)
    adjusted = [x * 0.9 + baseline * 0.1 for x in data]
    
    # Compute aggregated health metric using lambda and conditional logic
    health_evaluator = lambda x: 1 if x > baseline else 0
    active_count = sum(map(health_evaluator, adjusted))

    # Determine system state with conditional expression
    system_state = 'active' if active_count >= len(data) // 2 else 'standby'

    # Critical computation point
    threshold_score = len(data) * 0.75 if system_state == 'active' else len(data) * 0.25

    return threshold_score

# Input data
measurements = [12, 15, 10, 8, 20, 14]

# Execution
final_diagnostic = apply_calibration(measurements)

# Output result
print(f"Result: {final_diagnostic}")