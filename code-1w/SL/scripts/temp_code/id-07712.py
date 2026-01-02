from collections import defaultdict, Counter
import math

# Simulated quantum register diagnostics with noise filtering
def initialize_registers(size):
    reg = {}
    for i in range(size):
        reg[f'q{i}'] = (i % 2 == 0, {'phase': 0.5 * i, 'coherence': 1.0 / (1 + i)})
    return reg

def apply_correction_pass(registers):
    corrections = 0
    temp_snapshot = []
    for k, (state, meta) in registers.items():
        if meta['coherence'] < 0.3:
            meta['corrected'] = True
            corrections += 1
            temp_snapshot.append(k)
        else:
            meta['corrected'] = False
    # Irrelevant snapshot logging
    log_entry = f"Corrected {corrections} registers: {', '.join(temp_snapshot)}"
    return corrections

def compute_entropy(registers):
    entropy = 0.0
    for _, (state, meta) in registers.items():
        c = meta['coherence']
        if c > 0:
            entropy -= c * math.log(c)
    return round(entropy, 6)

def flag_anomalies(registers):
    anomaly_flags = []
    phase_sum = 0.0
    for idx, (k, (state, meta)) in enumerate(registers.items()):
        if meta.get('corrected', False):
            phase_sum += meta['phase']
            if phase_sum > 5.0:
                anomaly_flags.append(f'anomaly_q{idx}')
                phase_sum = 0  # Reset
    # Dead path: this list is never used downstream
    if len(anomaly_flags) > 3:
        backup_mode = True
        fallback_threshold = 0.45
        for k in registers:
            pass  # Placeholder loop, no effect
    return len(anomaly_flags)

def build_diagnostic_summary(registers, errors):
    summary = defaultdict(int)
    state_count = Counter()
    
    for k, (state, meta) in registers.items():
        state_count[state] += 1
        summary['total'] += 1
        if meta['coherence'] < 0.25:
            summary['low_coherence'] += 1
    
    # Distractor computation: unrelated statistical moment
    moments = []
    for v in state_count.values():
        moments.append(v ** 3 - v * 2)  # Cubic deviation - unused
    
    summary['ratio'] = summary['low_coherence'] / summary['total'] if summary['total'] else 0
    return dict(summary)

def analyze_system_state(registers, error_log):
    # Key analysis pipeline
    entropy = compute_entropy(registers)
    correction_count = apply_correction_pass(registers)
    anomalies = flag_anomalies(registers)
    
    # Distractor: parse error log even though it's synthetic
    error_stats = defaultdict(int)
    for e in error_log:
        parts = e.split(':')
        if len(parts) > 1:
            error_stats[parts[0]] += 1
    ignored_metric = sum(error_stats.values()) * 0.1  # Not used
    
    # Main diagnostic score calculation
    base_score = 100.0
    base_score -= correction_count * 7.5
    base_score -= anomalies * 12.2
    base_score += entropy * 3.8
    
    # Conditional adjustment based on hidden threshold
    summary = build_diagnostic_summary(registers, error_log)
    if summary['ratio'] > 0.3:
        base_score -= 20.0  # Penalty
    else:
        base_score += 5.0  # Stability bonus
    
    # Final transformation
    final_score = int(round(base_score * 2.3))
    
    # Critical red herring: two similarly named variables
    final_diagnostic = final_score + 1000  # Actual target
    final_diagnostig = final_score + 2000  # Typo-named decoy
    
    return final_diagnostic

# Setup and execution
quantum_registers = initialize_registers(12)
error_log = [
    'ECC:multi_bit_flip',
    'PHY:thermal_decay',
    'ECC:parity_mismatch',
    'CTR:timing_jitter'
]

# Execution point of interest
correction_count = apply_correction_pass(quantum_registers)
anomaly_count = flag_anomalies(quantum_registers)
entropy_value = compute_entropy(quantum_registers)

# Key statement
final_diagnostic = analyze_system_state(quantum_registers, error_log)

print(f"Result: {final_diagnostic}")