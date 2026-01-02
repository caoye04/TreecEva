def process_telemetry(data_stream, thresholds):
    cumulative_score = 0
    anomaly_count = 0
    temp_buffer = []
    baseline = sum(thresholds) / len(thresholds)
    decay_factor = 0.85

    for index, (timestamp, reading, status) in enumerate(data_stream):
        if status == "OFFLINE":
            continue
        adjusted_reading = reading * (decay_factor ** index)
        temp_buffer.append(adjusted_reading)

        if adjusted_reading > thresholds[index % len(thresholds)]:
            anomaly_count += 1

    if len(temp_buffer) == 0:
        return 0

    cumulative_score = sum(temp_buffer) / len(temp_buffer)
    return cumulative_score if cumulative_score >= baseline else baseline


def compute_stability_index(events, window_size=3):
    if len(events) < window_size:
        return -1

    peaks = 0
    for i in range(1, len(events) - 1):
        if events[i-1] < events[i] > events[i+1]:
            peaks += 1
    return peaks


def validate_checksum(sequence):
    # Irrelevant validation function — red herring
    return sum(sequence) % 256


def decode_payload(payload):
    # Decoy function: looks important but unused in critical path
    decoded = []
    shift = payload[0] % 7
    for val in payload:
        decoded.append((val << shift) ^ 0xA5)
    return decoded


def analyze_phase_shift(samples):
    # Misleading intermediate calculation
    total_shift = 0
    for i in range(1, len(samples)):
        total_shift += abs(samples[i] - samples[i-1])
    return total_shift / len(samples) if samples else 0


def aggregate_metrics(log_entries, system_flags):
    base_metrics = []
    debug_flag = system_flags.get('debug_mode', False)
    safety_engaged = system_flags.get('safe_op', True)
    
    irrelevant_thresholds = [92, 88, 76, 94, 85]
    dummy_stream = [(t, (t*17)%101, "ACTIVE") for t in range(len(log_entries))]
    
    # Dead code path — never executed due to flag value
    if debug_flag and not safety_engaged:
        fallback_data = [x["value"] * 0.9 for x in log_entries if x["type"] == "SENSOR"]
        return sum(fallback_data)

    # Real processing begins
    filtered_logs = [entry for entry in log_entries if entry["active"] and entry["source"] != "SIMULATED"]

    # Compute primary metric using conditional expression and zip
    scores = [
        (log["value"] * 1.1) if log["quality"] > 0.7 else (log["value"] * 0.85)
        for log in filtered_logs
    ]

    # Use enumerate and zip together — required python idiom
    trend_offsets = []
    for i, (score, log) in enumerate(zip(scores, filtered_logs)):
        offset = score - (log["baseline"] * (1 + i * 0.01))
        trend_offsets.append(offset)

    avg_offset = sum(trend_offsets) / len(trend_offsets) if trend_offsets else 0

    # Secondary metric with decoy function call (no side effects)
    sample_sequence = [int(s["value"]) for s in filtered_logs[:8]]
    _ = analyze_phase_shift(sample_sequence)  # Result ignored
    _ = validate_checksum(sample_sequence)     # Another ignored check

    # Conditional logic determining final output
    if avg_offset > 5:
        base_adjustment = 23.7
    elif avg_offset < -5:
        base_adjustment = -18.4
    else:
        base_adjustment = 42.1

    stability_logs = [int(x["value"]) for x in filtered_logs if x["type"] == "CONTROL"]
    stability_index = compute_stability_index(stability_logs)

    # Final composition
    final_diagnostic = int(
        base_adjustment * 100 + 
        len(filtered_logs) * 7 - 
        abs(int(avg_offset)) * 3 + 
        (stability_index if stability_index > 0 else 0) * 5
    )

    # Additional distraction: recursive-looking but actually not used
    def internal_audit():
        return sum([len(str(x)) for x in sample_sequence])

    return final_diagnostic

# Main execution
log_data = [
    {"value": 89,  "baseline": 85, "quality": 0.85, "type": "SENSOR", "active": True, "source": "REAL"},
    {"value": 76,  "baseline": 78, "quality": 0.65, "type": "SENSOR", "active": True, "source": "REAL"},
    {"value": 94,  "baseline": 90, "quality": 0.92, "type": "CONTROL","active": True, "source": "REAL"},
    {"value": 67,  "baseline": 70, "quality": 0.55, "type": "SENSOR", "active": False,"source": "REAL"},
    {"value": 102, "baseline": 98, "quality": 0.95, "type": "CONTROL","active": True, "source": "REAL"},
    {"value": 83,  "baseline": 80, "quality": 0.71, "type": "SENSOR", "active": True, "source": "SIMULATED"},
    {"value": 91,  "baseline": 87, "quality": 0.88, "type": "CONTROL","active": True, "source": "REAL"}
]

flags = {
    "debug_mode": False,
    "safe_op": True,
    "override_safety": False,
    "enable_tracing": True
}

# Key execution point
final_diagnostic = aggregate_metrics(log_entries=log_data, system_flags=flags)
print(f"Target result: {final_diagnostic}")