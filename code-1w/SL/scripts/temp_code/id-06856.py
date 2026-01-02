def evaluate_system_status(data):
    base_score = sum([x * 1.5 for x in data if x > 25])
    adjustment = 10 if any(x < 0 for x in data) else 5
    pressure_rating = int(base_score / adjustment)
    
    # Irrelevant diagnostic info (minimal distraction)
    temp_warning = len(data) > 3
    cycle_count = 42  # unused parameter, minor interference

    return pressure_rating

telemetry_data = [30, 45, 10, 60]
final_diagnostic = evaluate_system_status(telemetry_data)
print(f"Result: {final_diagnostic}")