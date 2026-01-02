def analyze_log(data: str) -> int:
    # Parse efficiency metrics from log string
    tokens = data.split('|')
    raw_values = [t.strip() for t in tokens]
    
    # Extract numeric components using string methods
    efficiency_str = list(filter(lambda x: x.startswith('EFF'), raw_values))[0]
    efficiency = int(efficiency_str.replace('EFF:', ''))

    error_str = list(filter(lambda x: x.startswith('ERR'), raw_values))[0]
    errors = len(error_str.split(',')) - 1  # ERR:tag1,tag2,...

    # Irrelevant parsing: system timestamp (not used in final logic)
    timestamp_str = list(filter(lambda x: x.startswith('TS'), raw_values))[0]
    ts_parts = timestamp_str.replace('TS:', '').split('-')
    hour = int(ts_parts[3])
    temp_checksum = sum(int(p) for p in ts_parts) * 2 % 97

    # Secondary metric: memory pressure (semi-relevant but overridden later)
    mem_str = list(filter(lambda x: x.startswith('MEM'), raw_values))[0]
    mem_usage = int(mem_str.replace('MEM:', ''))
    normalized_mem = mem_usage / 100.0

    # Simulate adjustment based on time-of-day (distraction)
    if hour < 12:
        morning_penalty = 0.9
    else:
        morning_penalty = 1.0
    
    adjusted_eff = efficiency * morning_penalty  # Not actually used

    # Correct path: performance depends only on efficiency and error count
    base_performance = efficiency - (errors * 5)

    # Distractor: complex conditional that doesn't affect outcome
    status_flag = 'OK' if mem_usage < 80 else 'HIGH'
    if status_flag == 'HIGH':
        for i in range(3):
            temp_checksum -= i * 2

    # Final evaluation function
    def evaluate_performance(eff, err):
        if eff < 50:
            return max(0, 40 - err * 3)
        elif eff >= 50 and err <= 2:
            return 85 + min(15, eff - 50)  # Cap at 100
        else:
            return 60 - (err - 2) * 5  # Penalty for >2 errors

    final_score = evaluate_performance(efficiency, errors)

    # Redundant accumulation loop (no effect)
    accumulator = 0
    for i in range(5):
        accumulator += i * temp_checksum
    dummy_offset = accumulator % 10

    # Output result
    print(f"Result: {final_score}")
    return final_score

# Input log string
log_input = 'TS:2023-04-15-14|EFF:78|ERR:critical,fault,resync|MEM:67|OTHER:debug'
analyze_log(log_input)