import math

# Simulated system performance metrics
latency_ms = 120
packet_loss = 0.05
throughput_mbps = 85
cpu_utilization = 78.3
temperature_c = 67

# Auxiliary irrelevant metrics (distractors)
memory_usage_mb = 2140
disk_io_ops = 198
network_jitter_ms = 4.2
fan_speed_rpm = 3400
voltage_stable = True

# Threshold baselines (some are decoys)
THRESHOLD_LATENCY = 100
THRESHOLD_LOSS = 0.02
THRESHOLD_THROUGHPUT = 90
THRESHOLD_CPU = 80
DECOY_THRESHOLD_1 = 500
DECOY_THRESHOLD_2 = 15.5

# Scoring weights (only some are actually used)
weight_latency = 0.3
weight_loss = 0.25
weight_throughput = 0.35
weight_cpu = 0.1

# Irrelevant weight variables (red herrings)
weight_memory = 0.08
weight_temp = 0.05
weight_jitter = 0.12

# Boolean flags based on thresholds (some influence logic, others don't)
high_latency = latency_ms > THRESHOLD_LATENCY
excessive_loss = packet_loss > THRESHOLD_LOSS
low_throughput = throughput_mbps < THRESHOLD_THROUGHPUT
cpu_overloaded = cpu_utilization > THRESHOLD_CPU
temp_critical = temperature_c > 70  # Not actually used

# Conditional adjustment factors (complex interdependencies)
adjustment_factor = 1.0
if high_latency:
    adjustment_factor *= 0.9
    if excessive_loss:
        adjustment_factor *= 0.85
elif low_throughput:
    adjustment_factor *= 0.95

if cpu_overloaded:
    adjustment_factor *= 0.88

# Define scoring function using lambda (relevant)
calculate_base_score = lambda tp, lt, pl, cpu: (tp * weight_throughput + 
                                             (100 - lt) * weight_latency + 
                                             (1 - pl * 100) * weight_loss + 
                                             (100 - cpu) * weight_cpu)

# Compute base score
base_score = calculate_base_score(throughput_mbps, latency_ms, packet_loss, cpu_utilization)

# Apply adjustment
adjusted_score = base_score * adjustment_factor

# Create diagnostic set with multiple operations (set usage)
diagnostic_flags = {"latency", "loss", "throughput", "cpu"}
active_issues = set()
if high_latency:
    active_issues.add("latency")
if excessive_loss:
    active_issues.add("loss")
if low_throughput:
    active_issues.add("throughput")
if cpu_overloaded:
    active_issues.add("cpu")

# Simulated resolution attempts (dead code path - never executed)
if temp_critical:
    for i in range(3):
        fan_speed_rpm += 200
        voltage_stable = False

# Bit manipulation red herring (irrelevant)
system_signature = (latency_ms ^ int(packet_loss * 1000)) & 0xFF
encryption_key = (system_signature << 4) | 0x0A

# Decoy transformation chain
transformed_metric = math.sqrt(latency_ms ** 2 + throughput_mbps * 10)
filtered_value = transformed_metric if transformed_metric > 150 else 150

# Core evaluation metric set (used in final function)
metric_set = {
    'base': base_score,
    'adjusted': adjusted_score,
    'issues': len(active_issues),
    'factor': adjustment_factor
}

# Final evaluation function with closure and lambda
def evaluate_performance(metrics):
    initial = metrics['base']
    factor = metrics['factor']
    issues = metrics['issues']
    
    # Internal corrective mapping (not obviously related)
    penalty_map = {0: 1.0, 1: 0.95, 2: 0.85, 3: 0.7, 4: 0.5}
    issue_penalty = penalty_map.get(issues, 0.3)
    
    # Secondary adjustment via lambda
    smooth_penalty = lambda x: x * 0.99 if x > 90 else x * 0.96
    
    intermediate = initial * factor
    if issues > 0:
        intermediate *= issue_penalty
    
    # Apply smoothing only if no CPU overload (conditional logic)
    cpu_issue_flag = cpu_overloaded  # shadow read
    if not cpu_issue_flag:
        intermediate = smooth_penalty(intermediate)
    
    # Final nonlinear transformation
    final = int(intermediate * (1.05 ** issues))  # boost for issue count?
    
    # Counterintuitive fix: cap at 100 but add bonus if single issue
    if issues == 1 and high_latency and not excessive_loss:
        final = min(final + 5, 100)
    else:
        final = min(final, 100)
    
    return final

# Execute main evaluation
temp_diagnostic = math.log(throughput_mbps + 1)  # unused computation
baseline_comparison = base_score > 85  # misleading indicator

final_score = evaluate_performance(metric_set)

# Output result
print(f"Result: {final_score}")