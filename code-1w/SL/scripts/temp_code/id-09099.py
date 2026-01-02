import math

# Simulated quantum register diagnostics (irrelevant initial setup)
def initialize_calibration():
    return [0.1 * i for i in range(10)]

def deprecated_signal_filter(data):
    # Outdated filtering method - never called
    return [x for x in data if x > 0.5]

# Irrelevant constants for electromagnetic interference modeling
EMI_TOLERANCE = 0.78
MAX_PHASE_SHIFT = 45.0
REFERENCE_VOLTAGE = 3.3

class SignalProcessor:
    def __init__(self, gain):
        self.gain = gain
        self.history = []

    def process(self, x):
        return x * self.gain

# Unused signal processor instance (distractor)
processor = SignalProcessor(2.5)

# Core system state variables
quantum_registers = [
    {'state': 1, 'coherence': 0.92, 'error_flag': False},
    {'state': 0, 'coherence': 0.45, 'error_flag': True},
    {'state': 1, 'coherence': 0.88, 'error_flag': False},
    {'state': 1, 'coherence': 0.91, 'error_flag': False}
]

# Auxiliary diagnostic vectors (some irrelevant)
diag_vector_a = [1, 0, 1, 1]
diag_vector_b = [0.92, 0.45, 0.88, 0.91]  # coherence values duplicate (red herring)
diag_vector_c = [False, True, False, False]  # error flags duplicate (misleading)

# Legacy checksum calculation (dead code path)
def compute_legacy_checksum(regs):
    return sum(r['state'] for r in regs) % 7

# Misleading intermediate computation (not used in final result)
temporal_weight = 0
for reg in quantum_registers:
    if reg['coherence'] < 0.5:
        temporal_weight += 0.1
    else:
        temporal_weight += 0.05

temporal_weight = round(temporal_weight, 3)  # Result: 0.15 (distractor)

# Complex lambda for dynamic thresholding (actually used)
adaptive_threshold = lambda x: 0.85 if x['state'] == 1 else 0.4

# Secondary evaluation function (looks important but unused)
def evaluate_stability(regs):
    stable_count = 0
    for r in regs:
        if not r['error_flag'] and r['coherence'] > 0.8:
            stable_count += 1
    return stable_count / len(regs)

# Another decoy function with bit manipulation (never invoked)
def encode_register_state(regs):
    encoded = 0
    for i, r in enumerate(regs):
        bit = (r['state'] << i) & 1
        encoded |= bit
    return encoded

# Global counter for side effects (appears to matter, doesn't)
system_wide_counter = 0

# Main analysis function with nested logic and distractors
def analyze_system_state(registers):
    global system_wide_counter
    diagnostic_score = 0.0
    valid_states = 0
    decay_penalty = 0.0

    # First pass: filter by error flag (critical)
    active_registers = [r for r in registers if not r['error_flag']]

    # Second pass: evaluate coherence against adaptive threshold
    for reg in active_registers:
        system_wide_counter += 1  # Incremented but not used
        threshold = adaptive_threshold(reg)
        
        # Significant branch: coherence above threshold adds score
        if reg['coherence'] >= threshold:
            diagnostic_score += reg['state'] * reg['coherence']
            valid_states += 1
        else:
            # Apply decay penalty based on difference
            diff = threshold - reg['coherence']
            decay_penalty += diff * 0.5
    
    # Compute base integrity (looks important, partially used)
    integrity_ratio = valid_states / len(registers) if registers else 0
    
    # Third component: entropy calculation from state distribution
    states = [r['state'] for r in active_registers]
    if states:
        p_one = sum(states) / len(states)
        p_zero = 1 - p_one
        entropy = 0.0
        if p_one > 0:
            entropy -= p_one * math.log(p_one)
        if p_zero > 0:
            entropy -= p_zero * math.log(p_zero)
    else:
        entropy = 0.0
    
    # Final diagnostic combines three factors
    # Only diagnostic_score and decay_penalty are actually used
    final_component = diagnostic_score - decay_penalty + (entropy * 0.1)  # entropy contribution minimal
    
    # Additional red herring: modify global that isn't used
    system_wide_counter = int(diagnostic_score * 10)
    
    return final_component

# Execution point of interest
final_diagnostic = analyze_system_state(quantum_registers)

# Print target result
print(f"Result: {final_diagnostic}")