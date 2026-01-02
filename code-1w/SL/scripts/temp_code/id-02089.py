def analyze_efficiency(values):
    total = 0
    count = 0
    for v in values:
        if v > 0:
            total += v ** 0.5
            count += 1
    return total / count if count else 0

# Simulate system health metrics
cpu_load = [0.8, 0.9, 0.75, 1.0, 0.88]
memory_usage = [0.6, 0.7, 0.65, 0.8, 0.72]
disk_io = [120, 150, 130, 145, 135]  # Irrelevant metric (distraction)

# Normalize and combine relevant metrics
normalized_cpu = [1 - load for load in cpu_load]  # Invert for performance score
smoothed_memory = [round((1 - mem) * 100) / 100 for mem in memory_usage]

# Create performance tuples
performance_entries = []
for i in range(len(cpu_load)):
    performance_entries.append((normalized_cpu[i], smoothed_memory[i], i))

# Build metric dictionary with redundant fields
metrics = {}
for idx, (cpu_score, mem_score, original_idx) in enumerate(performance_entries):
    key = f"node_{idx}"
    metrics[key] = {
        'cpu': cpu_score,
        'memory': mem_score,
        'timestamp': idx * 10 + 162500,  # Distractor field
        'raw_index': original_idx,
        'weight': 1.0 if idx % 2 == 0 else 0.9  # Unused weight
    }

# Adjustment factors with some irrelevant logic
baseline_adjustment = 0.95
adjustments = {}
for k, v in metrics.items():
    adj = baseline_adjustment
    if v['cpu'] > 0.15:
        adj += 0.05
    if v['memory'] < 0.35:  # Never true, dead logic path
        adj -= 0.1
    adjustments[k] = round(adj, 2)

# Secondary distraction: simulate network latency (unused)
network_latency_ms = [23, 45, 30, 67, 55]
latency_penalty = sum([1 for x in network_latency_ms if x > 50]) * 0.01  # Computed but unused

# Core processing function
def process_performance(metric_dict, adj_dict):
    composite_scores = []
    temp_log = []  # Tracking for debugging (not used in result)
    
    for node_id, data in metric_dict.items():
        raw_score = data['cpu'] * 0.6 + data['memory'] * 0.4
        adjusted_score = raw_score * adj_dict[node_id]
        composite_scores.append(adjusted_score)
        
        # Log transformation (distractor computation)
        if adjusted_score > 0:
            log_val = round(-1 * (adjusted_score - 1), 3)
            temp_log.append(log_val)
    
    # Aggregate final score
    base_final = sum(composite_scores) / len(composite_scores)
    fluctuation = max(composite_scores) - min(composite_scores)
    stability_bonus = 0.98 if fluctuation < 0.1 else 0.95
    
    # Final adjustment using tuple unpacking (relevant)
    multiplier_tuple = (stability_bonus, 1.02)
    bonus_applied = False
    for mult in multiplier_tuple:
        if abs(mult - 1.0) < 0.03 and not bonus_applied:
            base_final *= mult
            bonus_applied = True
    
    # Distractor: unused dictionary aggregation
    summary_stats = {
        'count': len(composite_scores),
        'min_raw': min([d['cpu']*0.6 + d['memory']*0.4 for d in metric_dict.values()]),
        'max_adj': max(composite_scores),
        'debug_logs': len(temp_log)
    }
    
    return int(round(base_final * 100))  # Final result as integer percentage

# Execute main logic
final_score = process_performance(metrics, adjustments)
print(f"Result: {final_score}")