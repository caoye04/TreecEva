from itertools import cycle, islice

def generate_phase_shift(n):
    return (n ^ (n >> 3)) & 0xFF

def evaluate_entropy(stream):
    # Irrelevant entropy calculation (dead logic)
    total = 0
    for s in stream:
        total += (s ** 2) % 17
    return total // len(stream) if stream else 0

def simulate_harmonic(nodes):
    # Distractor function: looks important but unused
    result = []
    for i in range(len(nodes)):
        val = (nodes[i] + nodes[(i+1)%len(nodes)]) * (i+1)
        result.append(val % 128)
    return result

def filter_resonance(sequence):
    # Applies bit filtering; partially relevant
    filtered = []
    for x in sequence:
        if (x & 5) == 1:  # Bitmask red herring
            filtered.append(x & 15)
        elif (x & 3) == 2:
            filtered.append(x ^ 7)
        else:
            filtered.append(x >> 2)  # Key transformation path
    return filtered

def compute_invariant(trail):
    # Computes modular invariant used later
    accum = 0
    for idx, val in enumerate(trail):
        accum = (accum + (idx + 1) * val) % 987
    return accum

def derive_chaos_factor(seed_seq):
    # Misleading name; actually generates base signal
    transformed = []
    for item in seed_seq:
        transformed.append((item * 2) ^ 45)
    return transformed

def detect_symmetry(pattern):
    # Unused symmetry detector (red herring)
    length = len(pattern)
    for i in range(length // 2):
        if pattern[i] != pattern[length - 1 - i]:
            return False
    return True

def calculate_equilibrium(chain):
    # Core logic hidden among distractions
    processed = []
    for c in chain:
        if c % 4 == 0:
            processed.append(c + 11)
        elif c % 3 == 0:
            processed.append(c - 7)
        else:
            processed.append(c * 2)  # Critical branch
    
    # Final aggregation using modular arithmetic
    score = 0
    for j, v in enumerate(processed):
        score = (score + (v * (j + 1))) % 100000
    return score

# --- Main Execution with High Interference ---
initial_keys = [13, 27, 34, 41, 58, 62]
decoy_buffer = [x ** 3 for x in initial_keys if x < 50]  # Dead data structure

# Generate phase-shifted values (partially irrelevant)
phase_data = [generate_phase_shift(k) for k in initial_keys]

# Simulate harmonic interference (unused)
harmonics = simulate_harmonic(phase_data)

# Derive chaos factor – actual input source
chaos_stream = derive_chaos_factor(initial_keys)

# Filter resonance: modifies stream; contains key preprocessing
filtered_output = filter_resonance(chaos_stream)

# Build convergence chain using itertools
repeater = cycle(filtered_output)
convergence_chain = list(islice(repeater, 20))  # Use first 20 elements

# Introduce decoy operations
entropy_metric = evaluate_entropy(convergence_chain)  # Computed but unused
symmetry_flag = detect_symmetry(convergence_chain)  # Never used

# Compute invariant (looks critical, not directly used)
invariant = compute_invariant(convergence_chain)

# Actual target computation
equilibrium_score = calculate_equilibrium(convergence_chain)

# Print final answer as required
print(f"Target result: {equilibrium_score}")