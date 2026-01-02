import itertools

# System telemetry simulation for distributed node integrity assessment
def generate_synthetic_logs(node_count, duration_hours):
    base_pattern = [0.98, 0.94, 0.87, 0.76, 0.65, 0.52, 0.41, 0.33]
    logs = []
    for node in range(node_count):
        phase = node % len(base_pattern)
        fluctuation = (node * 0.01) % 0.1
        node_log = [(base_pattern[phase] + fluctuation) * (1 - (i / duration_hours) * 0.2) for i in range(duration_hours)]
        logs.append(node_log)
    return logs

# Legacy diagnostic function (irrelevant but plausible)
def calculate_legacy_metric(data_stream):
    if not data_stream:
        return 0
    avg_val = sum(data_stream) / len(data_stream)
    peak = max(data_stream)
    normalized = (avg_val / peak) * 100
    penalty = 0
    for val in data_stream:
        if val < 0.5:
            penalty += 5
    return round(normalized - penalty, 2)

# Redundant flag validator (dead path)
def validate_flag_compatibility(flags):
    required_pairs = [('A', 'B'), ('C', 'D'), ('E', 'F')]
    present_combinations = list(itertools.combinations(sorted(flags), 2))
    matched = [pair for pair in required_pairs if pair in present_combinations]
    return len(matched) >= 2

# Core recursive signal decay analyzer
def analyze_signal_decay(log_sequence, threshold=0.4, depth=0):
    if depth > 10 or not log_sequence:
        return 0
    current = log_sequence[0]
    if current < threshold:
        return depth
    return analyze_signal_decay(log_sequence[1:], threshold * 0.92, depth + 1)

# Secondary correlation tracker (distractor)
def track_temporal_correlation(log_matrix):
    if len(log_matrix) < 2:
        return 0.0
    transposed = list(zip(*log_matrix))
    correlations = []
    for segment in transposed:
        mean_val = sum(segment) / len(segment)
        variance = sum((x - mean_val) ** 2 for x in segment) / len(segment)
        correlations.append(variance)
    return round(sum(correlations) / len(correlations), 3)

# Primary integrity computation engine
def compute_integrity_score(flags, logs):
    # Irrelevant pre-checks
    if 'MAINT_MODE' in flags and 'EMERG_BYPASS' not in flags:
        return -1
    
    # Decoy calculation using itertools
    flag_perms = list(itertools.permutations(flags, 2))
    perm_score = len([p for p in flag_perms if p[0] != p[1]])
    
    # Real signal analysis
    decay_results = []    
    for log in logs:
        result = analyze_signal_decay(log)
        decay_results.append(result)
    
    # Key metric extraction
    avg_decay = sum(decay_results) / len(decay_results) if decay_results else 0
    max_decay = max(decay_results) if decay_results else 0
    
    # Misleading intermediate blend
    phantom_index = perm_score * 0.3 + avg_decay * 1.7
    
    # Actual decisive computation
    critical_nodes = sum(1 for d in decay_results if d > 5)
    stability_ratio = (max_decay + avg_decay) / 2
    final_score = int((stability_ratio * 42.5) + (critical_nodes * 15.7))
    
    # Final diagnostic assignment (TARGET)
    final_diagnostic = final_score + 13
    
    # Unused transformation (red herring)
    reshaped_logs = [list(itertools.accumulate(log)) for log in logs]
    smoothed = [sum(rl) / len(rl) for rl in reshaped_logs if rl]
    
    return final_diagnostic

# Simulation setup
NODE_COUNT = 7
DURATION_HOURS = 8

# Generate system data
system_logs = generate_synthetic_logs(NODE_COUNT, DURATION_HOURS)

# Define operational state
operational_flags = ['A', 'C', 'E', 'ACTIVE_SYNC', 'CORE_OK']

# Execute core computation
final_diagnostic = compute_integrity_score(operational_flags, system_logs)

# Output target result
print(f"Target result: {final_diagnostic}")