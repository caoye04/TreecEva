def analyze_signal(samples, threshold=0.5):
    """Irrelevant signal processing function (dead path)."""
    filtered = [s for s in samples if abs(s) > threshold]
    return [f ** 2 for f in filtered]


def generate_checksum(data):
    """Misleading checksum used nowhere in critical path."""
    chk = 0
    for item in data:
        chk ^= hash(str(item)) % 256
    return chk

# Irrelevant constants (red herrings)
MAX_BUFFER_SIZE = 1024
DEFAULT_TIMEOUT = 15.5
SYSTEM_MODE = 'diagnostic'

# Core diagnostic data (mixed with noise)
diagnostics = [
    85.6,   # CPU temperature (°C)
    42,     # Fan RPM (thousands)
    3.21,   # Voltage rail A (V)
    1.85,   # Voltage rail B (V)
    0.97,   # Current draw (A)
    777     # Sensor ID (irrelevant)
]

# Weights for actual computation (key input)
weights = [0.4, 0.3, 0.2, 0.1, 0.05, 0]  # Last weight nullifies Sensor ID

# Dead code: Unused transformation
inverted_weights = [round(1/w, 2) if w != 0 else 999 for w in weights]

# Distractor: fake aggregation
baseline_shift = sum(diagnostics[:3]) * 0.1
offset_correction = [d + baseline_shift for d in diagnostics]

# Real computation begins here — deeply nested
if len(diagnostics) == len(weights):
    weighted_sum = 0
    temp_cache = []
    for i in range(len(diagnostics)):
        entry = diagnostics[i]
        weight = weights[i]
        
        # Bit manipulation red herring
        if isinstance(entry, int):
            masked = entry & 0b111111  # Only lower 6 bits
            entry = masked if masked > 0 else entry
        
        # Conditional expression (required feature)
        adjusted_entry = entry if entry >= 0 else abs(entry) * 1.1
        
        # Accumulate only if weight has effect
        if weight > 0:
            contribution = adjusted_entry * weight
            temp_cache.append(round(contribution, 4))
            weighted_sum += contribution
        else:
            temp_cache.append(0)
    
    # Secondary validation (distraction)
    if len(temp_cache) > 5:
        slice_peak = max(temp_cache[1:4])  # Slicing (required feature)
        decay_factor = slice_peak * 0.05
        weighted_sum -= decay_factor
    
    # Tertiary check: character-based switch (case conversion)
    mode_flag = 'CALIBRATE'
    normalization_enabled = mode_flag.lower() == 'calibrate'
    
    if normalization_enabled:
        count_chars = len(mode_flag)
        weighted_sum /= (count_chars / 4)  # Divide by 2.25 → 1.777...
    
    # Final transformation
    final_diagnostic = round(weighted_sum * 1.03, 6)
else:
    final_diagnostic = -999  # Dead branch

# Unused data structure with cross-reference
log_entry = {
    'timestamp': '2024-05-20',
    'values': diagnostics,
    'weights_used': weights,
    'temp_results': temp_cache,
    'checksum': generate_checksum(diagnostics)  # Decoy call
}

# Output required result
Result: {final_diagnostic}