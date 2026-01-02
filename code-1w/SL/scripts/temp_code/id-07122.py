def process_telemetry(data_stream, thresholds):
    base_offset = 1024
    temp_buffer = []
    rolling_checksum = 0
    mode_flag = False

    for index, (timestamp, value, sensor_id) in enumerate(data_stream):
        if value > thresholds['critical']:
            rolling_checksum ^= index + sensor_id
            temp_buffer.append(value * 0.85)
        elif value > thresholds['warning']:
            temp_buffer.append(value * 0.95)
            if index % 3 == 0:
                mode_flag = not mode_flag
        else:
            temp_buffer.append(value)

        # Irrelevant accumulation (red herring)
        base_offset += len(str(timestamp))

    # Dead code path - never executed due to logic above
    if len(temp_buffer) == 0 and mode_flag:
        return sum(rolling_checksum for _ in range(3))

    return [x for x in temp_buffer if x > 0], rolling_checksum


def validate_sequence(signal_chain):
    # Misleading function with no real impact
    cumulative = 0
    for s in signal_chain:
        cumulative += s % 7
    return cumulative > 100


def decode_payload(raw_packets):
    # Unused decoy function
    return [sum(p) * 0.1 for p in raw_packets if sum(p) > 50]

# Simulated telemetry data (sensor readings over time)
data_log = [
    (1678886400, 120, 1),
    (1678886401, 250, 2),
    (1678886402, 80, 3),
    (1678886403, 300, 1),
    (1678886404, 90, 2),
    (1678886405, 400, 3),
    (1678886406, 70, 1)
]

system_thresholds = {
    'warning': 100,
    'critical': 200,
    'base': 50
}

# Extraneous data structure with misleading relevance
auxiliary_signals = [55, 60, 210, 65, 70]

# Unused packet simulation (distractor)
packet_queue = [[10, 20], [30, 40, 50], [60, 70, 80]]

# Process main data stream
filtered_data, checksum = process_telemetry(data_log, system_thresholds)

# Secondary processing with tuple unpacking and zip (relevant)
scaled_readings = [v * 1.1 for v in filtered_data]
analysis_pairs = list(zip(filtered_data, scaled_readings))

# Compute diagnostic metrics with conditional expression and enumeration
metric_trace = []
for i, (orig, scaled) in enumerate(analysis_pairs):
    deviation = scaled - orig
    # Conditional expression used idiomatically
    status = 'amplified' if deviation > 10 else 'stable'
    metric_trace.append({'step': i, 'delta': deviation, 'status': status})

# Aggregation function with distractors
def aggregate_metrics(entries, flags):
    total_impact = 0
    volatility_index = 0
    baseline_shift = 1.0

    # Redundant flag processing (misleading)
    if 'override' in flags:
        baseline_shift *= 1.5

    # Core calculation
    for entry in entries:
        total_impact += entry[1] - entry[0]

    # Complex but irrelevant transformation chain
    temp_series = [e['delta'] for e in metric_trace]
    for idx, val in enumerate(temp_series):
        if idx % 2 == 0:
            volatility_index += val ** 2
        else:
            volatility_index -= val / 2

    # Final result combines relevant and misleading elements
    # BUT only total_impact is actually derived from correct propagation
    final_score = int(total_impact + volatility_index * 0.01)

    # Decoy assignments
    debug_snapshot = {'volatility': volatility_index, 'base': baseline_shift}
    audit_trail = [f"Step {i}" for i in range(len(metric_trace))]

    return final_score

# Unused validation call (dead path)
validate_sequence(auxiliary_signals)

# Key execution point
log_entries = analysis_pairs
system_flags = {'mode': 'standard'}
final_diagnostic = aggregate_metrics(log_entries, system_flags)

print(f"Target result: {final_diagnostic}")