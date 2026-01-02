import math

def analyze_signal_strength(signal, noise):
    # Irrelevant helper function (dead code path)
    return (signal - noise) ** 2

def deprecated_checksum(data):
    # Unused legacy function (distractor)
    return sum(data) % 256

def main():
    # System telemetry simulation with mixed signal and status data
    raw_samples = [127, 83, 91, 115, 74, 102]
    calibration_offset = 17
    adjusted_values = [x + calibration_offset for x in raw_samples]

    # Simulated log entries with metadata (some fields are decoys)
    log_entries = [
        {'timestamp': 1001, 'power': 45.2, 'temp': 67, 'status': 'OK', 'aux': 3},
        {'timestamp': 1002, 'power': 48.7, 'temp': 70, 'status': 'WARN', 'aux': 1},
        {'timestamp': 1003, 'power': 52.1, 'temp': 75, 'status': 'WARN', 'aux': 4},
        {'timestamp': 1004, 'power': 55.3, 'temp': 82, 'status': 'ALERT', 'aux': 0},
        {'timestamp': 1005, 'power': 49.8, 'temp': 71, 'status': 'OK', 'aux': 2}
    ]

    # Irrelevant frequency analysis (red herring)
    sample_rate = 44100
    nyquist_window = [math.sin(2 * math.pi * 440 * i / sample_rate) for i in range(10)]
    avg_nyquist = sum(nyquist_window) / len(nyquist_window)

    # Real threshold logic embedded in noise
    system_thresholds = {
        'power_high': 50.0,
        'temp_critical': 80,
        'decay_factor': 0.88,
        'baseline': 40.0
    }

    # Misleading intermediate calculation (decoy metric)
    cumulative_risk = 0
    for entry in log_entries:
        if entry['status'] == 'ALERT':
            cumulative_risk += 20
        elif entry['status'] == 'WARN':
            cumulative_risk += 5

    # Hidden correction factor based on modular pattern in aux values
    aux_pattern_sum = sum(entry['aux'] for entry in log_entries)  # 10
    correction_multiplier = (aux_pattern_sum % 7) / 10.0  # 3/10 = 0.3

    # Core processing logic wrapped in lambda and conditional expression
    validate_entry = lambda e: e['power'] > system_thresholds['power_high'] and e['temp'] >= system_thresholds['temp_critical']

    def process_metrics(entries, thresholds):
        count_critical = 0
        total_deviation = 0.0
        recent_alert_power = []

        for e in entries:
            # Conditional expression used idiomatically
            deviation = (e['power'] - thresholds['baseline']) if e['power'] > thresholds['baseline'] else 0
            total_deviation += deviation

            if validate_entry(e):
                count_critical += 1
                recent_alert_power.append(e['power'])

        # Real computation path: weighted diagnostic score
        base_score = count_critical * 100
        adjustment = total_deviation * correction_multiplier  # Uses outer scope variable
        decayed_adjustment = adjustment * thresholds['decay_factor']

        # Final result built from multiple reasoning steps
        final_score = base_score + decayed_adjustment

        # Dead code below (never executed but looks important)
        if False:
            fallback = sum(recent_alert_power) / len(recent_alert_power) if recent_alert_power else 0
            final_score = max(final_score, fallback * 10)

        return int(round(final_score))

    # Key execution point
    final_diagnostic = process_metrics(log_entries, system_thresholds)

    # Print required output
    print(f"Target result: {final_diagnostic}")

    # Unused variables to increase interference (distractors)
    entropy_estimate = math.log(len(raw_samples) * 100 + 1)
    peak_sample = max(adjusted_values)
    system_age_years = 6
    deprecated_checksum([calibration_offset, peak_sample])

if __name__ == '__main__':
    main()