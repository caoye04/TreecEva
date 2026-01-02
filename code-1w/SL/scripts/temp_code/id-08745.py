import itertools

# Simulate quantum state transitions and stability analysis
# The actual answer lies in analyzing filtered energy decay sequences

def compute_entropy(seq):
    entropy = 0
    for x in seq:
        if x > 0:
            entropy -= x * x  # Simplified squared penalty
    return entropy

# Irrelevant helper: calculates phase shift (never used)
def calculate_phase_shift(n):
    total = 0
    for i in range(n):
        total += (i % 3) ** 2
    return total

# Decoy function: looks important but unused
def evaluate_coherence(states):
    score = 0
    for s in states:
        if len(s) > 2:
            score += sum(s[:2])
    return score

# Real logic: find stable subsequences under threshold constraints
def analyze_stability(energy_levels, limits):
    equilibrium_sum = 0
    
    # Generate all contiguous sublists (windows)
    subsequences = []
    for i in range(len(energy_levels)):
        for j in range(i+1, len(energy_levels)+1):
            subsequences.append(energy_levels[i:j])
    
    # Filter by length and max threshold
    valid_windows = [win for win in subsequences if len(win) >= 3 and max(win) <= limits[0]]
    
    # Further filter using average threshold (actual key step)
    refined_candidates = [w for w in valid_windows if sum(w)/len(w) <= limits[1]]
    
    # Compute transformation on candidates
    transformed = []
    for win in refined_candidates:
        # Apply alternating sign based on index parity
        signed = [(-1)**i * val for i, val in enumerate(win)]
        transformed.append(sum(signed))
    
    # Use itertools to generate pairwise differences (distraction)
    pairwise_deltas = []
    for a, b in itertools.combinations(transformed, 2):
        pairwise_deltas.append(abs(a - b))
    
    # Dead code path: never contributes to result
    if len(pairwise_deltas) > 10:
        outlier = max(pairwise_deltas) - min(pairwise_deltas)
        equilibrium_sum -= outlier // 5
    
    # Core computation: sum of transformed values modulated by entropy-like term
    base_value = sum(transformed)
    
    # Red herring: complex-looking but unused calculation
    decoy_momentum = 0
    temp_seq = [len(x)*x[0] for x in refined_candidates if x]
    for t in temp_seq:
        for shift in range(3):
            decoy_momentum ^= (t << shift)
    
    # Actual contribution: use only every second transformed value
    for idx, val in enumerate(transformed):
        if idx % 2 == 0:
            equilibrium_sum += val * (idx + 1)
    
    # Final adjustment using slice-based checksum (relevant)
    flat_data = [item for sublist in refined_candidates for item in sublist]
    if len(flat_data) > 5:
        checksum_slice = flat_data[2:-2:2]  # Every other element from truncated middle
        checksum = sum(checksum_slice)
        equilibrium_sum += checksum
    
    return equilibrium_sum

# Initialize simulation parameters
energy_states = [
    [1, 3, 2, 4],
    [2, 1, 1],
    [3, 2, 2, 1, 1],
    [1, 1, 3],
    [2, 2, 2],
    [1, 2, 1, 1]
]

# Flatten into 1D sequence for processing
flattened_energies = [item for sublist in energy_states for item in sublist]

# Thresholds for filtering: [max_peak, avg_limit]
thresholds = [3, 2.1]

# Irrelevant data structures (distractors)
data_logs = {
    'entries': [
        {'id': 101, 'flag': 5},
        {'id': 102, 'flag': 3},
        {'id': 103, 'flag': 7}
    ],
    'metrics': [compute_entropy([1,2,3]), compute_entropy([4,5])]  # Unused
}

# Hidden state tracker (red herring)
current_mode = 'CALIBRATION'
mode_weights = {'RUN': 1.1, 'DEBUG': 0.5, 'CALIBRATION': 0}

# Spurious transformation chain
buffer_stack = []
for val in flattened_energies:
    buffer_stack.append(val ^ 3)
    if val % 2 == 0:
        buffer_stack[-1] <<= 1

# Another decoy list comprehension
shadow_copy = [x for x in flattened_energies if x in {1,2}]
shadow_copy = [x*1.5 for x in shadow_copy][::-1]

# Key assignment — the answer depends on this call
equilibrium_score = analyze_stability(flattened_energies, thresholds)

# Print final result
print(f"Result: {equilibrium_score}")