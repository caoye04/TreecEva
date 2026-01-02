def analyze_component_health(raw_readings, threshold):
    health_flags = {}
    temp_store = []
    cumulative_score = 0

    for idx, reading in enumerate(raw_readings):
        normalized = (reading % 17) * 3 + idx
        if normalized > 40:
            health_flags[f'cmp_{idx}'] = 'critical'
        elif normalized > 25:
            health_flags[f'cmp_{idx}'] = 'warning'
            temp_store.append(normalized)
        else:
            health_flags[f'cmp_{idx}'] = 'stable'
            cumulative_score += normalized % 7

    # Distractor: unused aggregation
    avg_temp = sum(temp_store) / len(temp_store) if temp_store else 0
    spike_count = len([v for v in health_flags.values() if v == 'critical'])

    return health_flags, cumulative_score


def encode_status_code(status_map):
    code = 1
    for key in sorted(status_map.keys()):
        if 'critical' in status_map[key]:
            code *= 3
        elif 'warning' in status_map[key]:
            code *= 2
    return code if code > 1 else 5


def decrypt_sequence(encoded, shift):
    result = 0
    for c in str(encoded):
        result = result * 10 + ((int(c) - shift) % 10)
    return result

# Irrelevant helper - dead code path
def simulate_backup(config):
    import time
    timestamp = int(time.time()) % 10000
    encrypted_key = (timestamp * 73) % 9973
    return f'bkp_{encrypted_key}'

# Main data processing chain
system_logs = [
    [104, 23, 67, 89, 45],
    [12, 88, 33, 51],
    [76, 19, 94, 41, 22, 63]
]

active_threshold = 28
bypass_modes = {'mode_x': False, 'mode_y': True}
override_matrix = [[1, 0], [0, 1]]

aggregated_diagnostics = []
meta_flag_count = 0

for log_block in system_logs:
    flags, score = analyze_component_health(log_block, active_threshold)
    
    # Real computation path
    encoded = encode_status_code(flags)
    shifted_code = decrypt_sequence(encoded, 1)
    adjusted_score = (score * 13) % 1000
    
    # Red herring: complex-looking but unused calculation
    dummy_transform = ''.join(sorted(set(str(shifted_code)), reverse=True))
    shadow_value = sum(ord(c) for c in dummy_transform) % 500
    
    diagnostic_key = (shifted_code + adjusted_score) % 9871
    aggregated_diagnostics.append(diagnostic_key)

    # Misleading counter that looks important
    if len(log_block) > 4:
        meta_flag_count += 1

# Unused summary structure - distractor
summary_report = {
    'total_blocks': len(system_logs),
    'meta_flags': meta_flag_count,
    'bypass_active': any(bypass_modes.values()),
    'checksum': sum(aggregated_diagnostics) % 10000
}

# Critical computation - combines prior results
fusion_seed = sum(aggregated_diagnostics) % 10000
final_diagnostic = (fusion_seed * 7 + 5) % 100000

# Decoy transformation
hashed_diagnostic = decrypt_sequence(fusion_seed, 3)

print(f"Result: {final_diagnostic}")