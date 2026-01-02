def analyze_sequence(data):
    # Irrelevant transformation: character case manipulation
    upper_count = sum(1 for c in data if c.isupper())
    lower_count = sum(1 for c in data if c.islower())
    toggled = ''.join(c.lower() if c.isupper() else c.upper() for c in data)

    # Red herring: unused sorting operation
    sorted_chars = sorted(data)
    reversed_seq = data[::-1]

    # Distractor: bit manipulation with no impact
    magic_shift = (len(data) << 2) ^ 255

    # Relevant logic: count vowels for later use
    vowel_count = sum(1 for c in data.lower() if c in 'aeiou')
    return vowel_count

# Simulated log signature processing (mostly dead code)
def validate_signature(sig):
    if len(sig) % 2 == 0:
        return sig[-1] != 'X'
    else:
        return sig[0] == 'A'

# Unused recursive checksum (decoy function)
def checksum_recursive(arr):
    if len(arr) <= 1:
        return arr[0] if arr else 0
    return arr[0] + checksum_recursive(arr[1:])

# Core metric processor - only this matters
def compute_health_score(seq, flags):
    base = len(seq) * 3
    offset = 0
    
    # Conditional expression chain (required feature)
    offset += 10 if 'DEBUG' in flags else 5
    offset += 7 if 'VERBOSE' in flags and len(seq) > 10 else 0
    offset -= 3 if 'LEGACY' in flags else 0
    
    # Bitwise interference (partially relevant)
    flag_bits = 0
    for f in flags:
        flag_bits ^= hash(f) & 15  # Only low 4 bits used
    
    adjustment = (flag_bits & 3) - 1  # Maps to -1, 0, or 1
    
    return base + offset + adjustment

# Main processing function
def process_metrics(logs, config):
    # Extract diagnostic tokens (string method usage)
    tokens = [item.strip().split(':')[1].strip() for item in logs if ':' in item]
    
    # Irrelevant token analysis
    token_lengths = [len(t) for t in tokens]
    avg_length = sum(token_lengths) / len(token_lengths) if token_lengths else 0
    
    # Dead code path: never executed due to constant condition
    emergency_override = False
    if 0 > len(tokens) * 2:  # Always false
        emergency_override = True
        critical_reset = [c[::-1] for c in tokens if 'ERR' in c]
    
    # Meaningful but obscured accumulation
    total_weight = 0
    for i, token in enumerate(tokens):
        if 'TRACE' in token:
            total_weight += i * 2
        elif 'METADATA' in token:
            total_weight += len(token) // 4
        elif 'SESS' in token:
            total_weight += hash(token) % 7
    
    # Critical intermediate value buried in noise
    entropy_proxy = analyze_sequence(''.join(tokens))
    
    # Primary health computation (only this affects final result)
    raw_score = compute_health_score(tokens, config)
    
    # Distractor: complex but unused formula
    synthetic_index = (avg_length ** 1.5) + (len(tokens) * entropy_proxy)
    normalized_index = synthetic_index / (1 + abs(hash(str(config)) % 100))
    
    # Final computation with conditional override (never triggered)
    final_value = raw_score * 4 + entropy_proxy
    if 'CRITICAL_MODE' in config and emergency_override:
        final_value = 999  # Unreachable
    
    return int(final_value)

# Setup test scenario
log_entries = [
    "STATUS: TRACE_INIT",
    "MODE: METADATA_REFRESH_LOOP",
    "STATE: SESS_RESTART_REQUIRED",
    "LEVEL: TRACE_BACKUP_PENDING",
    "CODE: NOMINAL_OPERATION"
]

system_flags = ['DEBUG', 'VERBOSE']  # Influences offset in health score

# Execution point of interest
final_diagnostic = process_metrics(log_entries, system_flags)

print(f"Result: {final_diagnostic}")