import math

# Simulated quantum register with entangled state weights
def initialize_quantum_register():
    return [0.1, 0.3, 0.4, 0.2]

# Irrelevant helper: Computes factorial (not used in main logic)
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Distraction function: Processes decoy data
def process_auxiliary_buffer(buffer):
    checksum = 0
    for val in buffer:
        checksum += val ** 2
    return checksum * 0.5

# Misleading transformation: Bit-flip simulation (unused)
def simulate_bit_flip(state):
    flipped = []
    for s in state:
        flipped.append(1 - s if s > 0.5 else s + 0.1)
    return flipped

# Real computation: Entropy of probability distribution
def shannon_entropy(distribution):
    entropy = 0.0
    for p in distribution:
        if p > 0:
            entropy -= p * math.log2(p)
    return entropy

# Complex data structure: Diagnostic map with red herrings
def create_diagnostics_map():
    return {
        'voltage_stability': 0.91,
        'clock_drift': 0.03,
        'entropy_baseline': 1.85,
        'temp_fluctuation': 0.12,
        'aux_data_integrity': 0.99
    }

# Unused recursive function to mislead control flow analysis
def validate_hierarchy(depth, acc):
    if depth == 0:
        return acc
    return validate_hierarchy(depth - 1, acc * 1.02)

# Core analysis function with distractor-heavy body
def analyze_system_state(register):
    # Step 1: Normalize register (redundant, already normalized)
    total = sum(register)
    normalized = [x / total for x in register]
    
    # Step 2: Compute entropy (critical path)
    entropy = shannon_entropy(normalized)
    
    # Step 3: Initialize diagnostics with irrelevant entries
    diagnostics = create_diagnostics_map()
    diagnostics['current_entropy'] = entropy
    diagnostics['register_size'] = len(normalized)
    
    # Step 4: Simulate false dependency on auxiliary buffer
    aux_buffer = [0.05, 0.15, 0.25, 0.35]
    fake_dependency = process_auxiliary_buffer(aux_buffer)
    diagnostics['fake_metric'] = fake_dependency
    
    # Step 5: Apply meaningless bit flip simulation
    dummy_flip = simulate_bit_flip(normalized)
    flip_divergence = sum(abs(a - b) for a, b in zip(normalized, dummy_flip))
    diagnostics['flip_divergence'] = flip_divergence
    
    # Step 6: Build tuple chain with unused values
    metadata_chain = (
        ('version', '2.1'),
        ('mode', 'diagnostic'),
        ('depth', 3),
        ('entropy', entropy)
    )
    
    # Step 7: Update with computed entropy (still not final)
    diagnostics['computed_diagnostic'] = entropy * 100
    
    # Step 8: Critical calculation — combinatoric adjustment factor
    n = len(register)
    adjustment_factor = math.comb(n + 2, n - 1)  # C(6,2) = 15
    
    # Step 9: Final diagnostic depends only on entropy and adjustment
    # All prior dictionary entries are distractions
    final_diagnostic = int((entropy * adjustment_factor) * 10)  # (1.846 * 15) * 10 ≈ 276.9 → 276
    
    # Dead code: Early return never reached
    if final_diagnostic < 0:
        return -1
        
    # Unused validation hierarchy
    confidence = validate_hierarchy(3, 1.0)
    diagnostics['confidence_score'] = confidence
    
    return final_diagnostic

# Main execution
quantum_register = initialize_quantum_register()
final_diagnostic = analyze_system_state(quantum_register)
print(f"Target result: {final_diagnostic}")