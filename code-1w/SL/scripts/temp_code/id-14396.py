from collections import defaultdict

def analyze_system_load():
    # Simulate time-series resource monitoring
    timestamps = list(range(10))
    base_load = [120, 135, 140, 160, 175, 180, 170, 155, 145, 140]
    redundancy_factor = 1.4
    threshold_capacity = 200
    emergency_buffer = 35
    peak_capacity = 0
    total_fluctuation = 0
    maintenance_mode = False
    
    # Historical tracking (distractor)
    load_history = defaultdict(int)
    fluctuation_log = []
    
    for t in timestamps:
        current_load = base_load[t]
        projected_load = current_load * redundancy_factor
        
        # Update history (semi-relevant)
        load_history[t] = current_load
        
        # Calculate momentary fluctuation (distractor)
        if t > 0:
            delta = abs(current_load - base_load[t-1])
            fluctuation_log.append(delta)
            total_fluctuation += delta
        
        # Core logic: track peak under safety margin
        safe_capacity = projected_load + emergency_buffer
        if safe_capacity > peak_capacity:
            peak_capacity = safe_capacity
        
        # Simulated anomaly detection (dead code path)
        anomaly_score = sum(1 for x in base_load[:t+1] if x > 150)
        if anomaly_score > 10:
            maintenance_mode = True

        # Critical control flow
        reserve_margin = threshold_capacity - current_load
        if reserve_margin < threshold_capacity and not maintenance_mode:
            break
        
        # Irrelevant post-check adjustment (misleading)
        temp_adjustment = (t + 1) * 0.95
        peak_capacity = max(peak_capacity, temp_adjustment)

    # Final correction unrelated to loop logic
    final_audit = ''.join([str(int(x))[-1] for x in base_load]).count('5')
    peak_capacity -= final_audit * 1.5

    print(f"Result: {peak_capacity}")

analyze_system_load()