from collections import defaultdict, Counter

# Simulated sensor fusion and system health analysis
def collect_telemetry():
    raw_signals = [0.85, 0.92, 1.01, 0.77, 0.63, 0.94, 1.15, 0.88]
    weights = [0.5, 1.2, 0.8, 1.0, 0.7, 1.1, 0.9, 1.3]
    weighted_sum = sum(s * w for s, w in zip(raw_signals, weights))
    normalization_factor = sum(weights)
    normalized_score = weighted_sum / normalization_factor
    
    # Irrelevant transformation (distractor)
    inverted_values = [1.0 / (1 + abs(x)) for x in raw_signals]
    entropy_proxy = sum(-v * v for v in inverted_values)
    
    return {'score': normalized_score, 'samples': len(raw_signals)}

def compute_stability_index(telemetry):
    base_score = telemetry['score']
    sample_count = telemetry['samples']
    
    # Apply non-linear correction (relevant)
    if base_score > 0.9:
        adjusted = base_score * (1.1 - 0.05 * sample_count)
    else:
        adjusted = base_score * (0.9 + 0.02 * sample_count)
    
    # Dead code path (red herring)
    if False:
        for i in range(100):
            adjusted = (adjusted + base_score) / 2
    
    # Additional irrelevant calculation
    dummy_accumulator = 0
    for i in range(sample_count):
        dummy_accumulator += (i + 1) ** 0.5
    
    return adjusted

def generate_diagnostics(stability):
    # Complex branching with misleading intermediate variables
    diagnostics = {}
    level_map = {0: 'LOW', 1: 'MEDIUM', 2: 'HIGH'}
    
    if stability > 0.95:
        diagnostics['threat'] = 2
        diagnostics['response'] = 'CRITICAL'
    elif stability > 0.85:
        diagnostics['threat'] = 1
        diagnostics['response'] = 'WARNING'
    else:
        diagnostics['threat'] = 0
        diagnostics['response'] = 'NORMAL'
    
    # Distractor block: unused statistical summary
    stats_summary = defaultdict(int)
    stats_summary['peak'] = int(stability * 100)
    stats_summary['floor'] = int(stability * 50)
    stats_summary['span'] = stats_summary['peak'] - stats_summary['floor']
    
    # Unused complex structure (decoy)
    decoy_matrix = [[i * j + stability for j in range(3)] for i in range(3)]
    
    return diagnostics

def evaluate_redunancy_pattern():
    # Irrelevant bit manipulation sequence (misleading)
    pattern = 0b101010
    for shift in range(1, 5):
        pattern ^= (pattern << shift) | (pattern >> shift)
    pattern &= 0xFFFF
    
    # This function returns nothing useful
    return None

def analyze_metrics(diag, state):
    # Core logic hidden among distractions
    threat_level = diag['threat']
    system_mode = state['mode']
    error_count = state['errors']
    
    # Real computation path
    base_value = threat_level * 1000
    
    if system_mode == 'SAFE':
        modifier = 0.5
    elif system_mode == 'MONITOR':
        modifier = 1.2
    else:
        modifier = 1.8  # Default active mode
    
    intermediate = base_value * modifier
    
    # Additional adjustment based on errors
    error_penalty = max(0, 100 - error_count * 10)
    
    result = intermediate + error_penalty
    
    # Numerous irrelevant operations below
    temp_data = [{'val': result % (i+2)} for i in range(5)]
    counter_obj = Counter([int(d['val']) for d in temp_data])
    
    # Fake recursive distraction
    def helper(n):
        if n <= 1:
            return 1
        return helper(n-1) + helper(n-2)
    
    _ = helper(5)  # Precomputed, irrelevant
    
    # Final red herring: string manipulation unrelated to result
    status_msg = "System:\t" + "OK".lower().replace('k', 'K') + "\n"
    status_msg += f"Code: {int(result)}".encode('ascii').decode('utf-8')
    
    return int(result)

# Main execution flow
telemetry_data = collect_telemetry()
stability_metric = compute_stability_index(telemetry_data)
diagnostic_report = generate_diagnostics(stability_metric)

# Simulated system state with meaningful parameters
system_state = {
    'mode': 'ACTIVE',
    'errors': 3,
    'version': '3.7.1',
    'uptime': 87430,
    'users': 12
}

# Key statement that produces the target variable
final_diagnostic = analyze_metrics(diagnostic_report, system_state)

# Execution continues with irrelevant final steps
redundant_check = evaluate_redunancy_pattern()  # Returns None
log_entry = str(final_diagnostic) + '_STATUS_' + hex(final_diagnostic ^ 0xABCD)

print(f"Result: {final_diagnostic}")