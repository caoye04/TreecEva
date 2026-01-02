def preprocess_signal(data, threshold=0.75):
    filtered = [x for x in data if abs(x) > threshold]
    normalized = [round(x / max(filtered), 3) for x in filtered] if filtered else [0]
    return normalized


def evaluate_coherence(sequence):
    score = 0
    for i, val in enumerate(sequence):
        if i > 0 and sequence[i-1] * val < 0:
            score += 1.5
        if val == 0:
            score -= 1
    return score


def transform_register(reg):
    temp_result = 0
    for i in range(len(reg)):
        temp_result ^= int(reg[i] * (i + 1))  
    return temp_result % 17


def generate_checksum(structure):
    total = 0
    for idx, item in enumerate(structure):
        if idx % 2 == 0:
            total += sum([item.count(x) for x in set(item) if x > 2])
        else:
            total -= len(item)
    return total


def decode_entanglement(pair_list):
    result = []
    for a, b in pair_list:
        result.append((a ^ b) + (a & b))
    return result


def analyze_system_state(registers):
    # Irrelevant preprocessing (distraction)
    signal_data = [sum(reg) / len(reg) for reg in registers]
    processed_signal = preprocess_signal(signal_data)
    
    # Misleading coherence evaluation (red herring)
    decoy_score = evaluate_coherence(signal_data)
    adjustment_factor = 0.0
    if decoy_score > 2:
        adjustment_factor = 1.2
    else:
        adjustment_factor = 0.8
    
    # Core logic: bit manipulation on register patterns
    transformed_values = [transform_register(reg) for reg in registers]
    
    # Distractor: unused complex structure
    aux_structures = [[i*2 + j for j in range(4)] for i in range(len(registers))]
    checksum = generate_checksum(aux_structures)  # Unused later
    
    # Another distraction: entanglement decoding with no impact
    paired = list(zip(registers[::2], registers[1::2]))
    if len(paired) > 0:
        _ = decode_entanglement([(sum(a), sum(b)) for a, b in paired])
    
    # Actual computation path (non-obvious due to noise)
    base_accumulator = 0
    for idx, tv in enumerate(transformed_values):
        if idx % 2 == 0:
            base_accumulator += tv * (idx + 1)
        else:
            base_accumulator -= tv
    
    # Final adjustment using enumerate and zip (required features)
    offsets = [1, -1, 2, -2]
    for i, (val, offset) in enumerate(zip(transformed_values, offsets)):
        if i < len(offsets):
            base_accumulator += (val % 5) * offset
    
    final_diagnostic = abs(base_accumulator) * 3
    return final_diagnostic

# Simulated quantum register states (input data)
quantum_registers = [
    [1.2, 0.8, 3.1, 0.9],
    [2.5, 1.3, 0.7, 4.4],
    [0.6, 2.9, 1.1, 3.3],
    [4.0, 0.5, 2.2, 1.8]
]

# Execute main analysis
diagnostic_value = analyze_system_state(quantum_registers)
print(f"Result: {diagnostic_value}")