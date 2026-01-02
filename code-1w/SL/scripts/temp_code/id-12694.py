import itertools

# Simulated sensor data preprocessing with red herrings
def preprocess_signals(raw_streams, filter_mode='legacy'):
    if filter_mode == 'legacy':
        legacy_offset = sum([i * 0.01 for i in range(len(raw_streams))])
        adjusted = [x + legacy_offset for x in raw_streams]
    else:
        adjusted = [x * 1.1 for x in raw_streams]

    # Irrelevant normalization branch (never taken)
    if False:
        max_val = max(adjusted)
        adjusted = [x / max_val for x in adjusted]

    return adjusted

# Misleading auxiliary function that looks important but is unused
def compute_entropy(sequence):
    from math import log
    freq = {}
    for item in sequence:
        freq[item] = freq.get(item, 0) + 1
    entropy = 0
    total = len(sequence)
    for count in freq.values():
        p = count / total
        entropy -= p * log(p, 2)
    return entropy

# Core transformation with slicing and combinatorics
def generate_phase_shifts(data_window):
    shifted_variants = []
    n = len(data_window)
    for i in range(n):
        shifted_variants.append(data_window[i:] + data_window[:i])  # Rotation via slicing
    return shifted_variants

# Secondary transformation with decoy operations
def apply_harmonic_map(signal, depth=3):
    result = signal.copy()
    temp_accum = 0
    
    for _ in range(depth):
        temp_accum += sum([x % 7 for x in result if x > 30])  # Dead-end accumulation
        result = [int(x // 2) if x > 50 else int(x * 1.5) for x in result]
    
    # This modification is irrelevant but looks like processing
    scaling_factor = 1.05
    final_scaled = [x * scaling_factor for x in result]
    
    return final_scaled  # Used later, but only a part of the chain

# Key analysis function combining multiple concepts
def analyze_pattern(grid_sequence, threshold):
    counter = 0
    pattern_signature = 0
    
    for idx, seq in enumerate(grid_sequence):
        # Use of itertools to create pairwise combinations (real logic)
        pairs = list(itertools.combinations(seq[:4], 2))
        for a, b in pairs:
            if (a ^ b) & 1:  # Bitwise XOR and AND check (odd parity)
                counter += 1
        
        # Real contribution: modular arithmetic on index
        if idx % 3 == 0:
            pattern_signature += sum(seq) % 11
    
    # Final computation - only this matters
    diagnostic_score = (counter * 17) + pattern_signature
    
    # Distractor: complex-looking but unused expression
    if diagnostic_score > threshold:
        adjustment = pow(diagnostic_score, 2, 1009)
        diagnostic_score = (diagnostic_score + adjustment) % 5000
    
    return diagnostic_score

# --- Main execution with layered distractions ---

def main():
    # Initial dataset (simulated measurement readings)
    base_readings = [12, 15, 23, 34, 45, 51]
    
    # Apply preprocessing (relevant)
    processed = preprocess_signals(base_readings, filter_mode='legacy')
    
    # Unused entropy calculation (red herring)
    _ = compute_entropy(processed)
    
    # Extract window using slicing (relevant step)
    focus_window = processed[1:5]
    
    # Generate phase shifts (used later)
    phase_grids = generate_phase_shifts(focus_window)
    
    # Apply harmonic map - output partially used
    transformed_grid = []
    for grid in phase_grids:
        mapped = apply_harmonic_map(grid, depth=2)
        transformed_grid.append(mapped[:len(grid)])  # Truncate and store
    
    # Decoy loop with no effect (dead code path)
    temp_result = 0
    for i in range(5):
        temp_result += i ** 3
    temp_result = temp_result % 0xFACE  # Looks cryptic, does nothing
    
    # Key threshold derived from bitwise manipulation (real)
    key_threshold = (len(transformed_grid[0]) << 3) ^ 42  # 4 << 3 = 32, 32 ^ 42 = 10
    
    # Final analysis (this produces the answer)
    final_diagnostic = analyze_pattern(transformed_grid, key_threshold)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")

    return final_diagnostic

# Execute and capture
result = main()