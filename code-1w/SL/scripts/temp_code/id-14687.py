import math

def simulate_quantum_decay(steps):
    decay_chain = []
    accumulator = 1.0
    for i in range(1, steps + 1):
        if i % 3 == 0:
            accumulator *= 0.9
        elif i % 5 == 0:
            accumulator += 0.05
        else:
            accumulator += 0.01
        decay_chain.append(round(accumulator, 4))
    return decay_chain


def calculate_entropy(sequence):
    # Irrelevant entropy calculation (red herring)
    total = sum(x * math.log2(x) for x in sequence if x > 0)
    return abs(total / len(sequence))


def validate_checksum(data_str):
    # Unused validation function (dead code path)
    checksum = 0
    for ch in data_str:
        checksum ^= ord(ch)
    return checksum == 255


def transform_register(registers):
    # Applies bit shifts and masking with decoy transformations
    transformed = {}
    for k, v in registers.items():
        temp_val = (v << 2) ^ 0xFF
        if temp_val > 100:
            temp_val = temp_val // 3
        transformed[f't_{k}'] = temp_val & 0xFFFF
    return transformed


def filter_outliers(data_list):
    # Linear search to remove extreme values (misleading preprocessing)
    mean_val = sum(data_list) / len(data_list)
    filtered = [x for x in data_list if abs(x - mean_val) < 0.5]
    return filtered if len(filtered) > 0 else data_list


def compute_coherence_factor(registers):
    # Coherence based on XOR patterns across register values
    values = list(registers.values())
    coherence = 0
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            coherence += (values[i] ^ values[j]) & 0xF
    return coherence


def extract_diagnostics(log_entries):
    # String parsing to extract numeric codes (distractor logic)
    codes = []
    for entry in log_entries:
        if 'ERROR' in entry:
            parts = entry.split(':')
            if len(parts) > 1:
                num_part = ''.join(filter(str.isdigit, parts[1]))
                if num_part:
                    codes.append(int(num_part) % 100)
    return codes


def analyze_system_state(registers):
    # Core logic buried among distractions
    temp_state = {k: v for k, v in registers.items()}
    
    # Step 1: Scale certain register values
    for key in temp_state:
        if 'q' in key:
            temp_state[key] *= 2
    
    # Step 2: Aggregate modified values
    aggregate = 0
    for val in temp_state.values():
        aggregate += val
    
    # Step 3: Apply conditional adjustment
    if aggregate > 300:
        aggregate -= 50
    else:
        aggregate += 25
    
    # Step 4: Use dictionary keys to modulate result
    key_score = 0
    for k in temp_state.keys():
        key_score += len(k) * (ord(k[0]) % 8)
    
    # Step 5: Final computation combining state and structure
    raw_diagnostic = (aggregate * 2) - key_score
    
    # Step 6: Clamp within expected system bounds
    final_diagnostic = max(100, min(raw_diagnostic, 999))
    
    # Irrelevant print for confusion
    debug_trace = f"Diag-{raw_diagnostic}-Norm"
    
    return final_diagnostic

# Main execution with heavy interference
if __name__ == '__main__':
    # Initialize quantum register states (meaningful input)
    quantum_registers = {
        'q_a': 42,
        'q_b': 88,
        'q_c': 67,
        'aux_1': 15,
        'meta_z': 9
    }

    # Generate decay simulation (irrelevant side process)
    decay_log = simulate_quantum_decay(50)
    
    # Filter simulated data (red herring operation)
    cleaned_decay = filter_outliers(decay_log)
    
    # Compute fake entropy (distraction metric)
    entropy_metric = calculate_entropy(cleaned_decay)
    
    # Transform registers through bit ops (decoy transformation)
    processed_registers = transform_register(quantum_registers)
    
    # Extract fake diagnostics from logs (unrelated string processing)
    system_logs = [
        'INIT: Start sequence 1024',
        'ERROR: Failure in module 5678',
        'DEBUG: Loop count 99',
        'ERROR: Memory fault 1357'
    ]
    diagnostic_codes = extract_diagnostics(system_logs)
    
    # Compute coherence (intermediate irrelevant value)
    coherence_index = compute_coherence_factor(quantum_registers)
    
    # Critical statement: this determines the actual answer
    final_diagnostic = analyze_system_state(quantum_registers)
    
    # Print only the target result
    print(f"Result: {final_diagnostic}")