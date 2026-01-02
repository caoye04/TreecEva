def preprocess_signal(data):
    processed = []
    for x in data:
        if x % 3 == 0:
            processed.append(x * 2)
        elif x % 5 == 0:
            processed.append(x + 7)
    return processed

# Irrelevant signal processing chain (red herring)
signal_chain = [12, 15, 9, 25, 18]
filtered_data = [x for x in signal_chain if x > 10]
baseline_correction = sum(filtered_data) // len(filtered_data)
detrended = [x - baseline_correction for x in filtered_data]
noise_floor = max(detrended) - min(detrended)

# Core quantum sequence with meaningful pattern
quantum_sequence = [1, 2, 4, 8, 16, 32, 64]

# Distractor: fake quantum harmonics
temporal_phase = [q ** 0.5 for q in quantum_sequence if q % 4 == 0]
amplitude_envelope = sum(temporal_phase[:3])

# System flags with embedded logic
flag_weights = {'F_SIGMA': 2, 'Q_REF': -1, 'T_MODE': 3}
system_flags = {
    'F_SIGMA': True,
    'Q_REF': False,
    'T_MODE': True,
    'OVERRIDE': False,
    'SAFETY_LOCK': True
}

# Misleading diagnostic path (dead code - never used)
class DiagnosticNode:
    def __init__(self, value):
        self.value = value
    def validate(self):
        return self.value > 0

node_pool = [DiagnosticNode(i * 3) for i in range(5)]
consensus_score = sum(1 for n in node_pool if n.validate())

# Real computation begins here
def evaluate_coherence(seq):
    total = 0
    for i, val in enumerate(seq):
        if i % 2 == 0:
            total += val & (i + 1)  # Bitwise with index
        else:
            total -= val ^ (i * 2)
    return total

# Secondary evaluation with conditional expression
def compute_stability(flags):
    base = flag_weights['F_SIGMA'] if flags['F_SIGMA'] else -2
    bonus = 5 if flags['T_MODE'] and not flags['OVERRIDE'] else 0
    penalty = 10 if not flags['Q_REF'] else 0
    return base + bonus - penalty

# Main analysis function combining multiple concepts
def analyze_system_state(sequence, flags):
    coherence = evaluate_coherence(sequence)
    stability = compute_stability(flags)
    
    # Complex conditional expression with distractor variables
    adjustment_factor = 2.5 if noise_floor > 5 else 1.1  # Uses earlier red herring
    temporal_weight = amplitude_envelope / 10 if temporal_phase else 0  # More red herrings
    
    # Actual key calculation (non-obvious due to distractions)
    raw_diagnostic = coherence * stability
    
    # Final adjustment using irrelevant preprocessed signal
    offset = len(preprocess_signal([3, 5, 6, 10]))  # Calls red herring function
    final_diagnostic = raw_diagnostic + offset
    
    # Dead code branch (never executes due to constant)
    if False:
        fallback = 0
        for node in node_pool:
            fallback += node.value
        final_diagnostic = fallback
    
    return final_diagnostic

# Execute main logic
coherence_value = evaluate_coherence(quantum_sequence)
stability_index = compute_stability(system_flags)
final_diagnostic = analyze_system_state(quantum_sequence, system_flags)

# Print result as required
print(f"Target result: {final_diagnostic}")