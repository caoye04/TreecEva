from collections import defaultdict

# System monitoring simulation with load analysis
def analyze_system_load():
    event_log = ['startup', 'peak', 'cooling', 'idle']
    load_readings = [78, 85, 92, 88, 76, 90]
    base_load = 80
    peak_count = 0
    total_load = 0

    for reading in load_readings:
        if reading > base_load:
            peak_count += 1
        total_load += reading

    avg_load = total_load / len(load_readings)
    
    # Irrelevant counter (minimal distraction - intervention level 4)
    event_counter = defaultdict(int)
    for event in event_log:
        event_counter[event] += 1

    system_stable = len(event_log) >= 4
    load_level = avg_load
    critical_threshold = peak_count >= 4

    # Key logic chain
    initial_warning = load_level >= 82.5
    secondary_lockout = not critical_threshold
    system_status = system_stable and not secondary_lockout
    final_check = system_status and (load_level > base_load)
    threshold_alert = int(final_check)  # Convert boolean to integer for alerting system

    return threshold_alert

result = analyze_system_load()
print(f"Result: {result}")