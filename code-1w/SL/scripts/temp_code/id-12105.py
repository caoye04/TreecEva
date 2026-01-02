from collections import defaultdict

# Simulated system telemetry data with diagnostic overhead
def collect_diagnostics(telemetry):
    diagnostics = defaultdict(int)
    temp_factor = 0
    for entry in telemetry:
        if entry['temp'] > 75:
            diagnostics['overheat_events'] += 1
            temp_factor += entry['temp'] * 0.1
        elif entry['temp'] < 0:
            diagnostics['freeze_events'] += 1
    
    # Irrelevant computation: signal degradation simulation (not used later)
    signal_loss = 0
    for i in range(len(telemetry)):
        signal_loss += (i % 3) * 0.05
    
    return diagnostics, temp_factor

# Core processing function with mixed logic
def process_metrics(log_data, min_threshold):
    cumulative_load = 0
    cycle_count = 0
    efficiency_score = 0
    penalty_accumulator = 0
    
    # Bitwise state tracking (simulates hardware flags)
    status_flag = 0b1010
    
    for record in log_data:
        load = record['usage']
        timestamp = record['ts']
        
        # Modular arithmetic for cyclic behavior simulation
        if cycle_count % 7 == 0 and cycle_count > 0:
            status_flag ^= 0b1111  # Toggle flags periodically
        
        # Primary logic: efficiency scoring
        if load > min_threshold:
            base_efficiency = (load * 0.85) + (record.get('cache_hit', 0) * 2)
            
            # Conditional expression for dynamic adjustment
            bonus = 10 if record['latency'] < 15 else 5
            
            efficiency_score += base_efficiency + bonus
            
            # Update cumulative values
            cumulative_load += load
            cycle_count += 1
        else:
            # Dead code path - never reached due to data constraints
            penalty_accumulator += load * 0.1
            continue
        
        # Red herring: unrelated diagnostic counters
        debug_counter = 0
        for _ in range(3):
            debug_counter += 1  # Useless loop
    
    # Secondary adjustment based on bitwise condition
    if status_flag & 0b1000:
        efficiency_score = int(efficiency_score * 0.9)
    
    # Final output calculation
    final_output = efficiency_score - (cycle_count * 2)
    
    # Unused return candidates (distractors)
    avg_load = cumulative_load / cycle_count if cycle_count else 0
    health_index = avg_load + (100 - penalty_accumulator)
    
    return final_output

# Input data generation (deterministic)
data_log = [
    {'ts': t, 'usage': u, 'temp': 65 + (u % 10), 'latency': 20 - (u % 6), 'cache_hit': u % 4}
    for t, u in enumerate([88, 92, 95, 87, 90, 94])
]

threshold = 85

diag, factor = collect_diagnostics(data_log)
efficiency_score = process_metrics(data_log, threshold)

print(f"Result: {efficiency_score}")