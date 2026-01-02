def preprocess_signal(data, threshold=0.5):
    filtered = [x for x in data if abs(x) > threshold]
    normalized = [x / max(filtered) for x in filtered]
    return normalized

# Irrelevant sensor array (red herring)
sensor_readings = [0.1, 0.4, 0.8, 1.2, -0.3, -0.7, 0.9]
processed_noise = preprocess_signal(sensor_readings, 0.35)

# Quantum register simulation with bit manipulation
class QuantumRegister:
    def __init__(self, size):
        self.size = size
        self.state = (1 << size) - 1  # All bits set

    def apply_hadamard(self):
        # Simulate superposition: toggle every other bit
        for i in range(self.size):
            if i % 2 == 1:
                self.state ^= (1 << i)

    def measure(self):
        # Collapse to classical state via XOR folding
        val = self.state
        while val >> 8:
            val ^= (val >> 8)
        return val & 255  # Return 8-bit result

# Initialize quantum registers
qr_a = QuantumRegister(6)
qr_b = QuantumRegister(5)
qr_c = QuantumRegister(7)

# Apply operations (some irrelevant)
qr_a.apply_hadamard()
qr_b.apply_hadamard()  # This one isn't used later (distractor)
qr_c.apply_hadamard()

# Extract measured states
measured_states = {
    'reg_a': qr_a.measure(),
    'reg_b': qr_b.measure(),  # Included but not used
    'reg_c': qr_c.measure()
}

# Decoy function (never called)
def decrypt_entropy(signal):
    acc = 0
    for i in range(len(signal)):
        acc += signal[i] * (i + 1)
    return acc % 100

# Real computation begins here
bit_flags = {
    'flag_alpha': 0b1010,
    'flag_beta': 0b1100,
    'flag_gamma': 0b1111
}

# Flag manipulation with masking
temp_mask = (bit_flags['flag_alpha'] ^ bit_flags['flag_beta']) & 0b1110
bit_flags['flag_delta'] = temp_mask | 0b0001

# Set of active qubits based on measurement
active_qubits = set()
for reg_name, value in measured_states.items():
    if 'a' in reg_name or 'c' in reg_name:  # Skip reg_b
        for bit_pos in range(8):
            if (value >> bit_pos) & 1:
                active_qubits.add((reg_name, bit_pos))

# Counting and grouping logic
qubit_groups = {}
for reg_bit_pair in active_qubits:
    reg_name = reg_bit_pair[0]
    if reg_name not in qubit_groups:
        qubit_groups[reg_name] = 0
    qubit_groups[reg_name] += 1

# Add decoy group count (unused)
decoy_group = {}
for i in range(3):
    decoy_group[f'aux_{i}'] = i * 10 + 5

# Core diagnostic calculation
def compute_coherence_score(groups, base_factor=3.7):
    total = 0
    for name, count in groups.items():
        if 'a' in name:
            total += count * base_factor
        elif 'c' in name:
            total += count * (base_factor * 0.7)
    return round(total, 4)

coherence = compute_coherence_score(qubit_groups)

# System state analyzer (main path)
def analyze_system_state(registers):
    # Dummy dictionary for metadata
    diagnostics = {
        'version': '2.1.0',
        'calibration': [0.1, 0.2, 0.3],
        'status': 'nominal'
    }
    
    # Actual computation
    reg_a_state = registers[0].state
    reg_c_state = registers[2].state
    
    combined_entropy = (reg_a_state ^ reg_c_state) & 0xFFFF
    
    # Modular arithmetic chain
    step1 = (combined_entropy * 7) % 199
    step2 = (step1 + 13) % 107
    step3 = (step2 * step2) % 89
    step4 = (step3 - 5) % 73
    
    # Bit counting
    popcount = bin(combined_entropy).count('1')
    
    # Final formula
    result = (step4 * popcount) - (coherence * 10)
    
    # Distractor assignment (looks important but unused)
    diagnostics['intermediate'] = step3 * 2
    diagnostics['valid'] = True
    diagnostics['final_value'] = result + 1000  # Misleading!
    
    return int(result)

# Execute main analysis
quantum_registers = [qr_a, qr_b, qr_c]
final_diagnostic = analyze_system_state(quantum_registers)

print(f"Target result: {final_diagnostic}")