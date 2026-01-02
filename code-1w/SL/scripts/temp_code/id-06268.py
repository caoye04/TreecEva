from collections import defaultdict, Counter
import math

# Simulated quantum register diagnostics with decoy data structures
def initialize_quantum_registers():
    registers = [3, 7, 15, 31, 63]
    metadata = {'version': 'QX-4.2', 'active': True, 'mode': 'diagnostic'}
    audit_trail = [len(registers), sum(registers) // len(registers), 0]
    return registers, metadata, audit_trail

# Irrelevant helper for red-herring error correction
def hamming_encode(value):
    if value <= 0: return 0
    bits = bin(value).count('1')
    return value ^ (bits << 2)

# Decoy function that appears related but is never called
def calibrate_sensors(log_data):
    stats = defaultdict(int)
    for entry in log_data:
        stats['total'] += entry
        stats['squares'] += entry ** 2
    return dict(stats)

# Core diagnostic analyzer with multiple logic layers
def analyze_register_pair(x, y, mode='strict'):
    if x == 0 or y == 0:
        return 0
    
    # Compute composite signature
    sig_a = (x & y) + (x | y)  # bitwise mix
    sig_b = abs(x - y) * 2
    ratio = max(x, y) / (min(x, y) + 1e-8)
    
    # Conditional override path (rarely triggered)
    if ratio > 5 and mode == 'relaxed':
        return sig_b * 2
    
    temp_result = sig_a + sig_b
    adjustment = int(math.log(temp_result + 1, 2))
    return temp_result - adjustment

# System log processor - processes event counts
def process_system_log(raw_log):
    filtered = [x for x in raw_log if x % 2 == 1]  # keep odd values only
    count_map = Counter(filtered)
    total_events = sum(count_map.values())
    unique_events = len(count_map)
    
    # Dummy aggregation with irrelevant metrics
    entropy = 0.0
    for count in count_map.values():
        prob = count / total_events
        entropy -= prob * math.log(prob + 1e-9, 2)
    
    summary = {
        'score': total_events * unique_events,
        'peak': max(filtered) if filtered else 0,
        'baseline': sum(filtered) // (len(filtered) or 1)
    }
    return summary, entropy  # entropy unused later

# Main analysis pipeline with conditional branching
def analyze_system_state(registers, log_entries):
    # Initialize tracking variables (some are distractions)
    diagnostics = []
    debug_flags = [False, True, False]
    accumulator = 0
    temporal_weight = 0.0

    # Process log first to generate baseline
    log_summary, _ = process_system_log(log_entries)
    base_score = log_summary['score']
    
    # Analyze pairs of quantum registers
    for i in range(len(registers) - 1):
        reg_a = registers[i]
        reg_b = registers[i + 1]
        
        # Apply transformation that mimics calibration
        transformed_a = reg_a ^ (reg_a >> 2)
        transformed_b = reg_b + (reg_b & 7)
        
        # Real computation path
        pair_diag = analyze_register_pair(transformed_a, transformed_b, mode='strict')
        diagnostics.append(pair_diag)
        
        # Dead code path - debug only
        if debug_flags[i % len(debug_flags)]:
            temp_var = (transformed_a + transformed_b) ** 0.5
            accumulator += int(temp_var)

    # Aggregate real results
    if diagnostics:
        raw_total = sum(diagnostics)
        penalty = len([d for d in diagnostics if d < 50])
        adjusted_total = raw_total - (penalty * 5)
        
        # Final adjustment using log baseline
        final_component = adjusted_total * (base_score // 10 + 1)
        temporal_weight = math.sin(math.pi / (base_score % 10 + 1))
    else:
        final_component = 0
        temporal_weight = 0.0

    # Critical result calculation
    final_diagnostic = int(final_component * (1 + temporal_weight))
    
    # Distractor assignment - looks important but unused
    system_verdict = 'STABLE' if final_diagnostic > 1000 else 'MONITORING'
    confidence_interval = [final_diagnostic - 10, final_diagnostic, final_diagnostic + 15]
    
    return final_diagnostic

# Setup test data
quantum_registers, sys_meta, trail = initialize_quantum_registers()
system_log = [5, 12, 7, 8, 9, 10, 11, 14, 15, 3, 6, 13]

# Execute main analysis
diagnostic_trace = sum(quantum_registers) * len(system_log)  # Red herring computation

final_diagnostic = analyze_system_state(quantum_registers, system_log)

# Output target result
Target result: {final_diagnostic}