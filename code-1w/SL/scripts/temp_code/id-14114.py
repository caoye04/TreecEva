import math

# System calibration constants (irrelevant to final result)
CALIBRATION_OFFSET = 0.00314
REFERENCE_VOLTAGE = 5.0
BASELINE_NOISE_FLOOR = 0.02

# Quantum register simulation with decoy and real data paths
quantum_registers = [
    {'state': 1, 'coherence': 0.88, 'timestamp': 1623456789, 'parity': 1},
    {'state': 0, 'coherence': 0.91, 'timestamp': 1623456792, 'parity': 0},
    {'state': 1, 'coherence': 0.85, 'timestamp': 1623456795, 'parity': 1},
    {'state': 1, 'coherence': 0.87, 'timestamp': 1623456798, 'parity': 1}
]

# Decoy system: energy fluctuation modeling (dead code path)
def compute_energy_fluctuations(registers):
    total_energy = 0.0
    for r in registers:
        freq = r['coherence'] * 1e9
        energy = 6.626e-34 * freq
        total_energy += energy + CALIBRATION_OFFSET
    return total_energy

# Irrelevant signal processing chain
def filter_signal(data_stream):
    filtered = []
    for point in data_stream:
        if point['coherence'] > 0.86:
            adjusted = point['coherence'] * REFERENCE_VOLTAGE
            filtered.append(adjusted - BASELINE_NOISE_FLOOR)
    return filtered

# Fake diagnostic routine (never called)
def deprecated_diagnostic(seq):
    cumulative = 0
    for i in range(len(seq)):
        cumulative += seq[i]['timestamp'] % (i + 1) if i > 0 else 0
    return cumulative

# Real logic buried among distractions
status_flags = {
    'INIT': 0x01,
    'RUNNING': 0x02,
    'STANDBY': 0x04,
    'ERROR': 0x08,
    'SYNCED': 0x10
}

system_mode = status_flags['RUNNING'] | status_flags['SYNCED']
mode_check = (system_mode & status_flags['ERROR']) == 0  # Should be True

# Data transformation with conditional expression
normalized_states = [
    {'weight': reg['coherence'] ** 2, 'active': True if reg['state'] == 1 else False}
    for reg in quantum_registers
]

# Red herring: matrix-like structure with no impact
redundant_correlation_matrix = [
    [math.cos(reg['coherence'] * math.pi) for reg in quantum_registers],
    [math.sin(reg['coherence'] * math.pi / 2) for reg in quantum_registers]
]

# Critical counting/grouping operation buried in distraction
state_counter = {0: 0, 1: 0}
for reg in quantum_registers:
    state_counter[reg['state']] += 1

# Misleading average calculation (not used in final answer)
fake_average = sum(math.log(reg['coherence'] + 1) for reg in quantum_registers) / len(quantum_registers)

# Real computation hidden behind decoy
threshold_met_count = sum(
    1 for ns in normalized_states 
    if ns['weight'] > 0.75 and ns['active']
)

# Auxiliary function that looks important but isn't used
def generate_report(flags):
    report = {}
    for name, val in status_flags.items():
        report[name] = bool(flags & val)
    report['INTEGRITY'] = report['RUNNING'] and report['SYNCED']
    return report

# Core analysis function — only this contributes to final answer
def analyze_system_state(registers):
    # Step 1: extract timestamps
    timestamps = [r['timestamp'] for r in registers]
    
    # Step 2: compute time deltas
    deltas = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps)-1)]
    
    # Step 3: find median delta
    sorted_deltas = sorted(deltas)
    median_delta = sorted_deltas[len(sorted_deltas)//2]
    
    # Step 4: count high-coherence active states
    high_coherence_active = sum(
        1 for r in registers 
        if r['coherence'] > 0.86 and r['state'] == 1
    )
    
    # Step 5: combine using arithmetic and bit manipulation
    raw_score = (median_delta << 2) + high_coherence_active  # shift adds complexity
    
    # Step 6: apply conditional adjustment
    adjustment = 5 if mode_check else -5
    
    # Step 7: use dictionary lookup for scaling factor
    scaling_map = {2: 1.5, 3: 2.0, 4: 2.5}
    scale = scaling_map.get(high_coherence_active, 1.0)
    
    # Step 8: final diagnostic calculation
    diagnostic_value = (raw_score + adjustment) * scale
    
    # Step 9: truncate to integer (deterministic)
    return int(diagnostic_value)

# Execute main analysis
final_diagnostic = analyze_system_state(quantum_registers)

# Print result as required
print(f"Target result: {final_diagnostic}")