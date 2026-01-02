import math

# Simulated system telemetry data with mixed types and noise
telemetry_stream = [
    {'time': 0.1, 'value': '1010', 'type': 'binary_sensor', 'seq': 'A'},
    {'time': 0.2, 'value': '1100', 'type': 'binary_sensor', 'seq': 'B'},
    {'time': 0.3, 'value': '1010', 'type': 'binary_sensor', 'seq': 'C'},
    {'time': 0.4, 'value': 'invalid', 'type': 'error', 'seq': None},
    {'time': 0.5, 'value': '1111', 'type': 'binary_sensor', 'seq': 'D'}
]

# Irrelevant auxiliary mapping (distractor)
symbol_map = {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69}

# System flags with some decoy entries
system_flags = {
    'debug_mode': False,
    'encrypt_logs': True,
    'threshold': 12,
    'mask_sensors': False,
    'legacy_mode': 'disabled'
}

# Dummy transformation matrix (unused red herring)
transform_matrix = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [1, 1, 0, 0],
    [0, 0, 1, 1]
]

# Legacy checksum function (dead code path)
def legacy_checksum(data):
    return sum(ord(c) for c in str(data)) % 256

# Auxiliary string analysis (partial distractor, minor use)
analyze_string = lambda s: (len(s), s.startswith('1'), s.count('1')) if isinstance(s, str) else (0, False, 0)

# Bitwise reducer with meaningful use in final logic
def reduce_bits(bit_str):
    if not isinstance(bit_str, str) or not all(c in '01' for c in bit_str):
        return 0
    value = int(bit_str, 2)
    return (value ^ (value >> 1)) & 0xF  # Apply XOR shift and mask

# Complex log parser with filtering and transformation
def parse_logs(raw_stream):
    parsed = []
    errors = 0
    for entry in raw_stream:
        t = entry['time']
        v = entry['value']
        ty = entry['type']
        # Filter only valid binary sensors
        if ty == 'binary_sensor' and isinstance(v, str) and all(c in '01' for c in v):
            length, starts_with_one, ones_count = analyze_string(v)
            # Compute reduced feature
            reduced = reduce_bits(v)
            # Add derived features (some used later)
            parsed.append({
                'timestamp': t,
                'bit_len': length,
                'leading_one': starts_with_one,
                'ones': ones_count,
                'reduced': reduced,
                'entropy': math.log2(reduced + 1) if reduced > 0 else 0.0
            })
        else:
            errors += 1
    # Return stats and filtered data
    return parsed, errors

# Secondary processor to extract temporal patterns (mostly irrelevant)
def extract_patterns(entries):
    if len(entries) < 2:
        return {'jitter': 0.0, 'trend': 'stable'}
    jitter = sum(
        abs(entries[i+1]['timestamp'] - entries[i]['timestamp'])
        for i in range(len(entries)-1)
    )
    trend = 'increasing' if entries[-1]['timestamp'] > entries[0]['timestamp'] else 'decreasing'
    return {'jitter': jitter, 'trend': trend}

# Core metric computation with key logic
# This also uses dictionary aggregation
# Only the 'reduced' values are critical here
def compute_metrics(parsed_data):
    aggregated = {}
    total_reduced = 0
    count = 0
    for record in parsed_data:
        r = record['reduced']
        total_reduced += r
        count += 1
        # Build histogram (only last bin matters indirectly)
        bucket = r // 4
        aggregated[bucket] = aggregated.get(bucket, 0) + 1
    
    # Key intermediate result
    avg_reduced = total_reduced / count if count else 0
    
    # Use dictionary to map to diagnostic level
    level_map = {0: 10, 1: 20, 2: 40, 3: 80}
    # Only bucket 3 is present due to data
    diagnostic_score = sum(level_map.get(k, 0) * v for k, v in aggregated.items())
    
    return {
        'avg_feature': avg_reduced,
        'diagnostic_code': diagnostic_score,
        'record_count': count
    }

# Main processor combining multiple inputs
def process_metrics(logs, flags):
    # Parse logs (core data extraction)
    parsed, err_count = parse_logs(logs)
    
    # Extract temporal pattern (distractor - computed but not used)
    pattern_stats = extract_patterns(parsed)
    
    # Compute core metrics (used)
    metrics = compute_metrics(parsed)
    
    # Simulated encryption overhead (irrelevant)
    if flags.get('encrypt_logs'):
        overhead = sum(1 for p in parsed if p['leading_one']) * 0.25
        # Not used anywhere
    
    # Debug mode effect (not triggered)
    if flags.get('debug_mode'):
        return -999  # Dead path
    
    # Final diagnostic calculation
    base_score = metrics['diagnostic_code']
    adjustment = metrics['record_count'] * 2
    
    # Apply bitwise adjustment based on threshold
    threshold = flags.get('threshold', 10)
    adjusted = (base_score + adjustment) ^ threshold  # XOR with threshold
    
    # Final nonlinear transformation
    final_diagnostic = int((adjusted * 1.5) - math.sqrt(abs(adjusted - 50)))
    
    return final_diagnostic

# Execution flow begins
parsed_entries, _ = parse_logs(telemetry_stream)

# Key statement
final_diagnostic = process_metrics(telemetry_stream, system_flags)

print(f"Result: {final_diagnostic}")