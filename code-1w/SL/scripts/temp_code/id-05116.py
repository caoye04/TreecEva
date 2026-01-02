def compute_redundancy_factor(states):
    return sum([s % 3 for s in states if s > 0])

# Irrelevant helper function (dead code path)
def encrypt_state_vector(vector):
    return [v ^ 255 for v in vector]

# Another decoy function with misleading intermediate output
def validate_coherence(state, threshold=0.7):
    coherence_score = sum(state) / len(state) if state else 0
    print(f'Debug: Coherence score={coherence_score:.4f}')  # Distracting output
    return coherence_score > threshold

# Main system simulation with red herrings
def simulate_quantum_decay(register, cycles):
    temp_register = register.copy()
    decay_mask = 255
    history = []
    
    for i in range(cycles):
        if i % 4 == 0:
            temp_register = [(r ^ decay_mask) for r in temp_register]
        elif i % 3 == 0:
            temp_register = [(r + 17) % 256 for r in temp_register]
        
        # Meaningless accumulation (distractor)
        snapshot = {
            'cycle': i,
            'entropy': sum([b & 3 for b in temp_register]),
            'checksum': sum(temp_register) % 1000
        }
        history.append(snapshot)
    
    return temp_register

# Core analysis logic buried among noise
def extract_syndrome_pattern(reg):
    pattern = 0
    for i, val in enumerate(reg):
        if val & (1 << (i % 8)):
            pattern += (val & 15) * (i + 1)
    return pattern % 97

# Unused but plausible-sounding function
def calibrate_phase_shifters(reg):
    adjusted = []
    for x in reg:
        adjusted.append((x >> 2) | (x << 6))
    return adjusted

# Critical diagnostic function — key to answer
# This gets called at the end
def analyze_system_state(register, syndrome):
    base_metric = 0
    
    # Real computation interlaced with irrelevant steps
    for idx, value in enumerate(register):
        if idx % 2 == 0:
            base_metric += (value ^ syndrome) % 19
        else:
            base_metric -= (value + syndrome) % 7
    
    # Actual core calculation
    adjustment_map = {i: (i*i) % 13 for i in range(15)}
    for k in adjustment_map:
        if k % 3 == 0:
            base_metric += adjustment_map[k]

    # Final transformation using dictionary lookup and modular arithmetic
    lookup_table = {i: ((i*5 + 3) % 97) for i in range(97)}
    final_adjustment = lookup_table[syndrome] // 3
    
    # Key result computed here
    result = (base_metric * 2) - final_adjustment
    
    # Several decoy variables and computations
    debug_info = {
        'temporal_drift': 0.0034,
        'parity_violations': 7,
        'ghost_metric': (result ^ 12345) % 10000
    }
    
    # Only this matters
    return abs(result)

# Irrelevant initialization block (misleading setup)
initialization_keys = [0x1F, 0x0A, 0x0B, 0x0C]
key_schedule = {}
for k in initialization_keys:
    key_schedule[k] = [(k ^ i) % 256 for i in range(4)]

# Simulate hardware register states (real input data)
quantum_register = [128, 64, 32, 16, 8, 4, 2, 1]
error_syndrome = extract_syndrome_pattern(simulate_quantum_decay(quantum_register, 12))

# Apply real transformation on real data
processed_register = simulate_quantum_decay(quantum_register, 5)

# Red herring: this looks important but isn't used
redundancy_factor = compute_redundancy_factor(processed_register)
print(f'System redundancy factor: {redundancy_factor}')

# Critical execution point — answer depends on this call
defensive_offset = 0
for i in range(3):
    defensive_offset += (redundancy_factor * i) % 5

# Final diagnostic determination (where answer is produced)
final_diagnostic = analyze_system_state(quantum_register, error_syndrome)

# Print result as required
print(f'Result: {final_diagnostic}')