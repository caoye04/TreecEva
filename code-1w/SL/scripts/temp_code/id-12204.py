import itertools

def simulate_quantum_decay(registers):
    decayed = {}
    for k, v in registers.items():
        if len(k) % 2 == 0:
            decayed[k] = v * 0.95
        else:
            decayed[k] = v * 1.05
    return decayed

def compute_entropy(registers):
    total = sum(registers.values())
    entropy = 0
    for v in registers.values():
        if v > 0:
            p = v / total
            entropy -= p * __import__('math').log(p)
    return entropy

def validate_checksum(data_str):
    # Irrelevant validation function (dead code path)
    return sum(ord(c) for c in data_str) % 17 == 0

def generate_hamming_sequence(n):
    # Distractor: unused sequence generation
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])
    return seq

def extract_relevant_modes(registers):
    modes = []
    for key in registers.keys():
        if key.startswith('Q') and key.endswith('X'):
            modes.append(key[1:-1])
    return modes

def filter_noisy_channels(signal_dict, threshold=0.75):
    # Misleading intermediate result
    filtered = {k: v for k, v in signal_dict.items() if v > threshold}
    normalization_factor = sum(filtered.values()) if filtered else 1.0
    return {k: v / normalization_factor for k, v in filtered.items()}

def analyze_system_state(registers):
    # Main computation chain
    temp_state = simulate_quantum_decay(registers)
    
    # Extract mode information (used later)
    active_modes = extract_relevant_modes(temp_state)
    
    # Compute side metric (distractor)
    _ = compute_entropy(temp_state)
    
    # Simulate signal filtering (red herring with partial use)
    strong_signals = filter_noisy_channels(temp_state, threshold=0.65)
    
    # Key transformation: map modes to numeric contributions
    contribution = 0
    mode_index_map = {mode: idx for idx, mode in enumerate(active_modes)}
    
    for mode, idx in mode_index_map.items():
        if 'B' in mode:
            contribution += idx * 3
        elif 'C' in mode:
            contribution -= idx * 2
        else:
            contribution += idx
    
    # Incorporate signal magnitudes from strong_signals (only QBX)
    if 'QBX' in strong_signals:
        contribution *= int(strong_signals['QBX'] * 10)
    
    # Additional distraction: character counting in keys
    char_count = sum(len(k) for k in temp_state.keys() if k.isalpha())
    dummy_offset = char_count % 13
    
    # Final diagnostic calculation
    final_diagnostic = contribution + dummy_offset - 5
    
    # Dead code: early return never taken
    if False:
        return -999
        extra_work = ''.join(itertools.repeat('Z', 5))
        return len(extra_work)
    
    return final_diagnostic

# Initialization block
quantum_registers = {
    'QAX': 0.82,
    'QBX': 0.93,
    'QCX': 0.71,
    'QDX': 0.64,
    'QEEX': 1.05  # Even-length key for decay logic
}

# Unused variable (distractor)
baseline_config = {'version': '2.1', 'active': True}

# Unused string method chain (irrelevant)
config_trace = "INIT;LOAD;CALIBRATE".split(';')
config_trace.append('DONE')

# Execution point of interest
final_diagnostic = analyze_system_state(quantum_registers)
print(f"Result: {final_diagnostic}")