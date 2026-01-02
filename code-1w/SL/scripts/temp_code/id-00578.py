import math

# System calibration constants (irrelevant to final result)
CALIBRATION_OFFSET = 0.0034
REFERENCE_VOLTAGE = 5.0
TEMP_CORRECTION_FACTOR = 0.987

# Quantum register simulation with decoy data
quantum_registers = [
    {'state': [1, 0, 1], 'phase': 0.12, 'energy': 42.5},
    {'state': [0, 1, 1], 'phase': 0.78, 'energy': 38.1},
    {'state': [1, 1, 0], 'phase': 0.45, 'energy': 45.3},
    {'state': [1, 1, 1], 'phase': 0.91, 'energy': 40.7}
]

# Irrelevant sensor arrays and dead-path variables
sensor_readings = [[0.1, 0.4, 0.2], [0.8, 0.6, 0.9]]
temp_buffer = [0] * 10
diagnostic_log = []

# Decoy function that is never called
def compute_entropy(data):
    return sum(-x * math.log(x) for x in data if x > 0)

# Auxiliary function with misleading intermediate calculations
def normalize_phase(value):
    normalized = (value % (2 * math.pi)) / math.pi
    # Distractor: correction not actually used
    corrected = normalized * TEMP_CORRECTION_FACTOR
    return round(normalized, 3)

# Function that processes quantum state bits (actually relevant)
def count_coherent_ones(register_list):
    total = 0
    for reg in register_list:
        # Only 'state' matters; 'phase' and 'energy' are red herrings
        coherent_bits = [bit for bit in reg['state'] if bit == 1]
        total += len(coherent_bits)
    return total

# Bit manipulation decoy
def shift_diagnostic_code(code):
    shifted = (code << 3) & 0xFF
    inverted = shifted ^ 0xAA
    return inverted  # Never used

# Real processing chain
status_flags = {
    'initialized': True,
    'calibrated': False,
    'verified': True
}

# Simulated pre-checks with irrelevant logic
validation_score = 0
if status_flags['initialized']:
    validation_score += 10
if status_flags['calibrated']:
    validation_score -= 5  # Dead path
if status_flags['verified']:
    validation_score += 15

# Linear search through registers (only some fields matter)
def extract_critical_indices(registers):
    indices = []
    for i, r in enumerate(registers):
        # Energy values are distraction; only state length is used
        if sum(r['state']) >= 2:
            indices.append(i)
    return indices  # Used later

# Main analysis function with multiple layers
def analyze_system_state(qregs):
    # Step 1: Extract indices where at least two bits are set
    critical_positions = extract_critical_indices(qregs)
    
    # Step 2: Count total coherent ones across all registers
    coherence_count = count_coherent_ones(qregs)
    
    # Step 3: Apply fake normalization (distraction)
    fake_normalized = 0
    for reg in qregs:
        fake_normalized += normalize_phase(reg['phase'])
    
    # Step 4: Build diagnostic map using dictionary operations
    diagnostic_map = {i: qregs[i]['energy'] for i in range(len(qregs))}
    
    # Step 5: Use list comprehension to filter high-energy registers (decoy)
    high_energy_regs = [e for e in diagnostic_map.values() if e > 40.0]
    
    # Step 6: Compute entropy proxy (not real entropy, just sum of squares)
    entropy_proxy = sum(x * x for x in high_energy_regs) / 1000.0
    
    # Step 7: Combine coherence count with number of critical positions
    structural_weight = len(critical_positions)
    
    # Step 8: Final diagnostic is based ONLY on coherence_count and structural_weight
    # All other computations above are distractions
    final_score = (coherence_count * 17) + (structural_weight * 5)
    
    # Misleading adjustment
    if entropy_proxy > 1.0:
        final_score -= 2  # Not triggered due to actual values
    
    return final_score

# Execute main logic
final_diagnostic = analyze_system_state(quantum_registers)

# Print result as required
print(f"Result: {final_diagnostic}")