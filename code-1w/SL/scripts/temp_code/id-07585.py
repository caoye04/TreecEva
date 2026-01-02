def analyze_system_load(baseline, requests, response_times):
    avg_response = sum(response_times) / len(response_times) if response_times else 0
    peak_load = max(requests) if requests else 0
    normalized_load = (peak_load - baseline) / baseline if baseline else 0
    
    # Irrelevant health check simulation
    system_health = 'stable'
    if peak_load > 2 * baseline:
        system_health = 'critical'
    elif peak_load > 1.5 * baseline:
        system_health = 'warning'
    
    # Distractor: unused computation
    jitter = max(response_times) - min(response_times) if response_times else 0
    smoothed_jitter = jitter * 0.85

    return avg_response, normalized_load

# Simulated monitoring data
timestamps = [1000, 1001, 1002, 1003, 1004]
raw_data = [(t, t%3 + 5, (t%4)*2 + 10) for t in timestamps]
requests_per_sec = [d[1] for d in raw_data]
latency_samples = [d[2] for d in raw_data]

baseline_capacity = 4
avg_latency, load_ratio = analyze_system_load(baseline_capacity, requests_per_sec, latency_samples)

# Secondary metric processing with conditional expressions
threshold = 12
exceedance_count = sum(1 for lat in latency_samples if lat > threshold)
penalty_factor = 1.5 if exceedance_count > 2 else 1.0

# Bitwise flag encoding (only one bit used meaningfully)
error_flag = (exceedance_count << 2) | (0x1 if load_ratio > 1.0 else 0x0)
status_code = error_flag ^ 0x5  # Red herring

# Core calculation chain
efficiency_score = 100 - (load_ratio * 10)
speed_bonus = 10 if avg_latency < 12 else 5 if avg_latency < 15 else 0

# Unused diagnostic log
log_entry = f"Load:{load_ratio:.2f}|Score:{efficiency_score}" if load_ratio > 0.8 else "Normal"

# Key function with lambda and string method distraction
def process_metrics(tput, late, flag):
    # Complex but focused logic
    base = (tput * 3.5) - (late * 0.8)
    
    # Conditional expression based on bitwise inspection
    adjustment = -15 if (flag & 0x1) else 10
    
    # Lambda for dynamic weight (used)
    dynamic_weight = lambda x: 1.2 if x > 6 else 0.9
    weighted_adj = adjustment * dynamic_weight(tput)
    
    # String-based switch emulation (distractor)
    mode_str = "high" if tput > 6 else "low"
    saturation_level = {"high": 1.1, "medium": 1.0}.get(mode_str, 1.0)
    
    intermediate = base + weighted_adj
    
    # Final nonlinear transformation
    final = int(intermediate * saturation_level + 5)
    
    # Dead code path
    if False:
        final = max(final, 50)
    
    return final

throughput = sum(requests_per_sec) / len(requests_per_sec)
final_score = process_metrics(throughput, avg_latency, error_flag)
print(f"Target result: {final_score}")