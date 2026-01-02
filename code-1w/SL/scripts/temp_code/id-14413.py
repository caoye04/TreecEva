import itertools

# System health monitoring simulation with red herrings and complex logic paths
def analyze_component_status(sensor_data, threshold_sequence):
    cumulative_stress = 0
    peak_anomaly = 0
    for i, reading in enumerate(sensor_data):
        if i % 3 == 0:
            cumulative_stress += reading * 0.7
        elif reading > threshold_sequence[i % len(threshold_sequence)]:
            peak_anomaly = max(peak_anomaly, reading - threshold_sequence[i % len(threshold_sequence)])
    return cumulative_stress > 150 or peak_anomaly > 25

# Distractor function - looks important but unused in final calculation
def compute_redundancy_score(node_list, failover_chain):
    score = 0
    for node in node_list:
        score += (node ** 2) % 7
    return score * len(failover_chain)

# Core diagnostic engine with conditional expressions and itertools usage
def generate_health_vector(base_pattern, iterations):
    expanded = list(itertools.accumulate(base_pattern, lambda x, y: (x + y) % 100))
    toggled = [val if idx % 2 == 0 else val * 1.1 for idx, val in enumerate(expanded)]
    return [round(v, 2) for v in toggled[:iterations]]

# Misleading preprocessing path - dead code branch
obsolete_flags = [True, False, True]
legacy_mode = any(obsolete_flags) and not all(obsolete_flags)

# Simulated sensor inputs - some relevant, some decoys
temp_readings = [23, 45, 67, 89, 31, 73, 94, 25, 66]
pressure_sequence = [101, 205, 130, 99, 210]  # Unused in final logic
clock_cycles = [512, 1024, 2048, 4096]

# Critical health signature generation
baseline = [34, 87, 56, 92, 44, 71]
health_vector = generate_health_vector(baseline, 6)

# Irrelevant transformation chain
shadow_copy = [x ^ 15 for x in clock_cycles]
dummy_aggregate = sum(shadow_copy) / len(shadow_copy)

# Conditional expression with nested logic
system_load = len(temp_readings) > 7 else len(temp_readings) < 5

# Another red herring: complex but unused bitwise analysis
event_flag = 0b101010
for cycle in clock_cycles:
    event_flag ^= (cycle & 0b1111)
event_flag = event_flag << 2 | (event_flag >> 6)

# Key control variable derived from health vector
trigger_condition = any(x > 85 for x in health_vector)

# Primary status matrix - looks like it might be used
status_matrix = [[i + j for j in range(4)] for i in range(4)]

# Decoy assignment with string manipulation that appears significant
log_entry = "DIAG_" + "".join([chr(65 + (len(baseline) % 26)) for _ in range(3)])
debug_tag = log_entry.replace("DIAG", "TRACE")

# Real processing begins here - hidden among distractions
def evaluate_stability(metrics):
    base_score = metrics[0] * 1.3
    adjustment = metrics[3] * 0.8 if len(metrics) > 3 else 0
    penalty = 45 if trigger_condition else 0
    return base_score + adjustment - penalty

# Final processing function combining boolean logic and arithmetic
def process_metrics(signature, load_factor):
    raw_value = evaluate_stability(signature)
    multiplier = 2.5 if load_factor and len(signature) >= 6 else 1.8
    intermediate = raw_value * multiplier
    
    # Additional filtering using logical operations
    filter_criteria = (
        intermediate > 100 and 
        signature[1] > 80 or 
        signature[2] < 60
    )
    
    # Final adjustment with conditional expression
    final_adjustment = -30 if not filter_criteria else 12
    
    result = intermediate + final_adjustment
    
    # This print is required for traceability
    return int(round(result))

# Execution point of interest
final_diagnostic = process_metrics(health_signature=health_vector, system_load=system_load)
print(f"Target result: {final_diagnostic}")