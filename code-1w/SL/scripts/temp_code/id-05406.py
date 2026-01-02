import math

# Simulated system telemetry data with mixed signal types
def generate_telemetry():
    raw_signals = [i * 1.5 + math.sin(i) for i in range(20)]
    timestamps = [1623456000 + t * 60 for t in range(20)]
    statuses = ['OK', 'WARN', 'ERROR'] * 7
    return list(zip(timestamps, raw_signals, statuses))

# Irrelevant helper: converts timestamp to readable format (not used in main logic)
def format_time(ts):
    hours = (ts // 3600) % 24
    mins = (ts // 60) % 60
    return f'{hours:02d}:{mins:02d}'

# Signal smoothing using moving average (partially relevant)
def smooth_signal(signal_list, window=3):
    smoothed = []
    for i in range(len(signal_list)):
        start = max(0, i - window + 1)
        end = min(len(signal_list), i + 1)
        window_avg = sum(signal_list[start:end]) / (end - start)
        smoothed.append(round(window_avg, 3))
    return smoothed

# Legacy checksum calculator (red herring - not used)
def compute_legacy_checksum(data):
    checksum = 0
    for item in str(data):
        checksum ^= ord(item)
    return checksum % 256

# Core pattern analyzer with decoy branches and distractions
def analyze_pattern(entries, flags):
    signal_values = [entry[1] for entry in entries]
    status_log = [entry[2] for entry in entries]
    
    # Distractor: count status occurrences (not directly used)
    status_count = {s: status_log.count(s) for s in set(status_log)}
    warning_count = status_count.get('WARN', 0) * 2
    error_penalty = len([s for s in status_log if s == 'ERROR']) * 5

    # Actual processing path begins
    filtered_signals = [v for v in signal_values if abs(v) > 1.0]  # Only significant signals
    if len(filtered_signals) == 0:
        filtered_signals = [0.0]
    
    # Apply smoothing (relevant)
    processed_signal = smooth_signal(filtered_signals)
    
    # Decoy conditional based on flag length (misleading)
    adjustment_factor = 1.0
    if len(flags) > 3:
        adjustment_factor = 0.9
    elif 'CRITICAL' in flags:
        adjustment_factor = 1.2  # Not triggered
    else:
        adjustment_factor = 1.1  # This actually applies

    # Real computation: variance of processed signal
    mean_val = sum(processed_signal) / len(processed_signal)
    variance = sum((x - mean_val) ** 2 for x in processed_signal) / len(processed_signal)
    
    # Additional red herring: unused transformation
    def transform(x):
        return (x ** 2 + 1) / (x + 0.1) if x != 0 else 10
    transformed_var = sum(transform(x) for x in processed_signal[:5])  # Computed but unused

    # Final diagnostic score calculation
    stability_index = 100 * math.exp(-variance / 10)
    final_diagnostic = int(stability_index * adjustment_factor)  # Key assignment point
    
    # Dead code branch (never reached due to structure)
    if False and variance < 0:
        final_diagnostic = -1
    
    return final_diagnostic

# Misleading data initialization (some fields unused)
system_flags = ['ACTIVE', 'MONITORING', 'REDUNDANT']
log_entries = generate_telemetry()

# Unused legacy validation (distractor)
def validate_entry(entry):
    ts, sig, stat = entry
    return stat in ['OK', 'WARN', 'ERROR'] and isinstance(sig, float)

# Background task that logs nothing (dead code path)
for entry in log_entries:
    if entry[2] == 'FATAL':  # Never occurs
        print("Critical failure detected")

# Main execution flow
final_diagnostic = 0
final_diagnostic = analyze_pattern(log_entries, system_flags)
print(f"Result: {final_diagnostic}")