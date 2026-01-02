def analyze_system_integrity():
    sensor_ids = {101, 203, 305, 407, 509, 611}
    fault_codes = {203, 407, 812, 915}
    critical_elements = {x for x in sensor_ids if x > 200}
    high_priority = fault_codes | {101, 305}
    baseline_eval = lambda x: (x ** 2) // 4

    # Key computation point
    filtration_score = len(critical_elements & high_priority) + baseline_eval(5)
    
    # Irrelevant tracking variables (minimal interference)
    log_timestamp = "2023-09-15T10:30:00Z"
    system_uptime = 127.4
    
    return filtration_score

result = analyze_system_integrity()
print(f"Result: {result}")