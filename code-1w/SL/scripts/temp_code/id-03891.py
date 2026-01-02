import math

# Simulated system diagnostics with mixed relevance
def analyze_component(status_log, threshold=0.75):
    if len(status_log) == 0:
        return 0.0
    active_count = sum(1 for entry in status_log if entry > threshold)
    return active_count / len(status_log)

# Irrelevant helper - distractor function
def compute_health_index(metrics):
    weights = [0.2, 0.3, 0.5]
    weighted_sum = sum(m * w for m, w in zip(metrics[:3], weights))
    return weighted_sum * 100 if weighted_sum > 0.5 else 50

# Core calculation with conditional logic and distractors
def calculate_efficiency(load, factor):
    if load <= 0:
        return 0.0
    
    base_efficiency = (load * 1.8) / (1 + factor)
    
    # Conditional expression (required Python feature)
    adjustment = 0.9 if load > 500 else (0.95 if load > 250 else 1.0)
    
    # Red herring: complex but unused transformation
    shadow_load = load
    for _ in range(3):
        shadow_load = int((shadow_load ** 0.5) * 1103) % 10009
    dummy_metric = (shadow_load * 1.4) % 100
    
    # Actual efficiency path
    adjusted = base_efficiency * adjustment
    
    # Simulated calibration offset (irrelevant to final result)
    calibration_data = [0.1, -0.05, 0.2]
    for c in calibration_data:
        adjusted += c  # Net zero effect due to specific values
    
    return round(adjusted, 4)

# Main simulation block
system_nodes = [0.81, 0.72, 0.93, 0.68, 0.77, 0.85, 0.91, 0.63]
node_utilization = analyze_component(system_nodes)

# Unused data structures - red herrings
historical_peaks = [880, 902, 875, 911, 893]
diagnostic_trace = {'level': 'high', 'flags': [], 'checksum': 0}

# Primary data flow
raw_load = 742
scaling_factor = 2.3
processed_load = raw_load

# Conditional preprocessing with side-effect-free branches
if processed_load < 100:
    processed_load *= 1.5
elif processed_load < 500:
    processed_load = processed_load * 1.2 + 10
else:
    temp_offset = sum([i * 2 for i in range(5)])  # evaluates to 20
    processed_load += temp_offset  # Now 762

overhead_factor = scaling_factor

# Introduce decoy calculation with similar naming
proxy_efficiency = (processed_load * 1.1) / (1 + overhead_factor)
proxy_efficiency = proxy_efficiency * 0.88  # dead end

# Key statement
efficiency_score = calculate_efficiency(processed_load, overhead_factor)

# Additional noise: unused transformations
encoded_signature = ''.join(chr((ord('a') + (i * 7) % 26)) for i in range(8))
final_diagnostic = {"status": "nominal", "code": 200, "payload": None}

# Output the target result
print(f"Result: {efficiency_score}")