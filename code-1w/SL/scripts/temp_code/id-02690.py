def analyze_component_integrity(raw_data, threshold=0.75):
    """Irrelevant auxiliary function for data validation (dead code path)."""
    if not raw_data:
        return False
    avg = sum(raw_data) / len(raw_data)
    return avg > threshold

# Distractor: Unused complex structure
class DiagnosticTrace:
    def __init__(self, timestamp, level, message):
        self.timestamp = timestamp
        self.level = level
        self.message = message

    def format_entry(self):
        return f'[{self.timestamp}] {self.level}: {self.message}'

# Misleading intermediate computation (no impact on final result)
diagnostic_chain = [
    DiagnosticTrace(1001, 'INFO', 'System nominal'),
    DiagnosticTrace(1003, 'WARN', 'Fluctuation detected'),
    DiagnosticTrace(1005, 'INFO', 'Stabilized')
]

log_summary = ''.join([entry.format_entry() for entry in diagnostic_chain])
summary_hash = sum(ord(c) for c in log_summary) % 1000  # Red herring

# Real input data disguised among noise
baseline_readings = [0.88, 0.91, 0.76, 0.85, 0.99, 0.67, 0.83]
outlier_mask = [abs(x - 0.85) > 0.1 for x in baseline_readings]
filtered_readings = [x for x, mask in zip(baseline_readings, outlier_mask) if not mask]

# Irrelevant string processing with slicing and enumeration
status_messages = ['CALIBRATION_OK', 'SENSOR_STABLE', 'FLOW_NORMAL', 'PRESSURE_HIGH']
enumerated_diagnostics = []
for i, msg in enumerate(status_messages):
    sliced = msg[5:10]  # Extracts 'BRATI', 'NSOR_', etc.
    reversed_part = sliced[::-1]
    enumerated_diagnostics.append(f'{i}_{reversed_part}')

diagnostic_token = ''.join([d[0] for d in enumerated_diagnostics])  # Another red herring

# Key boolean flags (some are decoys)
system_locked = False
override_enabled = True
calibration_valid = True
pressure_critical = False

# Performance log with tuple structure
performance_log = [
    (1, 'read', 45, True),
    (2, 'write', 120, False),
    (3, 'read', 67, True),
    (4, 'compute', 203, True),
    (5, 'read', 58, False)
]

# Quality flags using bit manipulation as distraction
quality_flags = 0
for i, (_, op, cycles, success) in enumerate(performance_log):
    if success and cycles > 50:
        quality_flags |= (1 << i)  # Set bit if successful and high cycle
    elif op == 'compute':
        quality_flags &= ~(1 << i)  # Clear bit for compute (overridden later)

# Decoy bit check
if quality_flags & (1 << 2) and not (quality_flags & (1 << 4)):
    system_locked = True

# Actual logic hidden in seemingly secondary operation
def evaluate_throughput(log):
    total_ops = 0
    total_latency = 0
    for seq, op_type, latency, success_flag in log:
        if op_type == 'read' and success_flag:
            total_ops += 1
            total_latency += latency
    return total_latency / total_ops if total_ops else 0

# Secondary metric used in final calculation
effective_latency = evaluate_throughput(performance_log)

# Hidden control flow with short-circuiting
latency_factor = (effective_latency < 60) or (not pressure_critical and override_enabled)

# Core transformation involving slicing and zip
recent = filtered_readings[-3:]  # Take last three valid readings
reference = filtered_readings[-4:-1]  # Offset reference
improvement_trend = all(curr > prev for curr, prev in zip(recent, reference))

trend_factor = 1.1 if improvement_trend else 0.9

# Final processing function (only this matters)
def process_metrics(flags, log):
    # Extract read counts
    reads_completed = sum(1 for _, op, _, success in log if op == 'read' and success)
    
    # Compute score from bit count in flags
    flag_count = bin(flags).count('1')
    
    # Combine with latency (this is where effective_latency is actually used)
    base_score = reads_completed * 100
    adjustment = int(effective_latency / 10)  # Each 10 units reduces score
    trend_bonus = int(flag_count * 2.5)  # Bonus per active flag
    
    return base_score - adjustment + trend_bonus

# Critical execution point
final_score = process_metrics(quality_flags, performance_log)
print(f'Result: {final_score}')