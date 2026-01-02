import itertools

# Simulated sensor array data from a distributed monitoring system
def collect_sensor_readings():
    base_values = [0.88, 0.92, 0.76, 0.94, 0.81]
    adjustments = [0.02, -0.01, 0.03, -0.02, 0.01]
    readings = [base + adj for base, adj in zip(base_values, adjustments)]
    return readings

# Legacy function – appears important but unused in critical path
def legacy_normalization(data):
    max_val = max(data)
    return [x / max_val for x in data]

# Decoy function that looks relevant but is never called in execution path
def compute_fusion_index(x, y):
    temp = 0
    for i in range(len(x)):
        temp += x[i] * y[(i+1) % len(y)]
    return temp ** 0.5 if temp > 0 else 0

# Bit manipulation red herring - simulates low-level optimization
sensor_flags = 0b110101
mask = 0b111100
masked_flags = sensor_flags & mask  # Irrelevant to final result

# Unused intermediate calculation - distractor
redundant_score = sum([i * 0.77 for i in range(5)])

# System load levels (simulated)
system_load = list(range(60, 100, 8))  # [60, 68, 76, 84, 92]

# Health signature derived from sensor fusion
health_signature = sum(collect_sensor_readings()) * 100  # Key value: ~385.0

# Secondary distractor: complex but unused data structure
status_matrix = list(itertools.product([True, False], repeat=3))
duplicate_count = len([x for x in status_matrix if sum(x) == 2])

# Auxiliary transformation that feeds into real computation
def transform_load(load_seq):
    filtered = [x for x in load_seq if x > 70]
    scaled = map(lambda val: val * 0.618, filtered)  # Use of lambda
    return list(scaled)

# Core processing with nested logic and multiple concepts
def process_metrics(health, loads):
    adjusted_loads = transform_load(loads)
    
    # Multi-step conditional logic with red herrings
    baseline = 380.0
    threshold = baseline + 10
    
    # Simulated calibration offset (distractor)
    calib_offset = 0
    for i in range(3):
        calib_offset += i * 0.15  # Ends at 0.3
    
    # Real computation begins
    if health > threshold:
        stage_factor = 1.2
    elif health > baseline:
        stage_factor = 1.0
    else:
        stage_factor = 0.8
    
    # Complex aggregation with generator expression (itertools flavor)
    windowed = [adjusted_loads[i:i+2] for i in range(len(adjusted_loads)-1)]
    correlations = [(a * b) for a, b in windowed]  # Pairwise product
    
    # Final diagnostic computed through non-obvious chain
    aggregate = sum(correlations)  # ~ (76*0.618)*(84*0.618) + ...
    final_diagnostic = int((health * stage_factor) + aggregate)  # Critical line
    
    # Dead code branch - never executed due to prior conditions
    if False and calib_offset > 1.0:
        final_diagnostic *= 0.9
        
    return final_diagnostic

# Execution point of interest
final_diagnostic = process_metrics(health_signature, system_load)
print(f"Result: {final_diagnostic}")