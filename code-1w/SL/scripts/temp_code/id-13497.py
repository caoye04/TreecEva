def analyze_system_load(usage_logs):
    # Irrelevant data transformation
    timestamps = [log.split()[0] for log in usage_logs if 'ERROR' not in log]
    errors = list(filter(lambda x: 'ERROR' in x, usage_logs))
    critical_count = len([e for e in errors if 'CRITICAL' in e])

    # Distractor: complex string processing with no impact
    summary = ''.join([t[-2:] for t in timestamps]).replace('PM', '').replace('AM', '')
    checksum = sum(ord(c) for c in summary) % 100

    # Real computation buried in noise
    raw_values = []
    for log in usage_logs:
        parts = log.split()
        if len(parts) > 2 and parts[1].isdigit():
            raw_values.append(int(parts[1]))

    return raw_values


def normalize_data(stream):
    # Dead function - never used but looks important
    return [x / max(stream) if max(stream) != 0 else 0 for x in stream]


def calculate_efficiency_index(data):
    # Decoy calculation with intermediate misleading results
    base = sum(data) / len(data) if data else 0
    variance = sum((x - base) ** 2 for x in data) / len(data) if data else 0
    peak = max(data) if data else 0

    # Looks important but unused
    adjusted_peak = peak * (1 + variance / 100) if variance < 50 else peak * 0.8

    # Actual relevant result
    return base * 0.7 + peak * 0.3


def evaluate_performance(metrics, weights):
    # Mix of relevant and irrelevant operations
    temp_results = {}
    
    # Real logic interwoven with red herrings
    for i, val in enumerate(metrics):
        if i % 2 == 0:
            # Meaningful transformation
            temp_results[f'even_{i}'] = val ** 0.5 * weights[i]
        else:
            # Distractor branch
            temp_results[f'odd_{i}'] = val * 0.1  # Never used

    # Key computation hidden among decoys
    aggregated = sum(temp_results[k] for k in temp_results.keys() if 'even' in k)
    
    # More distractions
    metadata = "analysis_complete_v2.1"
    version_code = sum(ord(c) for c in metadata[:5]) % 7
    
    # Early return that seems like it might trigger, but won't
    if version_code > 10:
        return -999  # Dead code path

    # Final calculation - only this matters
    adjustment_factor = 1.2 if aggregated > 50 else 0.9
    final_score = round(aggregated * adjustment_factor, 4)
    
    # Unused complex structure
    report = {
        'version': metadata,
        'checksum': version_code,
        'findings': {k: v for k, v in temp_results.items() if 'odd' in k}
    }
    
    return final_score

# Simulated system logs - source of truth
logs = [
    '10:15AM 85 CPU_LOAD HIGH',
    '10:16AM 92 MEMORY_USAGE CRITICAL',
    '10:17AM 78 NETWORK_IO',
    '10:18AM 95 DISK_WRITE ERROR_CRITICAL',
    '10:19AM 88 GPU_TEMP',
    '10:20AM 91 FAN_SPEED WARNING'
]

# Extract core metrics - this is where real data comes from
extracted = analyze_system_load(logs)

# Weights applied to even-indexed values only
weights = [0.8, 0.0, 0.9, 0.0, 1.1, 0.0]  # Odd indices get zero weight (but not obvious)

# This calls the key function
final_score = evaluate_performance(extracted, weights)

# Print final answer as required
print(f"Target result: {final_score}")