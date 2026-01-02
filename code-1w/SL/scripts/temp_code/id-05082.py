import math

# Simulated quantum register analysis system with decoy computations

def generate_entropy_sequence(length):
    # Distractor: generates unused entropy values
    return [len(str(math.factorial(i))) % 7 for i in range(2, length + 2)]

def compute_decoherence_factor(registers):
    # Irrelevant computation - never used in final result
    total = 0
    for r in registers:
        if r % 3 == 0:
            total += math.log(r + 1) * 0.1
    return round(total, 3)

def evaluate_superposition_stability(config):
    # Dead-end function: looks important but unused
    stability_score = 0
    for i, val in enumerate(config):
        stability_score += (val ** (i % 4 + 1)) % 97
    return stability_score // len(config)

def filter_active_qubits(registers):
    # Relevant preprocessing: extracts qubits above threshold
    threshold = sum(registers) / len(registers)
    return [q for q in registers if q > threshold]

def transform_register_state(qubits):
    # Key transformation using list comprehension and lambda
    shift_op = lambda x: (x << 2) ^ 0b101
    shifted = [shift_op(q & 0b111) for q in qubits]
    return list(map(lambda x: x - (x >> 3), shifted))

def calculate_coherence_vector(states):
    # Mid-level processing with dictionary operations
    stats = {
        'sum': sum(states),
        'max': max(states),
        'min': min(states),
        'range': 0
    }
    stats['range'] = stats['max'] - stats['min']
    
    # Real computation path
    raw_product = 1
    for s in states:
        if s != 0:
            raw_product *= abs(s)
            if raw_product > 10000:
                raw_product //= 10
    
    return {
        'product': raw_product,
        'adjusted_mean': (stats['sum'] + stats['range']) / (len(states) + 1)
    }

def analyze_system_state(registers):
    # Main analysis pipeline with nesting and filtering
    
    # Step 1: Filter active qubits (relevant)
    active_qubits = filter_active_qubits(registers)
    
    # Step 2: Transform state (critical path)
    processed_states = transform_register_state(active_qubits)
    
    # Step 3: Compute coherence metrics (partially relevant)
    coherence_data = calculate_coherence_vector(processed_states)
    
    # Step 4: Apply corrective weighting (key step)
    weight_factor = 0.75 if len(processed_states) > 3 else 1.25
    weighted_score = coherence_data['adjusted_mean'] * weight_factor
    
    # Step 5: Final integration with red herring variables
    baseline_offset = 42  # Misleading constant
    decoy_entropy = generate_entropy_sequence(6)  # Unused call
    hypothetical_limit = math.gamma(6) * 2.5  # Distractor calculation
    
    # Critical logic chain continuation
    temp_result = int(weighted_score * 100)
    checksum = 0
    for digit in str(temp_result):
        checksum += int(digit) ** 2
    
    # Final computation
    final_modifier = (checksum % 7) + 1
    return int((temp_result / final_modifier) - 13)

# Primary quantum register input (system state)
quantum_registers = [12, 7, 19, 4, 15, 8, 21]

# Execute decoy functions to increase interference
_ = compute_decoherence_factor(quantum_registers)
_ = evaluate_superposition_stability(quantum_registers)
entropy_profile = generate_entropy_sequence(len(quantum_registers))

# Critical execution point
final_diagnostic = analyze_system_state(quantum_registers)

# Output target result
print(f"Result: {final_diagnostic}")