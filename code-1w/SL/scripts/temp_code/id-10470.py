def preprocess_signal(data, threshold=0.5):
    filtered = [x for x in data if abs(x) > threshold]
    normalized = [x / max(filtered) for x in filtered]
    return normalized

# Irrelevant sensor array (distractor)
sensor_readings = [0.1, 0.4, 0.8, 1.2, 0.9, 0.3, 0.6]
processed_data = preprocess_signal(sensor_readings)

# Quantum register simulation with bit manipulation
class QuantumRegister:
    def __init__(self, bits):
        self.bits = bits
        self.state = (1 << bits) - 1

    def apply_hadamard(self):
        # Simulate superposition: toggle every other bit
        for i in range(0, self.bits, 2):
            self.state ^= (1 << i)

    def entangle(self, other):
        # XOR state with another register (simplified entanglement)
        self.state ^= other.state

# Misleading decoy function (never used)
def compute_entropy(sequence):
    from math import log
    freq = {}
    for item in sequence:
        freq[item] = freq.get(item, 0) + 1
    entropy = 0.0
    total = len(sequence)
    for count in freq.values():
        p = count / total
        entropy -= p * log(p, 2)
    return entropy

# Actual quantum system setup
qreg_a = QuantumRegister(5)
qreg_b = QuantumRegister(4)
qreg_a.apply_hadamard()  # Alters state

# Red herring: unused transformation chain
buffer_stream = ['a', 'b', 'c']
token_map = {k: idx for idx, k in enumerate(buffer_stream)}
encoded = ''.join([str(token_map[x]) for x in buffer_stream if x != 'b'])
sliced_part = encoded[1:]  # Distractor slice

# Entanglement alters both registers
qreg_b.apply_hadamard()
qreg_a.entangle(qreg_b)

# Data structure mixing: dictionary and slicing
register_snapshot = {
    'a_state': qreg_a.state,
    'b_state': qreg_b.state,
    'timestamp': 1699999999,
    'history': [qreg_a.state, 0, qreg_b.state]
}

# Linear search in decoy list (dead path)
search_space = list(range(100, 200, 7))
found_index = -1
for i, val in enumerate(search_space):
    if val == 150:
        found_index = i

# Core analysis logic (uses dictionary and slicing)
def analyze_system_state(registers):
    # Combine both registers using XOR and bit counting
    combined_state = registers.state ^ ((1 << 3) - 1)
    
    # Slicing a virtual history (simulated)
    history_proxy = [0, 0, registers.state, 404, 505]
    recent = history_proxy[-3:]  # Use last three
    
    # Compute diagnostic metric
    bit_count = bin(combined_state).count('1')
    position_factor = len(recent) * 17
    
    # Dummy dictionary operations (distraction)
    stats = {
        'bits': bit_count,
        'factor': position_factor,
        'meta': {'level': 2, 'active': True}
    }
    
    # Actual computation path
    base_score = stats['bits'] * stats['factor']
    adjustment = (combined_state >> 2) & 15  # Bitwise extract
    final_value = base_score - adjustment
    
    return final_value

# Critical execution point
final_diagnostic = analyze_system_state(qreg_a)
print(f"Target result: {final_diagnostic}")