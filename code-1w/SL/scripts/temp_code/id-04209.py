def simulate_quantum_decay(registers):
    # Irrelevant simulation function (dead code path)
    for i in range(len(registers)):
        registers[i] = (registers[i] * 17 + 3) % 256
    return registers


def compute_entropy(signal):
    # Distractor: computes entropy but not used in final result
    from math import log2
    freq = {}
    for s in signal:
        freq[s] = freq.get(s, 0) + 1
    entropy = 0.0
    total = len(signal)
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 6)


def validate_checksum(structure):
    # Decoy validation function that looks important but isn't used
    checksum = 0
    for idx, val in enumerate(structure):
        checksum ^= (val + idx) * 3
    return checksum == 0


def extract_patterns(sequence):
    # Unused pattern extractor - misleading intermediate logic
    patterns = []
    for i in range(len(sequence) - 2):
        if sequence[i] < sequence[i+1] > sequence[i+2]:
            patterns.append(i)
    return patterns


def analyze_system_state(registers):
    # Core logic begins
    temp_state = [r for r in registers]
    
    # Apply bit rotation (relevant)
    rotated = []
    for val in temp_state:
        # Right rotate 3 bits
        rotated.append(((val >> 3) | (val << 5)) & 255)
    
    # Misleading normalization (looks important but irrelevant)
    normalized = [round(v / 255.0, 4) for v in rotated]
    
    # Key transformation: XOR with index and sum
    indexed_sum = 0
    for idx, val in enumerate(rotated):
        if idx % 2 == 1:  # Only odd indices contribute
            indexed_sum += val ^ idx
    
    # Secondary filter using slicing (relevant)
    segment = rotated[1:6:2]  # Take elements at indices 1,3,5
    
    # Accumulate filtered values with character counting red herring
    decoy_text = "diagnostic_frame_2048"
    char_count = {c: decoy_text.count(c) for c in set(decoy_text)}  # Distractor dictionary
    
    # Actual contribution: sum of segment with offset
    partial = sum(segment) + len(char_count)  # len(char_count)=10, but masked as complex
    
    # Combine paths: only indexed_sum contributes
    final_score = indexed_sum  # This line overwrites any prior confusion
    
    # Tertiary distraction: zip unused lists
    timestamps = [120, 125, 130]
    phases = ['A', 'B', 'C']
    sync_map = dict(zip(timestamps, phases))  # Dead code
    
    # Final computation
    diagnostic_code = (partial * 0) + final_score  # Neutralize partial
    return diagnostic_code

# Initialization block
initial_load = [120, 200, 75, 150, 90, 220, 60, 180]

# Apply decoy transformations
processed_load = [x for x in initial_load]
processed_load.sort(reverse=True)  # Sorting side effect (irrelevant)

# Add noise vector (distractor)
noise_profile = [3, 1, 4, 1, 5, 9, 2, 6]
noisy_load = [p ^ n for p, n in zip(processed_load, noise_profile)]

# Real input to function
quantum_registers = [x for x in initial_load]  # Reset to original

# Critical execution point
final_diagnostic = analyze_system_state(quantum_registers)

# Output result
print(f"Result: {final_diagnostic}")