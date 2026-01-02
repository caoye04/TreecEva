import math

# System calibration constants (irrelevant to final result)
CALIBRATION_OFFSET = 0.0037
REFERENCE_VOLTAGE = 3.3
TEMP_CORRECTION_FACTOR = 1.02

# Quantum register simulation arrays
qubit_states = [1, 0, 1, 1, 0, 1]
phase_shifts = [0.1, -0.4, 0.8, 0.0, 1.2, -0.7]
error_flags = {i: False for i in range(len(qubit_states))}

# Misleading diagnostic tracker (partially updated but not used in final logic)
misleading_diagnostics = {
    'aggregate_entropy': 0,
    'phase_variance': 0,
    'coherence_index': 0.0
}

# Auxiliary decoy function (never called)
def compute_legacy_metric(data):
    total = 0
    for x in data:
        total += x ** 2
    return total / len(data) if data else 0

# Unused transformation matrix
TRANSFORMATION_MATRIX = [
    [1, 0, 0],
    [0, 0.707, 0.707],
    [0, -0.707, 0.707]
]

# Simulated sensor drift compensation (dead code path)
sensor_drift_log = []
for tick in range(5):
    drift_value = CALIBRATION_OFFSET * math.sin(tick * 0.5)
    sensor_drift_log.append(round(drift_value, 4))

# Real-time monitoring buffer (partially relevant)
monitor_buffer = []
for i, state in enumerate(qubit_states):
    adjusted_phase = phase_shifts[i] + (state * 0.1)
    if abs(adjusted_phase) > 0.5:
        monitor_buffer.append(state ^ 1)  # Flip if high phase
    else:
        monitor_buffer.append(state)

# Decoy statistical summary (looks important but unused)
mean_qubit = sum(qubit_states) / len(qubit_states)
median_phase = sorted(phase_shifts)[len(phase_shifts)//2]
max_deviation = max(abs(p) for p in phase_shifts)

# Hidden control flag computed via list comprehension (critical!)
control_sequence = [i for i, x in enumerate(qubit_states) if x == 1]
activation_threshold = sum([i*i for i in control_sequence]) // 2  # Key intermediate

# Bitmask synthesis from phase characteristics
bitmask = 0
for i, p in enumerate(phase_shifts):
    if p > 0.5 or p < -0.3:
        bitmask |= (1 << (i % 6))

# Secondary derived state (red herring)
derived_state_vector = []
for i in range(4):
    val = (bitmask >> i) & 1
    derived_state_vector.append(val)

# Core analysis function with nested logic and distractors
def analyze_system_state(registers):
    # Local irrelevant scaling factor
    scaling_factor = REFERENCE_VOLTAGE / (1 + TEMP_CORRECTION_FACTOR)
    
    # Primary accumulator (this will determine output)
    accumulator = 0
    
    # Simulated error correction cycle (contains distraction)
    correction_log = []
    for idx, bit in enumerate(registers):
        if idx % 2 == 0:
            accumulator += bit * (idx + 1)
        else:
            # This block looks complex but contributes minimally
            temp_val = (bit + phase_shifts[idx % len(phase_shifts)])
            if temp_val > 0.5:
                correction_log.append(1)
            else:
                correction_log.append(0)
    
    # Critical secondary adjustment using dictionary lookup
    weight_map = {0: 3, 1: -1, 2: 2, 3: 0, 4: -2, 5: 1}
    for pos, bit in enumerate(registers):
        if bit == 1:
            accumulator += weight_map.get(pos, 0) * pos
    
    # Tertiary influence: interaction with activation threshold
    global activation_threshold
    if accumulator > activation_threshold:
        accumulator -= int(math.sqrt(activation_threshold))
    else:
        accumulator += int(math.log(activation_threshold + 1))
    
    # Final nonlinear transformation (deterministic)
    accumulator = abs(accumulator) ^ 7
    accumulator = (accumulator * 3) % 1000
    
    # Dead code: elaborate but unreachable
    if accumulator < 0:  # Never true due to abs()
        accumulator = -accumulator * 2
    
    return accumulator

# Execution point of interest
final_diagnostic = analyze_system_state(qubit_states)

# Irrelevant visualization prep
plot_compatibility = []
for i in range(8):
    plot_compatibility.append((i, (final_diagnostic + i) % 7))

# Another decoy structure
status_summary = {
    'readiness': 'nominal',
    'channels_active': len(qubit_states),
    'final_diagnostic_backup': final_diagnostic + 100  # Incorrect offset
}

# ACTUAL OUTPUT (required format)
print(f"Target result: {final_diagnostic}")