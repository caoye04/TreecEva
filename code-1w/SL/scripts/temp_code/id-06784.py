from collections import defaultdict, Counter
from itertools import cycle, islice

# System integrity diagnostic module

def analyze_event_frequency(log_stream):
    # Irrelevant frequency analysis (distractor)
    freq_map = defaultdict(int)
    for event in log_stream:
        freq_map[event] += 1
    sorted_events = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)
    return [e for e, _ in sorted_events[:3]]

def validate_checksum(sequence):
    # Unused checksum validator (dead code path)
    chk = 0
    for val in sequence:
        chk ^= val * 3
    return chk % 256

def generate_prediction_model(data_window):
    # Complex but irrelevant prediction model (red herring)
    trend_weights = [0.1, 0.3, 0.6]
    forecast = 0.0
    for i, sample in enumerate(islice(cycle(data_window), 9)):
        forecast += sample * trend_weights[i % 3]
    return round(forecast, 3)

def evaluate_stability_index(telemetry):
    # Misleading stability metric (intermediate decoy)
    base = sum(t for t in telemetry if t > 0) / len(telemetry)
    fluctuation = sum(abs(telemetry[i] - telemetry[i-1]) for i in range(1, len(telemetry)))
    return base - fluctuation * 0.01

def detect_anomalies(timestamps, thresholds):
    # Unused anomaly detection with complex logic (distractor)
    anomalies = []
    for t, thresh in zip(timestamps, cycle(thresholds)):
        if t < 0:
            continue
        if t % 7 == 0 and thresh > 50:
            anomalies.append(t * 2)
        elif t > 1000:
            anomalies.append(-t)
    return anomalies

def compute_integrity_score(flags, log_entries):
    # CORE FUNCTION: Only this matters for final answer
    status_chain = [1 if f else 0 for f in flags]
    
    # Real computation begins
    shift_register = 0
    for bit in status_chain:
        shift_register = (shift_register << 1) | bit
    
    # Log processing affects weight
    action_counter = Counter(entry.split()[0] for entry in log_entries)
    critical_count = action_counter.get('CRITICAL', 0)
    warning_count = action_counter.get('WARNING', 0)
    
    # Key formula
    raw_score = shift_register * 3 + critical_count * (-15) + warning_count * 5
    
    # Final transformation
    normalized = abs(raw_score) % 10000
    return normalized if normalized != 0 else 999

# Simulated system data
system_telemetry = [127, 89, 155, 74, 201, 66, 92, 131, 77, 104]
system_timestamps = [1623, 741, 0, 2995, 1033, -1, 888]
event_sequence = [255, 170, 85, 0, 127]

# Distractor: unused prediction
forecast_value = generate_prediction_model(system_telemetry)

# Diagnostic log with meaningful patterns
system_log = [
    'INFO System reboot initiated',
    'WARNING Memory pressure detected',
    'DEBUG Cache cleared successfully',
    'CRITICAL I/O timeout',
    'WARNING Disk latency high',
    'INFO Network reconnected',
    'CRITICAL Permission denied',
    'DEBUG Watchdog timer reset'
]

# Consistency flags derived from telemetry pattern
consistency_flags = [
    system_telemetry[i] > system_telemetry[i-1] for i in range(1, len(system_telemetry))
]
consistency_flags.append(len(system_log) % 2 == 1)  # Additional flag

# Extraneous analyses (all distractors)
_ = analyze_event_frequency([line.split()[0] for line in system_log])
_ = evaluate_stability_index(system_telemetry)
_ = detect_anomalies(system_timestamps, [45, 60, 75])
chk_val = validate_checksum(event_sequence)  # Dead code usage

# Core execution point
final_diagnostic = compute_integrity_score(consistency_flags, system_log)
print(f"Result: {final_diagnostic}")