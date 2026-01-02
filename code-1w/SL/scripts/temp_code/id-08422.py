def preprocess_signal(data):
    return [x ^ 255 for x in data if x % 3 != 0]


def decode_entropy(stream):
    entropy = 0
    for val in stream:
        entropy += (val & 17) | (val >> 4)
    return entropy * 0.9


def validate_checksum(seq):
    checksum = 0
    for i, v in enumerate(seq):
        checksum ^= v + i * 3
    return checksum == 42


def transform_sequence(seq):
    temp = [s << 1 for s in seq]
    filtered = [t for t in temp if t < 500]
    normalized = [f / 2 for f in filtered]
    return [int(n) for n in normalized]

# Irrelevant helper (distractor)
def obsolete_routing_table(n):
    table = []
    for i in range(n):
        table.append((i, (i * 5 + 2) % 7))
    return table

# Unused function (dead code path)
def legacy_compatibility_mode():
    return sum([i ** 2 for i in range(10)]) // 3

# Misleading intermediate calculation
current_phase_offset = sum([decode_entropy([64, 128, 192]) for _ in range(3)])

# Real computation begins
raw_input_stream = [12, 45, 67, 89, 101, 113, 125, 137]
signal_buffer = preprocess_signal(raw_input_stream)

# Simulated quantum buffer (core data)
quantum_buffer = []
for x in signal_buffer:
    if x > 100:
        quantum_buffer.append(x % 89)
    elif x > 50:
        quantum_buffer.extend([x % 7, x % 11])
    else:
        quantum_buffer.append(x * 2)

# System flags with red herring values
system_flags = {
    'debug_mode': False,
    'legacy_protocol': True,
    'encryption_level': 7,
    'checksum_valid': validate_checksum(quantum_buffer),
    'phase_locked': len(quantum_buffer) > 10
}

# Distractor: string-based decoy processing
device_id = "QX-9000"
if device_id.startswith("Q") and len(device_id) > 5:
    encoded_tag = device_id.replace("-", ":").upper().strip("\0")
    version_check = len(encoded_tag.split(":")) == 2

# Secondary transformation chain (partially relevant)
working_data = transform_sequence(quantum_buffer)

# Conditional expression with embedded logic twist
interim_result = working_data[::-1] if system_flags['phase_locked'] else working_data[::2]

# Bit manipulation layer
masked_values = []
for v in interim_result:
    masked = (v ^ 240) & 127
    if masked > 10:
        masked_values.append(masked)

# Core analysis function with multiple concepts
def analyze_system_state(buffer, flags):
    base_score = sum(buffer) / (len(buffer) or 1)
    
    # Boolean logic + comparison chain
    safety_override = flags['debug_mode'] and not flags['legacy_protocol']
    security_penalty = 0
    if flags['encryption_level'] < 5 or not flags['checksum_valid']:
        security_penalty = -25.5
    
    # Dictionary-based adjustment
    adjustments = {
        'low': 10.2,
        'medium': -5.8,
        'high': 30.1
    }
    
    # String-controlled flow (uses id)
    level_key = "medium" if "X" in device_id else "low"
    
    # Complex conditional expression
    risk_factor = 1.5 if len(buffer) > 8 else (0.8 if sum(masked_values) > 100 else 1.1)
    
    # Final composition
    aggregate = base_score
    aggregate += adjustments.get(level_key, 0)
    aggregate += security_penalty
    aggregate *= risk_factor
    
    # Critical final computation
    final_diagnostic = int(round(aggregate * 2))
    
    # Dead code (never executed)
    if False:
        final_diagnostic = decode_entropy(buffer)
        
    return final_diagnostic

# Execute main analysis
final_diagnostic = analyze_system_state(quantum_buffer, system_flags)

# Print result as required
print(f"Target result: {final_diagnostic}")