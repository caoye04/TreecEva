import itertools

# Irrelevant helper function (dead code path)
def unused_signal_transform(x):
    return (x ** 2 + 3 * x + 1) % 7

# Distractor data structures
temporal_weights = [0.1, 0.3, 0.5, 0.7, 0.9]
sample_buffer = list(range(100, 115))
offset_lookup = {i: i * i - 2 * i for i in range(5)}

# Unused recursive decoy
def decoy_recursion(n):
    if n <= 1:
        return 1
    return n * decoy_recursion(n - 2) + 1

# Real signal processing chain
signal_chain = [8, 3, 5, 1, 9, 2]

# Misleading intermediate calculation
aggregate_score = sum(x * (x + 1) // 2 for x in signal_chain if x % 2 == 0)

# Complex transformation with relevant and irrelevant parts
def apply_window_filter(data, window_size=3):
    filtered = []
    for i in range(len(data)):
        window = [data[j % len(data)] for j in range(i, i + window_size)]
        avg = sum(window) / len(window)
        # Red herring computation
        _ = [w ** 0.5 for w in window if w > 2]
        filtered.append(avg * 0.9)
    return filtered

# Bit manipulation decoy
flag_register = 0b101010
for shift in range(4):
    flag_register ^= (flag_register << shift) % 256

# Real core logic disguised among noise
def generate_phase_sequence(base_seq):
    # Use of lambda and itertools - required python features
    cyclic_pairs = itertools.pairwise(itertools.islice(itertools.cycle(base_seq), len(base_seq) * 2))
    phase_shifts = list(map(lambda pair: abs(pair[0] - pair[1]) * 2, cyclic_pairs))
    return phase_shifts[:len(base_seq)]

# Another irrelevant accumulation
shadow_accumulator = 0
for index, val in enumerate(sample_buffer):
    if index % 7 == 0:
        shadow_accumulator += val * temporal_weights[index % 5]

# Key transformation function
def calculate_harmonic_return(sequence):
    # Step 1: Generate derived sequence
    derived = [x for x in sequence if x > 2]
    
    # Step 2: Apply transform
    transformed = [x - 1 for x in derived]
    
    # Step 3: Sum relevant elements
    base_sum = sum(transformed)
    
    # Step 4: Use phase sequence
    phases = generate_phase_sequence(transformed)
    
    # Step 5: Accumulate phase contributions
    phase_total = 0
    for i, p in enumerate(phases):
        if i % 2 == 0:
            phase_total += p
        else:
            phase_total -= p // 2
    
    # Step 6: Combine
    intermediate = base_sum + phase_total
    
    # Step 7: Apply harmonic factor
    harmonic_factor = 0
    for k in range(1, 5):
        harmonic_factor += 1 / (k * (k + 1))
    
    # Step 8: Final adjustment
    result = intermediate * harmonic_factor
    
    # Dead code branch (never executed)
    if False:
        backup = decoy_recursion(len(sequence))
        result = max(result, backup)
    
    return result

# Signal preprocessing - looks important but partially irrelevant
processed_signal = apply_window_filter(signal_chain)

# Dummy assignment to mislead tracking
reference_anchor = [sum(temporal_weights), len(offset_lookup), flag_register]

# Core execution point
final_yield = calculate_harmonic_return(signal_chain)

# Output the target result
print(f"Target result: {final_yield}")