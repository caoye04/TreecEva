from collections import defaultdict
import math

# Simulate quantum flux stabilization in a lattice network
def compute_lattice_signature(n):
    signature = []
    for i in range(n):
        if i % 3 == 0:
            signature.append((i ** 2) % 7)
        else:
            signature.append(int(math.sqrt(i + 1)) % 7)
    return signature

def generate_transfer_matrix(dim, shift):
    matrix = defaultdict(lambda: defaultdict(float))
    temp_cache = {}
    
    for i in range(dim):
        for j in range(dim):
            base_val = (i * dim + j + 1)
            shifted = base_val * (math.sin(shift * i) + 1.5)
            matrix[i][j] = round(shifted, 3)
            
            # Distractor: caching intermediate values not fully used
            temp_cache[(i,j)] = base_val ** 0.5
    
    # Dead computation: modifies cache but doesn't affect output
    for k in temp_cache:
        temp_cache[k] = temp_cache[k] * 0.1 if k[0] % 2 == 0 else temp_cache[k]
        
    return matrix

def evaluate_coherence(flow):
    # Determines quantum coherence level based on flow variance
    mean = sum(flow) / len(flow)
    variance = sum((x - mean) ** 2 for x in flow) / len(flow)
    return variance < 0.8

def calculate_stable_flow(matrix, phase_angle):
    raw_flow = []
    adjustment_factor = math.cos(phase_angle) + 2.0
    
    for i in range(5):
        cell_sum = 0
        for j in range(5):
            cell_sum += matrix[i][j]
        # Relevant transformation
        adjusted = cell_sum * adjustment_factor
        raw_flow.append(round(adjusted, 3))
    
    # Misleading filtering: appears important but only slight effect
    filtered = [x for x in raw_flow if x > 15.0]
    if len(filtered) == 0:
        filtered = [raw_flow[0]]
    
    # Key logic step: final flux depends on sum and correction
    total_energy = sum(filtered)
    correction = len(raw_flow) - len(filtered)
    final = total_energy - (correction * 0.25)
    
    # Red herring computation (no impact)
    imaginary_component = 0
    for val in raw_flow:
        imaginary_component += (val * 0.01j).imag  # Always zero
    
    return round(final, 3)

# Main execution
lattice_dim = 5
phase_shift = 1.2

# Irrelevant setup - distractor variables
lattice_sig = compute_lattice_signature(lattice_dim)
diagnostic_log = set(lattice_sig)
error_flags = {x for x in lattice_sig if x > 5}

# Actual relevant data generation
transfer_matrix = generate_transfer_matrix(lattice_dim, phase_shift)

# Critical statement
final_flux = calculate_stable_flow(transfer_matrix, phase_shift)

print(f"Result: {final_flux}")