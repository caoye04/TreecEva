def analyze_performance(timestamps, thresholds):
    # Irrelevant data transformation (dead path)
    normalized = [t % 100 for t in timestamps if t > 0]
    stats = { 'mean': sum(normalized) / len(normalized) }
    return stats['mean'] if stats['mean'] > 50 else 0

# Unused function - red herring
def decrypt_key(key_str):
    return ''.join(chr(ord(c)-1) for c in key_str[::-1])

# Decoy variables with plausible but unused computations
baseline_offset = 37.2
aggregation_window = [i * 0.75 for i in range(20)]
correlation_matrix = [[i*j for j in range(5)] for i in range(5)]

# Real input data
log_entries = [
    {'time': 120, 'level': 'ERROR', 'payload': [1, 3, 2]},
    {'time': 145, 'level': 'WARN', 'payload': [4, 1]},
    {'time': 160, 'level': 'ERROR', 'payload': [2, 2, 1]}]

system_flags = { 'debug_mode': False, 'tracing_enabled': True }

# Distractor: complex-looking but unused bitwise computation
shadow_mask = 0
for i in range(8):
    shadow_mask ^= (i << (i % 3))

# Auxiliary function that appears important but is only partially used
def extract_dimensions(records):
    dimensions = []
    for idx, entry in enumerate(records):
        size = len(entry['payload'])
        priority = 1 if entry['level'] == 'ERROR' else 0
        dimensions.append((idx, size, priority))
    return dimensions

# Another decoy using set operations (seemingly relevant)
unique_levels = set([entry['level'] for entry in log_entries])
level_snapshot = set(['ERROR', 'INFO', 'DEBUG'])
divergence = level_snapshot.difference(unique_levels)  # unused

# Critical processing function
def compute_integrity_score(entries):
    total_weight = 0
    error_count = 0
    for e in entries:
        # Only ERROR logs contribute to final result
        if e['level'] == 'ERROR':
            magnitude = sum(p ** 2 for p in e['payload'])
            total_weight += magnitude
            error_count += 1
    return total_weight if error_count > 0 else -1

# Simulated diagnostic pipeline
def evaluate_health(metrics, config):
    score = compute_integrity_score(metrics)
    adjustment = 1.75 if config.get('tracing_enabled') else 0.9
    # Complex conditional with misleading branches
    if score < 0:
        return 0
    elif score > 50:
        return score * adjustment - 12.5
    else:
        return score * 1.1

# Data alignment using zip and enumerate (actual use)
def align_segments(data_list):
    indices = []
    values = []
    for i, d in enumerate(data_list):
        indices.append(i)
        values.append(len(d['payload']))
    paired = list(zip(indices, values))
    # Use of enumerate and zip in meaningful context
    offset_map = {p[0]: p[1] * 2 for p in paired}
    return sum(offset_map.values())

# Final integration function
def process_metrics(logs, flags):
    # Step 1: Compute integrity score (core logic)
    raw_score = compute_integrity_score(logs)
    
    # Step 2: Derive alignment bonus (actually used)
    alignment_bonus = align_segments(logs)
    
    # Step 3: Apply health evaluation (calls evaluate_health)
    health_factor = evaluate_health(logs, flags)
    
    # Step 4: Combine results through non-obvious formula
    intermediate = raw_score + alignment_bonus
    
    # Step 5: Masking operation with bit manipulation (actually contributes)
    mask = (intermediate >> 2) & 0xFF
    
    # Step 6: Final composition
    final_diagnostic = int(intermediate ^ mask + health_factor)
    
    # Red herring: unused min/max calculation on irrelevant data
    dummy_sequence = [len(str(baseline_offset * i)) for i in range(1, 8)]
    ceiling_ref = max(dummy_sequence) if sum(dummy_sequence) > 20 else min(dummy_sequence)
    
    # Another dead end: unused string transformation
    temp_label = "diagnostic_{}".format(hex(int(sum(aggregation_window[:3]))))
    
    return final_diagnostic

# Execution point of interest
final_diagnostic = process_metrics(log_entries, system_flags)
print(f"Result: {final_diagnostic}")