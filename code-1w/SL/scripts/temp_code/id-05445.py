import math

# System calibration constants (irrelevant to final result)
CALIBRATION_OFFSET = 0.0034
TEMPERATURE_FACTOR = 1.02
REFERENCE_VOLTAGE = 3.3

# Quantum register simulation with decoherence modeling
quantum_registers = [
    {'state': 7, 'coherence': 0.88, 'flag': False},
    {'state': 15, 'coherence': 0.92, 'flag': True},
    {'state': 3, 'coherence': 0.76, 'flag': False},
    {'state': 12, 'coherence': 0.81, 'flag': True}
]

# Auxiliary monitoring system (distractor variables)
cpu_temperature = 67.4
memory_usage_mb = 2048
network_latency_ms = 12.7
system_uptime_hours = 142

# Decoy function - appears important but unused in critical path
def compute_thermal_drift(temp, voltage):
    return (temp * 0.01 + voltage * 0.05) * CALIBRATION_OFFSET

# Simulated sensor array (red herring data)
sensor_readings = {
    'accel_x': 0.12,
    'accel_y': -0.03,
    'gyro_z': 0.45,
    'mag_field': 23.1
}

# Misleading intermediate calculation (dead code path)
def evaluate_signal_integrity(readings):
    base_score = 0
    for key, value in readings.items():
        if 'accel' in key:
            base_score += abs(value) * 10
        elif 'gyro' in key:
            base_score += abs(value) * 5
    return round(base_score, 2)

# Unused recursive diagnostic (decoy)
def recursive_health_check(level=3):
    if level <= 0:
        return 1
    return level * recursive_health_check(level - 1) + 2

# Core analysis pipeline
status_map = {0: 'CRITICAL', 1: 'WARNING', 2: 'STABLE'}

# Data transformation matrix (partially relevant)
transformation_matrix = [
    [1, -1],
    [0.5, 0.5],
    [-1, 2],
    [0, 1]
]

# Primary processing function with multiple concerns
def preprocess_register(registers):
    processed = []
    total_coherence = 0
    
    for r in registers:
        # Apply fake environmental compensation
        adjusted_state = r['state'] + int(r['coherence'] * 100 % 4)
        
        # Real computation mixed with irrelevant operations
        entropy_factor = math.log(adjusted_state + 1) if adjusted_state > 0 else 0
        voltage_proxy = REFERENCE_VOLTAGE * (r['state'] / 16)
        
        # Actual signal extraction (key step)
        quantum_syndrome = adjusted_state & 7  # Extract lower 3 bits
        
        processed.append({
            'syndrome': quantum_syndrome,
            'entropy': entropy_factor,
            'voltage_proxy': voltage_proxy,
            'valid_flag': r['flag']
        })
        
        total_coherence += r['coherence']
    
    # Store intermediate metric (distractor)
    global system_stability_index
    system_stability_index = total_coherence / len(registers)
    
    return processed

# Secondary analysis with conditional logic
prev_results = None
def cache_aware_analysis(data):
    global prev_results
    
    if prev_results is None:
        checksum = 0
        for item in data:
            # Meaningful operation buried in noise
            if item['valid_flag']:
                checksum ^= item['syndrome']  # XOR accumulation
            
            # Irrelevant temperature adjustment
            adj_entropy = item['entropy'] * (1 + TEMPERATURE_FACTOR * 0.01)
            item['adjusted_entropy'] = round(adj_entropy, 3)
        
        prev_results = data
        return {'checksum': checksum, 'cached': False}
    else:
        return {'checksum': -1, 'cached': True}

# Final diagnostic engine
def analyze_system_state(registers):
    # Step 1: Preprocess raw register data
    processed_data = preprocess_register(registers)
    
    # Step 2: Perform cache-aware analysis
    analysis_outcome = cache_aware_analysis(processed_data)
    
    # Step 3: Extract key diagnostic signature
    active_syndromes = [item['syndrome'] for item in processed_data if item['valid_flag']]
    
    # Step 4: Compute primary diagnostic code (critical path)
    base_diagnostic = 0
    for syndrome in active_syndromes:
        base_diagnostic = (base_diagnostic * 3) + syndrome
    
    # Step 5: Apply non-linear transformation
    transformed_diagnostic = int(math.pow(base_diagnostic, 1.5))
    
    # Step 6: Conditional offset based on system state
    offset = 0
    if len(active_syndromes) >= 2 and system_stability_index > 0.8:
        offset = 50
    elif system_stability_index > 0.85:
        offset = 25
    
    # Step 7: Final adjustment using dictionary mapping (relevant feature)
    adjustment_map = {0: 10, 1: -5, 2: 15, 3: 0}
    key = len(active_syndromes) % 4
    adjustment = adjustment_map[key]
    
    # Step 8: Compute final result
    final_value = transformed_diagnostic + offset + adjustment
    
    # Red herring: Update fake metrics
    global network_latency_ms, memory_usage_mb
    network_latency_ms += 0.5
    memory_usage_mb = int(memory_usage_mb * 1.01)
    
    return final_value

# Execute main analysis
final_diagnostic = analyze_system_state(quantum_registers)
print(f"Result: {final_diagnostic}")