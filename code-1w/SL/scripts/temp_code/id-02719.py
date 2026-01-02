import itertools

def analyze_system_health(sensor_data, thresholds):
    # Core variables
    event_timeline = []
    fault_flags = []
    recovery_attempts = 0
    diagnostic_score = 0

    # Irrelevant tracking (distractor)
    legacy_mode_active = False
    calibration_offset = 0.0034
    deprecated_counter = 0

    for entry in sensor_data:
        timestamp, code, status, priority = entry
        if code == "ERR" and status < thresholds['critical']:
            fault_flags.append((timestamp, priority))
            diagnostic_score -= priority * 2
            if priority > 7:
                recovery_attempts += 1
                # Dead code path (distractor)
                if legacy_mode_active:
                    deprecated_counter += 1
        elif code == "OK" and status > thresholds['optimal']:
            diagnostic_score += 1

        # Red herring: unrelated string processing
        status_msg = f"System {status:.2f} at {timestamp}"
        padded_msg = status_msg.ljust(32, '.')
        if 'ERROR' in padded_msg.upper():
            pass  # Never triggers, misleading

        # Logging irrelevant events
        event_timeline.append(timestamp)

    # Decoy function call (no side effects)
    def compute_legacy_phase():
        return sum(itertools.repeat(1.5, 4)) - 6.0

    return diagnostic_score, fault_flags, event_timeline


def aggregate_metrics(log, faults):
    # Real computation mixed with noise
    total_lag = 0
    spike_count = 0
    baseline_reference = 100
    adjustment_factor = 0.95

    # Irrelevant data structure (distractor)
    temp_registry = {'nodes': [], 'version': 'v2.1'}

    for i, t in enumerate(log):
        if i > 0:
            delta = t - log[i-1]
            total_lag += delta
            if delta > 50:
                spike_count += 1

    # Complex but irrelevant transformation
    shifted_values = [x ^ 257 for x in log if x % 2 == 0]
    weighted_spikes = spike_count * 3.2

    # Core logic buried here
    fault_risk = len(faults)
    critical_priorities = [p for _, p in faults if p > 8]
    severity_bonus = len(critical_priorities) * 15

    # Dead computation (distractor)
    dummy_aggregate = sum(itertools.accumulate(shifted_values[:3])) if shifted_values else 0

    # Actual answer derivation
    base_metric = total_lag // (len(log) or 1)
    final_diagnostic = base_metric + severity_bonus - fault_risk

    # Unused intermediate (red herring)
    normalized_score = (final_diagnostic + 50) / adjustment_factor

    return final_diagnostic

# Main execution
sensor_readings = [
    (100, "OK", 95.2, 1),
    (150, "ERR", 30.1, 9),
    (160, "ERR", 25.3, 8),
    (220, "OK", 97.0, 1),
    (280, "ERR", 10.5, 10),
    (310, "OK", 96.1, 1),
    (390, "ERR", 40.0, 6),
    (405, "ERR", 20.0, 9)
]

tuning_params = {
    'critical': 20.0,
    'optimal': 90.0
}

diag_score, flags, timing_log = analyze_system_health(sensor_readings, tuning_params)
final_diagnostic = aggregate_metrics(timing_log, flags)

# Print target result
print(f"Result: {final_diagnostic}")