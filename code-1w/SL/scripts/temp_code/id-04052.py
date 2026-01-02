import math

# Simulated sensor data processing with embedded diagnostics
def collect_readings():
    raw = [127, 255, 192, 64, 32, 15, 8, 3]
    offset = 10
    adjusted = [x - offset for x in raw]
    return adjusted

# Irrelevant helper: formatting timestamps (distractor)
def format_timestamps(count):
    stamps = []
    for i in range(count):
        sec = str(i % 60).zfill(2)
        minu = str((i // 60) % 60).zfill(2)
        stamps.append(f'{minu}:{sec}')
    return stamps  # Unused return

# Signal mask generation using bit manipulation (partially relevant)
def generate_mask(length):
    mask = 0
    for i in range(length):
        if i % 3 == 0:
            mask |= (1 << i)
    return mask

# Core preprocessing with slicing and transformation
def preprocess(signal_stream):
    truncated = signal_stream[1:-1]  # Remove first and last
    filtered = [x for x in truncated if x > 50]
    base_shift = sum(filtered) // len(filtered) if filtered else 0
    
    # Apply exponential decay compensation (advanced arithmetic)
    compensated = []
    for i, val in enumerate(filtered):
        decay_factor = math.exp(-0.1 * i)
        compensated.append(int(val * decay_factor + base_shift * 0.3))
    
    # Dead code path: unused branch (red herring)
    if len(compensated) > 100:
        compensated = compensated[::-2]  # Never reached
    
    return compensated

# Checksum validation (distractor function - looks important)
def validate_checksum(data):
    checksum = 0
    for item in data:
        checksum ^= item
        checksum = (checksum << 1) & 0xFF
    return checksum == 0x7E  # Not used in logic

# String-based diagnostic token generation (irrelevant but complex)
def generate_diagnostics_token(flags):
    token_map = {'A': 'Alpha', 'B': 'Beta', 'C': 'Gamma'}
    parts = []
    for key in sorted(flags.keys()):
        if flags[key]:
            parts.append(token_map.get(key, 'Unknown'))
    joined = '-'.join(parts)
    reversed_parts = joined[::-1].upper()
    return reversed_parts[:8] if len(reversed_parts) > 5 else 'DEFAULT'

# Main analysis with conditional logic and comparisons
def analyze_signal(data):
    size = len(data)
    if size == 0:
        return -1
    
    # Compute statistical indicators
    mean_val = sum(data) / size
    variance = sum((x - mean_val) ** 2 for x in data) / size
    stdev = math.sqrt(variance)
    
    # Bitwise feature extraction
    aggregate = 0
    for val in data:
        aggregate ^= int(stdev + val) & 0xF
    
    # Conditional thresholds with short-circuit logic
    threshold_met = (mean_val > 40.0) or (stdev < 5.0 and size > 3)
    secondary_flag = (aggregate & 5 == 1)  # Rare condition
    
    # Key computation: scaled diagnostic index
    if threshold_met:
        scaling_factor = 1.75 if secondary_flag else 2.25
        index_score = (mean_val * scaling_factor) - (stdev * 1.5)
    else:
        index_score = (mean_val * 0.8) + (aggregate * 2)
    
    # Multiple assignment distraction
    temp_a, temp_b = index_score, index_score * 0.95
    temp_a, temp_b = temp_b, temp_a  # Swap, irrelevant
    
    # Final decision based on composite logic
    flags = {
        'A': mean_val > 60,
        'B': stdev < 8.0,
        'C': aggregate > 7
    }
    
    # Critical line: what is the value of final_diagnostic here?
    final_diagnostic = int(index_score + aggregate * 0.7)
    
    # Decoy output formatting
    token = generate_diagnostics_token(flags)
    stamp_list = format_timestamps(5)
    
    return final_diagnostic

# Execution flow
readings = collect_readings()
processed_data = preprocess(readings)
final_diagnostic = analyze_signal(processed_data)
print(f"Result: {final_diagnostic}")