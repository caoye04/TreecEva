def preprocess_segment(data_chunk, threshold=0.75):
    """Irrelevant preprocessing function for signal segments (distractor)"""
    filtered = [x for x in data_chunk if abs(x) > threshold]
    normalized = [x / max(filtered) if filtered else 0 for x in filtered]
    return normalized


def generate_checksum(sequence):
    """Decoy function: computes XOR checksum but not used in final result"""
    checksum = 0
    for val in sequence:
        checksum ^= int(val * 100) % 256
    return checksum

# Irrelevant global constants (red herrings)
BASE_FREQUENCY = 440.0
HARMONIC_TOLERANCE = 0.023
MAX_ITERATIONS = 1500

# Simulated sensor input buffer with diagnostic codes (mixed types)
sensor_stream = [
    (1, 102, 0.88), (2, 105, 0.91), (3, 102, 0.87),
    (4, 108, 0.93), (5, 102, 0.89), (6, 110, 0.95)
]

# Background noise profile (unused in logic path)
noise_floor = {102, 105, 110, 115, 120}
baseline_offsets = {k: v * 0.01 for k, v in enumerate([88, 91, 87, 93, 89])}

# Core signal processing variables
pattern_buffer = [item[1] for item in sensor_stream]  # Extract diagnostic codes
mask_sequence = [item[2] > 0.88 for item in sensor_stream]  # Boolean activation mask

# Dead code path: complex but unused transformation
temp_magnitude = sum(abs(x) for x in pattern_buffer) / len(pattern_buffer)
reference_key = ''.join(map(str, [1, 0, 2]))  # Decoy key

# Distractor: tuple unpacking with irrelevant assignment
(_, last_code, confidence) = sensor_stream[-1]
activation_log = []

# Misleading intermediate calculation (appears important)
aggregated_metric = 0
for i, val in enumerate(pattern_buffer):
    if i % 2 == 0:
        aggregated_metric += val * 0.1
    else:
        aggregated_metric -= val * 0.05

# Real computation begins: set operations and zip usage
valid_codes = set(pattern_buffer)
common_with_noise = valid_codes & noise_floor  # Overlap (not actually needed)

# Key logical transformation using enumerate and zip
adjustment_factor = 0.0
for idx, (code, active) in enumerate(zip(pattern_buffer, mask_sequence)):
    if active:
        adjustment_factor += (code % 17) * 0.01
    if idx > 0 and pattern_buffer[idx-1] == code:
        adjustment_factor += 0.005

# Conditional data restructuring (tuple usage)
diagnostic_pairs = [(pattern_buffer[i], pattern_buffer[i+1]) 
                     for i in range(len(pattern_buffer)-1)]

# Bitwise manipulation layer (core concept)
bit_encoded = 0
for code in pattern_buffer[:4]:
    bit_encoded ^= (code << 2) & 0xFF  # Shift and mask

# Secondary conditional branch with decoy update
if len(valid_codes) > 4:
    temp_adjust = 123
    temp_adjust &= ~bit_encoded  # Unused operation

# Actual answer computation chain (8-12 steps)
def analyze_signal(pattern, mask):
    accumulator = 0
    toggle = True
    
    for i, p in enumerate(pattern):
        if i >= len(mask):
            break
        # Step 1: base contribution
        if mask[i]:
            accumulator += p // 10
        # Step 2: alternating logic
        if toggle and p % 2 == 0:
            accumulator += 1
            toggle = False
        # Step 3: positional bonus
        if i == p % 10:
            accumulator += 5
        # Step 4: history-sensitive penalty
        if i > 0 and pattern[i-1] == p:
            accumulator -= 2
        # Step 5: set membership check
        if p in {102, 108}:
            accumulator += 3
        # Step 6: bitwise interaction
        accumulator ^= (i & 3)  # XOR with index mod 4
        
    # Step 7: post-loop correction
    if accumulator > 50:
        accumulator = accumulator // 2
    # Step 8: final adjustment via float conversion
    accumulator += int(adjustment_factor * 100)
    
    return accumulator

# Execute critical statement
calibration_data = preprocess_segment([x[2] for x in sensor_stream])
final_diagnostic = analyze_signal(pattern_buffer, mask_sequence)

# Print result as required
print(f"Result: {final_diagnostic}")