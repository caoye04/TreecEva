from collections import defaultdict, Counter
import math

# Simulated system telemetry data
timestamps = [1623456780, 1623456789, 1623456795, 1623456802, 1623456810]
raw_signals = [0.88, 0.91, 0.77, 0.65, 0.82]
error_flags = [False, True, False, False, True]

# Irrelevant auxiliary mapping (distractor)
signal_names = {0: 'voltage', 1: 'current', 2: 'temp', 3: 'freq', 4: 'phase'}

# System state with multiple dimensions (some relevant, some not)
system_state = {
    'core_temp': 72.4,
    'fan_speed': 2200,
    'power_draw': 145.6,
    'uptime_hours': 107,
    'last_reset_cause': 'overclock',
    'security_level': 3
}

# Log entries with mixed content
log_entries = [
    {'level': 'INFO', 'event': 'startup', 'code': 200},
    {'level': 'WARN', 'event': 'high_temp', 'code': 409},
    {'level': 'ERROR', 'event': 'sensor_fail', 'code': 501},
    {'level': 'INFO', 'event': 'recovery', 'code': 200},
    {'level': 'WARN', 'event': 'fluctuation', 'code': 404}
]

# Distractor function - never called
def analyze_historical_trends(data):
    cumulative = 0
    for i in range(len(data)):
        cumulative += data[i] * (i + 1)
    return math.log(cumulative + 1) if cumulative > 0 else 0

# Helper function to count event frequency (used later)
def count_event_frequency(entries):
    counter = Counter()
    for entry in entries:
        evt = entry['event']
        counter[evt] += 1
    return counter

# Secondary helper with red herring logic
def compute_health_score(temp, errors):
    base = 100 - temp * 0.5
    penalty = sum(1 for e in errors if e) * 5
    bonus = 10 if len(errors) > 4 else 0  # misleading bonus
    return base - penalty + bonus

# Complex processing with conditional early exits
def validate_signal_integrity(signals, threshold=0.7):
    valid_count = sum(1 for s in signals if s >= threshold)
    if valid_count < 3:
        return False
    avg = sum(signals) / len(signals)
    if avg < 0.75:
        return False
    return True

# Main processing function with multiple concerns and distractors
def process_metrics(logs, state):
    # Irrelevant intermediate calculation (distractor)
    uptime_factor = state['uptime_hours'] % 24
    security_override = state['security_level'] > 2

    # Extract relevant events
    event_freq = count_event_frequency(logs)
    error_count = event_freq.get('sensor_fail', 0) + event_freq.get('high_temp', 0)

    # Compute derived metrics (some used, some not)
    info_count = event_freq.get('INFO', 0)
    warn_count = event_freq.get('WARN', 0)
    total_events = len(logs)

    # Diagnostic flag based on logs
    has_recovery = any(log['event'] == 'recovery' for log in logs)
    initial_failure = logs[0]['level'] == 'ERROR'

    # Bitwise manipulation of error codes (red herring)
    aggregated_code = 0
    for log in logs:
        aggregated_code ^= log['code']  # XOR chaining - unused later
n    # Health assessment from physical state
    raw_health = compute_health_score(state['core_temp'], error_flags)

    # Signal validation (uses global raw_signals)
    signal_ok = validate_signal_integrity(raw_signals)

    # Distractor block: temperature conversion (unused)
    temp_fahrenheit = (state['core_temp'] * 9/5) + 32
    temp_kelvin = state['core_temp'] + 273.15

    # Primary diagnostic logic chain
    diagnostic_weight = 0
    if error_count == 0:
        diagnostic_weight += 10
    elif error_count == 1:
        diagnostic_weight += 5
    else:
        diagnostic_weight -= 8

    if signal_ok:
        diagnostic_weight += 12

    if has_recovery and warn_count >= 1:
        diagnostic_weight += 7

    if state['power_draw'] > 140:
        diagnostic_weight -= 5

    # Critical dependency on event code pattern
    recent_codes = [log['code'] for log in logs[-3:]]
    if recent_codes.count(200) >= 2 and all(c != 501 for c in recent_codes):
        diagnostic_weight += 6

    # Final composite computation
    baseline = 100
    adjustment = int(diagnostic_weight * 1.5)

    final_diagnostic = baseline + adjustment

    # Dead code path (never reached due to logic above)
    if temp_fahrenheit < 100 and security_override:
        final_diagnostic = max(final_diagnostic, 120)

    return final_diagnostic

# Execution point of interest
final_diagnostic = process_metrics(log_entries, system_state)
print(f"Target result: {final_diagnostic}")