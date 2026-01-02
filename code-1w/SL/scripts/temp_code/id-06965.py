from collections import defaultdict, Counter
import math

# Simulated quantum register diagnostics with noise filtering
def initialize_registers(size=8):
    registers = [0] * size
    for i in range(size):
        if i % 2 == 0:
            registers[i] = (i ** 2) ^ 5
        else:
            registers[i] = (i * 3) | 7
    return registers

# Irrelevant helper: simulates thermal decay (not used in final result)
def apply_thermal_decay(regs, factor=0.95):
    return [int(r * factor) for r in regs]

# Decoy function: looks important but unused in critical path
def compute_entropy(data):
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

# Misleading transformation chain
def transform_legacy_protocol(data):
    transformed = []
    for d in data:
        temp_val = (d + 13) * 2
        temp_val ^= 0xA5
        if temp_val > 100:
            temp_val = temp_val // 3
        transformed.append(temp_val)
    return transformed

# Core diagnostic logic
def filter_anomalies(registers):
    anomalies = []
    for idx, val in enumerate(registers):
        if val & 1:  # odd values are unstable
            anomalies.append(idx)
    return anomalies

def calculate_coherence_score(registers, anomalies):
    base_score = sum(registers)
    penalty = len(anomalies) * 17
    return base_score - penalty

# Real-time log analyzer (partially relevant)
def parse_system_log(log_entries):
    severity_map = defaultdict(int)
    for entry in log_entries:
        level = entry.get('level', 'INFO')
        severity_map[level] += 1
    return severity_map

# Critical analysis function
def analyze_stability_factors(registers):
    factor = 1
    for r in registers:
        if r % 4 == 0:
            factor *= 2
        elif r % 3 == 0:
            factor += 1
    return factor

# Unused checksum generator (red herring)
def generate_checksum(data):
    chk = 0
    for item in data:
        chk = (chk + item) * 31 % 997
    return chk

# Main analysis pipeline
def analyze_system_state(registers, log):
    # Step 1: Filter hardware-level anomalies
    unstable_indices = filter_anomalies(registers)
    
    # Step 2: Calculate physical coherence
    coherence = calculate_coherence_score(registers, unstable_indices)
    
    # Step 3: Parse operational logs
    log_severity = parse_system_log(log)
    warning_count = log_severity['WARN'] + log_severity['ERROR']
    
    # Step 4: Compute stability multiplier
    stability_factor = analyze_stability_factors(registers)
    
    # Step 5: Apply environmental adjustments
    env_adjustment = 1.0
    if warning_count > 0:
        env_adjustment = 0.9 - (warning_count * 0.05)
    
    # Step 6: Combine into diagnostic metric
    raw_diagnostic = (coherence * stability_factor)
    adjusted_diagnostic = int(raw_diagnostic * env_adjustment)
    
    # Step 7: Final normalization with bit manipulation
    normalized = (adjusted_diagnostic ^ 0xFF) & 0xFFFF
    if normalized > 32767:
        normalized -= 65536
    
    # Critical assignment point
    final_diagnostic = normalized
    
    # === DISTRACTOR BLOCK ===
    # Simulate legacy compatibility layer (dead code)
    legacy_data = transform_legacy_protocol(registers)
    legacy_checksum = generate_checksum(legacy_data)
    
    # Simulate entropy measurement (unused)
    entropy_score = compute_entropy(registers)
    
    # Simulate decayed state (irrelevant)
    decayed_registers = apply_thermal_decay(registers)
    # ======================
    
    return final_diagnostic

# Setup: quantum register initialization
quantum_registers = initialize_registers(8)

# Simulated system log with mixed severity (only WARN/ERROR matter)
system_log = [
    {'event': 'power_cycle', 'level': 'INFO'},
    {'event': 'register_drift', 'level': 'WARN'},
    {'event': 'timing_skew', 'level': 'WARN'},
    {'event': 'sync_acquired', 'level': 'INFO'},
    {'event': 'voltage_spike', 'level': 'ERROR'},
    {'event': 'resync_complete', 'level': 'INFO'}
]

# Execute critical analysis
final_diagnostic = analyze_system_state(quantum_registers, system_log)

# Output target result
print(f"Target result: {final_diagnostic}")