def analyze_workload(stats):
    if not stats:
        return 0
    
    # Irrelevant computation block - distractor
    temp_result = 0
    for k in stats:
        if len(k) % 2 == 0:
            temp_result += ord(k[0])
    temp_result = (temp_result * 3) % 100

    # Real logic begins: extract and process performance metrics
    cpu_load = stats.get('cpu', 0)
    mem_usage = stats.get('memory', 0)
    disk_io = stats.get('disk', 0)
    network_activity = stats.get('network', 0)

    # Misleading intermediate normalization (not used in final result)
    normalized = []
    for val in [cpu_load, mem_usage, disk_io]:
        norm_val = round(val / (sum([cpu_load, mem_usage, disk_io]) + 1e-5), 3)
        normalized.append(norm_val * 100)

    # Conditional expression chain with bit manipulation
    efficiency = cpu_load - (mem_usage >> 1)
    if disk_io > 50:
        efficiency += 10
    elif network_activity < 20:
        efficiency -= 5
    else:
        efficiency ^= 7  # red herring, never reached due to prior branches

    # Unused helper logic - dead code path
    def adjust_value(x):
        return (x << 2) | 1
    
    # Distractor: tuple unpacking with irrelevant data
    metadata = ('system_scan', 'v1.2', 'debug_off')
    scan_type, version, _ = metadata

    # Dictionary-based threshold mapping (core relevant logic)
    severity_map = {
        'low': (0, 30),
        'moderate': (31, 70),
        'high': (71, 100)
    }
    
    # Simulated state tracking across multiple conditions
    status_flags = []
    if efficiency < 40:
        status_flags.append('throttled')
    if mem_usage > 85:
        status_flags.append('overloaded')
    if disk_io in range(20, 40):
        status_flags.append('optimal_disk')

    # Actual metric used in final evaluation
    base_metric = efficiency + (10 if 'optimal_disk' in status_flags else 0)

    return base_metric


def evaluate_performance(data, limits):
    # Redundant sorting - does not affect outcome
    sorted_keys = sorted(data.keys(), key=lambda x: len(x))
    
    # Bitwise distraction
    magic_offset = (13 ^ 7) & 3  # evaluates to 2, but unused

    # Logical operations with short-circuiting
    primary = data.get('cpu', 0) > limits.get('high', 70) or data.get('memory', 0) > 90
    secondary = data.get('disk', 0) < limits.get('low', 25) and data.get('network', 0) > 50

    # Early return trap - condition never true due to input constraints
    if primary and secondary:
        return -1  # unreachable in this context

    # Core calculation: only this matters
    raw_score = analyze_workload(data)
    adjustment = 5 if primary else -3
    
    # Final composition using dictionary lookup
    category = 'high' if raw_score >= 60 else 'moderate'
    min_thresh, max_thresh = limits.get(category, (0, 50))
    
    # The actual answer-determining line
    final_score = (raw_score + adjustment) * (max_thresh // 50)
    
    # Print required output
    print(f"Result: {final_score}")
    return final_score

# Input construction with plausible distractions
metric_data = {
    'cpu': 68,
    'memory': 78,
    'disk': 35,
    'network': 15,
    'gpu': 45,  # unused field
    'temperature': 67  # dead data
}

thresholds = {
    'low': 20,
    'high': 75
}

# Trigger execution
final_score = evaluate_performance(metric_data, thresholds)