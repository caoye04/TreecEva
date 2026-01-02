def preprocess_signal(data):
    # Irrelevant preprocessing (dead code path)
    normalized = [x / max(data) for x in data]
    filtered = [x for x in normalized if x > 0.5]
    return sum(filtered) * 0.1

# Misleading global variables
turbulence_index = 42
phase_offset = [0, 1, 1, 2, 3, 5, 8]
entropy_buffer = {'a': 1, 'b': 2, 'c': 3}

# Decoy function that looks important but is never called
def compute_resonance(freq):
    import math
    return math.sin(freq) * math.cos(freq / 2)

# Real logic begins here
quantum_signature = [6, 3, 8, 2, 9, 1, 7]

def generate_key_vector(seq):
    # Uses lambda and conditional expression
    transform = lambda x: x ** 2 if x % 2 == 0 else x + 1
    return [transform(n) for n in seq]

key_vector = generate_key_vector(quantum_signature)

# Distractor: complex-looking but unused calculation
checksum = 0
for i, val in enumerate(key_vector):
    checksum += val * (i + 1)
checksum = checksum % 1000

# Another decoy: character counting in a meaningless string
diagnostic_log = "Error at sector 7G: flux capacitor unstable"
char_count = len([c for c in diagnostic_log if c.isalpha()])

# Core logic hidden among distractions
flags = set()
for x in quantum_signature:
    if x > 5:
        flags.add(x)

status_map = {k: k * 2 for k in flags}  # Dictionary transformation

# Conditional expression with side-effect-free mutation
intermediate = sum(status_map.values()) if len(flags) > 3 else -1

scaling_factor = 1.5

# This function contains the actual answer derivation
def analyze_system_state(signal):
    # Nested logic with multiple steps
    a = sum(x for x in signal if x % 2 == 0)  # Sum evens
    b = len([x for x in signal if x > 6])      # Count above threshold
    c = signal[2] * signal[-1]                 # Product of specific indices
    
    # Bit manipulation red herring
    bit_fiddle = (a << 2) ^ b
    mask_result = bit_fiddle & 0xFF
    
    # Actual relevant computation (non-obvious due to noise)
    base_score = a + (b * c)
    
    # More misdirection
    history_trace = [{'step': i, 'val': base_score >> i} for i in range(3)]
    
    # Final calculation using lambda in conditional context
    modifier = (lambda x: x * 1.2)(len(signal)) if mask_result > 50 else 5
    
    # The real answer
    return int(base_score * scaling_factor + modifier)

# Critical execution point
final_diagnostic = analyze_system_state(quantum_signature)

# Output result as required
print(f"Result: {final_diagnostic}")