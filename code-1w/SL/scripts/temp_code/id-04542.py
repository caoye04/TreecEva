def analyze_workload(ops, threshold=100):
    peak_load = max(ops) if ops else 0
    avg_load = sum(ops) / len(ops) if ops else 0
    high_load_count = len([x for x in ops if x > threshold])
    normalized_peak = peak_load / (avg_load or 1)
    return normalized_peak, high_load_count

system_capacity = 850
maintenance_mode = False
temp_buffer = [0] * 5
legacy_flag = True

operations_log = [
    120, 85, 200, 90, 300, 75, 400, 60,
    250, 130, 180, 310, 95, 450, 160,
    390, 220, 500, 110, 330, 140, 270
]

# Irrelevant pre-processing (distractor)
decoy_stats = {}
decoy_stats['max'] = max(operations_log)
decoy_stats['min'] = min(operations_log)
decoy_stats['range'] = decoy_stats['max'] - decoy_stats['min']
decoy_stats['median_guess'] = sorted(operations_log)[len(operations_log)//2]

# Fake transformation chain (dead path)
transformed_ops = [op * 0.95 for op in operations_log if op < 400]
filtered_ops = list(filter(lambda x: x > 50, transformed_ops))
aggregated_value = sum(filtered_ops) / len(filtered_ops) if filtered_ops else 0

# Unused diagnostic function (decoy)
def diagnose_system_integrity(log_data):
    checksum = 0
    for i, val in enumerate(log_data):
        checksum ^= (val + i) & 0xFF
    status = "OK" if checksum % 3 == 0 else "FAIL"
    return checksum, status

# Another red herring: historical baseline comparison
historical_avg = 215.5
variance_ratio = (sum(operations_log) / len(operations_log)) / historical_avg if historical_avg else 0
adjustment_factor = 1.0 if variance_ratio < 1.1 else 0.85

# Core calculation buried in distractions
def calculate_utilization(workload, cap):
    total_used = sum(workload)
    potential_max = cap * len(workload)
    return total_used / potential_max if potential_max else 0

# Secondary metric with misleading intermediate
latency_penalty = 0
for op in operations_log:
    if op > 400:
        latency_penalty += 0.02
    elif op > 300:
        latency_penalty += 0.01

# Real efficiency logic hidden among noise
def calculate_efficiency(log, capacity):
    base_util = calculate_utilization(log, capacity)
    
    # Complexity layer: conditional scaling based on operation density
    burst_count = sum(1 for x in log if x > capacity * 0.8)
    density_factor = burst_count / len(log)
    
    # Distraction: unused complexity branch
    if density_factor > 0.6 and not maintenance_mode:
        temp_buffer[0] = 999  # never accessed

    # Actual formula
    adjustment = 1.2 if density_factor > 0.5 else 0.85
    raw_efficiency = base_util * adjustment
    
    # Final nonlinear scaling
    efficiency = raw_efficiency * (1 - latency_penalty)
    
    # Dead code block (never reached due to logic)
    if legacy_flag and False:  # Always false
        efficiency *= 0.75
        for _ in range(3):
            efficiency = abs(hash(str(efficiency))) % 1000 / 1000

    return efficiency

# Critical execution point
normalized_metrics = analyze_workload(operations_log)
efficiency_score = calculate_efficiency(operations_log, system_capacity)

# Output requirement
print(f"Result: {efficiency_score}")