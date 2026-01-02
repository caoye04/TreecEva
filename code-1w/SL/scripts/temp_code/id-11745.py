def preprocess_signal(raw_data, threshold=0.75):
    filtered = [x for x in raw_data if abs(x) > threshold]
    normalized = [round(x ** 2, 3) for x in filtered]
    return normalized if len(normalized) > 2 else [0.0]


def shift_phase(registers, n):
    return [(reg << 3) & 0xFF for reg in registers[-n:]]


def calculate_entropy(sequence):
    from math import log2
    freq_map = {}
    for item in sequence:
        freq_map[item] = freq_map.get(item, 0) + 1
    total = len(sequence)
    entropy = -sum((count / total) * log2(count / total) for count in freq_map.values())
    return round(entropy, 4)


def decode_instruction(opcode):
    # Misleading function – looks important but unused
    mapping = {0x3A: 'JMP', 0x1F: 'HLT', 0x2B: 'MOV'}
    return mapping.get(opcode, 'NOP')

# Simulated sensor inputs (irrelevant to final result)
sensor_readings = [-1.2, 0.3, 0.8, 1.5, -0.6, 2.1, 0.72, 1.05]
processed_signal = preprocess_signal(sensor_readings, threshold=0.75)

# Quantum register simulation (core component)
quantum_registers = [0b11010110, 0b10101010, 0b11110000, 0b00011111, 0b10111011]

# Red herring: signal phase shifting with no impact on final result
shifted_phases = shift_phase(quantum_registers, 3)

# Decoy data structures
system_logs = {
    'errors': [0x1F, 0x2B],
    'warnings': [0x3A],
    'debug': []
}

# Unused transformation path
if len(shifted_phases) > 2:
    temp_state = [p ^ 0xAA for p in shifted_phases]
    # This branch executes but doesn't affect final_diagnostic

# Core analysis logic
bit_frequencies = {}
for reg in quantum_registers:
    for i in range(8):
        bit = (reg >> i) & 1
        bit_frequencies[i] = bit_frequencies.get(i, 0) + bit

# Extract bit pattern at position 3 (key insight)
active_at_pos3 = sum(1 for reg in quantum_registers if (reg >> 3) & 1)

# Construct diagnostic vector using multiple concepts
diagnostic_vector = []
for i in range(8):
    if i % 3 == 0:
        diagnostic_vector.append(bit_frequencies[i] * 2)
    elif i == active_at_pos3 % 4:
        diagnostic_vector.append(bit_frequencies[i] + 3)
    else:
        diagnostic_vector.append(1)

# Secondary red herring: entropy calculation on decoy data
fake_sequence = [1, 1, 0, 1, 1, 0, 0, 0, 1]
entropy_diagnostic = calculate_entropy(fake_sequence)  # Used nowhere

# Tertiary distraction: dictionary-based state tracking
state_tracker = {
    'active_bits': sum(bit_frequencies.values()),
    'high_activity_positions': [k for k, v in bit_frequencies.items() if v > 3],
    'checksum': sum(bit_frequencies.values()) ^ 0xFF
}

# Actual final computation (hidden among distractions)
def analyze_system_state(regs):
    cumulative = 0
    for idx, reg in enumerate(regs):
        # Focus on specific bits and modular arithmetic
        extracted = ((reg >> 2) & 0x0F)  # 4-bit slice starting at pos 2
        if extracted % 3 == 0:
            cumulative += extracted * idx
        else:
            cumulative -= (extracted ^ idx) % 5
    # Final transformation involving list comprehension and slicing
    history = [cumulative // (i+1) for i in range(1, 5)]
    return abs(history[1] - history[3]) * 2  # Critical computation

final_diagnostic = analyze_system_state(quantum_registers)
print(f"Target result: {final_diagnostic}")