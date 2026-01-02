from itertools import accumulate

# System health monitoring with adaptive thresholds
def compute_threshold():
    base_readings = [12, 15, 10, 8, 20]
    adjustments = [3, -2, 5, -1, 4]
    
    # Compute cumulative system load
    cumulative_load = list(accumulate(base_readings))
    total_adjusted_load = sum(cumulative_load) + sum(adjustments)
    
    # Determine base score from adjusted load
    base_score = total_adjusted_load // len(base_readings)
    
    # Evaluate eligibility based on trend
    increasing_trend = all(base_readings[i] <= base_readings[i+1] for i in range(len(base_readings)-1))
    critical_peak = max(base_readings) > 18
    
    is_eligible = increasing_trend or critical_peak
    
    # Apply conditional logic for threshold assignment
    penalty = 7
    final_rank = base_score * 2
    threshold_score = final_rank if is_eligible else base_score + penalty
    
    # Irrelevant auxiliary variable (minimal distraction)
    debug_mode = False
    
    print(f"Result: {threshold_score}")

compute_threshold()