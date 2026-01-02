from collections import defaultdict, Counter
import math

# Simulated quantum register diagnostics with decoy computations
def preprocess_register(reg):
    processed = []
    for val in reg:
        if val % 3 == 0:
            processed.append((val ** 2) % 7)
        elif val % 5 == 0:
            processed.append(int(math.sqrt(abs(val))) % 7)
    return processed

def validate_coherence(sequence):
    # Irrelevant validation function (dead code path)
    return all(seq > 0 for seq in sequence)

def compute_entropy(arr):
    counts = Counter(arr)
    total = len(arr)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 6)

def shift_registry(reg, offset):
    # Unused shift operation (red herring)
    return [(x + offset) % 8 for x in reg]

def filter_anomalies(logs):
    # Real but indirect preprocessing step
    anomalies = []
    for entry in logs:
        if entry['severity'] > 2 and 'ERR' in entry['code']:
            anomalies.append(entry['flag'])
    return anomalies

def accumulate_diagnostics(registers):
    accum = defaultdict(int)
    for i, reg in enumerate(registers):
        for j, val in enumerate(reg):
            key = (i % 3, j % 2)
            accum[key] += (val * (j + 1)) % 5
    return dict(accum)

def analyze_system_state(qregs, logs):
    # Key function: computes final diagnostic score
    
    # Distractor: irrelevant entropy computation on first register
    _entropy = compute_entropy(qregs[0])
    
    # Real data flow begins here
    processed_regs = [preprocess_register(reg) for reg in qregs]
    
    # Another red herring: shift registry with no effect
    shifted_regs = [shift_registry(reg, 3) for reg in qregs]
    
    # Accumulate meaningful diagnostics from original structure
    acc_diag = accumulate_diagnostics(qregs)
    
    # Extract values to form base signal
    signal_values = [v for k, v in acc_diag.items() if k[0] != 2]
    base_signal = sum(signal_values) * 3
    
    # Process logs for anomaly flags (real dependency)
    anomaly_flags = filter_anomalies(logs)
    flag_correction = sum(anomaly_flags) if anomaly_flags else -15
    
    # Decoy calculation: uses processed_regs but not in final path
    decoy_sum = sum(sum(pr) for pr in processed_regs) % 11
    
    # Critical intermediate: hidden in list comprehension
    adjustments = [\n        (base_signal + i) % 17 for i in range(len(anomaly_flags))
    ]
    adjustment_factor = adjustments[-1] if adjustments else 44
    
    # Final computation with modular arithmetic
    raw_diagnostic = (base_signal + flag_correction * 2) % 1000
    final_diagnostic = (raw_diagnostic ^ adjustment_factor) & 511
    
    # Dead return branch (misleading)
    if final_diagnostic < 0:
        return -final_diagnostic
    
    return final_diagnostic

# Simulated input data
quantum_registers = [
    [9, 15, 21, 30],
    [6, 12, 18, 24],
    [3, 8, 14, 16]
]

system_logs = [
    {'timestamp': 1001, 'code': 'ERR_7', 'severity': 3, 'flag': 7},
    {'timestamp': 1002, 'code': 'WARN_2', 'severity': 1, 'flag': 2},
    {'timestamp': 1003, 'code': 'ERR_5', 'severity': 4, 'flag': 5},
    {'timestamp': 1004, 'code': 'INFO_1', 'severity': 0, 'flag': 1}
]

# Execution point of interest
final_diagnostic = analyze_system_state(quantum_registers, system_logs)
print(f"Target result: {final_diagnostic}")