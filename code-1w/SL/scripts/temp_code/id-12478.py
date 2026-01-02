from itertools import cycle, islice

# Simulated IoT device health monitoring system with red herrings
def analyze_device_stream(log_entries):
    # Irrelevant transformation: counts characters in timestamps (decoy)
    timestamp_chars = sum(len(entry['timestamp']) for entry in log_entries if '2023' in entry['timestamp'])

    # Misleading score based on error count (not actually used in final result)
    error_frequency_score = len([e for e in log_entries if e['level'] == 'ERROR']) * 10

    # Core diagnostic variables
    base_health = 500
    critical_failures = 0
    warning_count = 0
    transmission_gaps = 0

    # Simulate packet stream analysis
    expected_sequence = cycle(range(1, 6))
    last_seq = 0

    for entry in log_entries:
        log_type = entry['type']
        seq_num = entry.get('sequence', 0)

        # Track gaps in transmission (relevant)
        if seq_num != next(expected_sequence) and last_seq != 0:
            transmission_gaps += 1
        last_seq = seq_num

        # Count warnings and failures (relevant)
        if log_type == 'DIAGNOSTIC':
            if 'critical' in entry['message'].lower():
                critical_failures += 1
            elif 'warning' in entry['message'].lower():
                warning_count += 1

        # Dead code path - never executed due to data structure
        if 'payload_size' in entry and entry['payload_size'] > 1024:
            pass  # Placeholder for future QoS analysis

    # Distractor: complex string manipulation with no impact
    lambda_mask = lambda s: ''.join(islice(cycle(s), 10))
    masked_id = lambda_mask('DEV456')
    id_checksum = sum(ord(c) for c in masked_id[:8]) % 17

    # Irrelevant statistical calculation
    avg_char_length = sum(len(e['message']) for e in log_entries) / len(log_entries) if log_entries else 0

    # Real computation chain begins
    gap_penalty = transmission_gaps * 15
    failure_penalty = critical_failures * 120
    warning_discount = warning_count * 5

    aggregate_health_score = base_health - gap_penalty - failure_penalty + warning_discount

    # Anomaly detection using bitwise decoy (only one affects result)
    status_flags = 0
    for entry in log_entries:
        if 'corrupted' in entry['message']:
            status_flags |= 0x01
        if 'timeout' in entry['message']:
            status_flags ^= 0x04  # This flips bit 2
        if 'retry' in entry['message']:
            status_flags &= ~0x02

    # Only this flag matters in final penalty
    anomaly_penalty = 42 if (status_flags & 0x04) else 0  # Depends only on bit 2

    # Unused health variants (distractors)
    predicted_health_next = aggregate_health_score * 0.95
    health_variance = abs(base_health - aggregate_health_score) / base_health

    # Key statement
    final_diagnostic = aggregate_health_score + anomaly_penalty

    # Print required output
    print(f"Result: {final_diagnostic}")

    return final_diagnostic

# Simulated input data with realistic structure
logs = [
    {'timestamp': '2023-04-05T10:01:05Z', 'level': 'INFO', 'type': 'DIAGNOSTIC', 'message': 'System nominal', 'sequence': 1},
    {'timestamp': '2023-04-05T10:01:07Z', 'level': 'WARNING', 'type': 'DIAGNOSTIC', 'message': 'Voltage warning', 'sequence': 3},
    {'timestamp': '2023-04-05T10:01:09Z', 'level': 'ERROR', 'type': 'DIAGNOSTIC', 'message': 'critical: sensor overload', 'sequence': 4},
    {'timestamp': '2023-04-05T10:01:11Z', 'level': 'INFO', 'type': 'DIAGNOSTIC', 'message': 'timeout detected', 'sequence': 6},
    {'timestamp': '2023-04-05T10:01:13Z', 'level': 'INFO', 'type': 'DIAGNOSTIC', 'message': 'retry attempt 1', 'sequence': 7},
    {'timestamp': '2023-04-05T10:01:15Z', 'level': 'INFO', 'type': 'DIAGNOSTIC', 'message': 'critical: buffer overflow', 'sequence': 9}
]

# Execute function
analyze_device_stream(logs)