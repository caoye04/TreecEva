import math

# System diagnostics simulation with signal processing and fault detection

def generate_pattern(base: int, length: int) -> list:
    """Generate a non-linear pattern for diagnostic testing (red herring)."""
    result = []
    for i in range(length):
        result.append((base ** i + i * 2) % 256)
    return result

def compute_checksum(data: list) -> int:
    """Simple checksum used in legacy systems (distractor)."""
    return sum(data) % 256

def detect_anomalies(stream: list) -> set:
    """Find outlier values in data stream using set logic."""
    thresholds = {x for x in stream if x > 128}
    noise_floor = {x for x in stream if x < 10}
    return thresholds - noise_floor

def shift_register_update(state: int, input_bit: int) -> int:
    """Simulate 8-bit shift register (bit manipulation red herring)."""
    return ((state << 1) | input_bit) & 0xFF

def encrypt_key(segment: int) -> int:
    """Dummy encryption function not actually used in final path (dead code)."""
    key = segment ^ 0xAA
    key = ((key << 4) | (key >> 4)) & 0xFF
    return key ^ 0x55

def validate_sequence(seq: list) -> bool:
    """Validate sequence structure (unused validation path)."""
    if len(seq) == 0:
        return False
    return all(x >= 0 and x <= 255 for x in seq)

def filter_signals(raw: list, mode: str = 'aggressive') -> list:
    """Filter out edge cases from signal (partially relevant)."""
    if mode == 'aggressive':
        return [x for x in raw if 20 < x < 200]
    else:
        return [x for x in raw if x >= 0]

def analyze_signal(buffer: list, mask: set) -> int:
    """Core analysis: apply mask and compute diagnostic metric."""
    # Apply logical filtering based on anomaly mask
    filtered = [x for x in buffer if x not in mask]
    if not filtered:
        return -1
    
    # Perform modular arithmetic reduction
    reduced = 0
    for i, val in enumerate(filtered):
        reduced = (reduced + (val * (i + 1))) % 97
    
    # Final transformation using trigonometric weighting (deterministic)
    weighted = reduced * math.cos(math.pi / 3)
    return int(weighted) + 50

# Begin simulation setup
initial_seed = 7
pattern_length = 12

# Generate base signal pattern (relevant)
pattern_buffer = generate_pattern(initial_seed, pattern_length)

# Compute auxiliary checksum (irrelevant)
aux_checksum = compute_checksum(pattern_buffer)

# Simulate shift register chain with dummy inputs (distractor loop)
current_state = 0x12
for bit in [1, 0, 1, 1, 0]:
    current_state = shift_register_update(current_state, bit)

# Detect anomalies in original pattern (partially relevant)
anomaly_set = detect_anomalies(pattern_buffer)

# Encrypt unused segment (completely irrelevant)
dummy_segment = 0x3C
obfuscated = encrypt_key(dummy_segment)

# Apply aggressive filtering to clean signal (relevant preprocessing)
filtered_buffer = filter_signals(pattern_buffer, 'aggressive')

# Create fault mask from detected anomalies (key set operation)
fault_mask = detect_anomalies(pattern_buffer)
fault_mask.add(42)  # Inject known fault signature

# Validate sequence (dead branch - result unused)
is_valid = validate_sequence(filtered_buffer)

# Core diagnostic analysis (TARGET EXECUTION POINT)
final_diagnostic = analyze_signal(pattern_buffer, fault_mask)

# Print result as required
print(f"Result: {final_diagnostic}")