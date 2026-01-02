def process_telemetry(raw_packets, config_profile):
    timing_log = []
    system_flags = []
    checksum_counter = 0
    temporal_weights = [0.1, 0.3, 0.6]
    baseline_offset = 245
    decoy_accumulator = 0

    for idx, packet in enumerate(raw_packets):
        if len(packet) < 4:
            continue

        # Parse packet structure
        header = packet[0]
        payload = packet[1:3]
        footer = packet[3]

        # Irrelevant signal processing (distractor)
        for i in range(len(temporal_weights)):
            decoy_accumulator += payload[0] * temporal_weights[i] + idx

        # Real logic: extract timing jitter
        if header & 0x08:
            jitter_value = (footer ^ 0xAA) % 17
            timing_log.append(jitter_value + baseline_offset)

        # Flag anomalies based on bit patterns
        flag_state = 0
        if payload[0] & 0x01 and not (payload[1] >> 2) & 0x01:
            flag_state |= 0x01
        if footer & 0x0F > 9:
            flag_state |= 0x02
        if bin(header).count('1') % 2 == 0:
            flag_state |= 0x04  # parity check

        system_flags.append(flag_state)

        # Dead code path - never executed due to fixed profile
        if config_profile == 'DEBUG_X9':
            reset_sequence = [decoy_accumulator, idx]
            break

    # Misleading intermediate summary (unused)
    average_jitter = sum(timing_log) / len(timing_log) if timing_log else 0
    anomaly_density = len([f for f in system_flags if f != 0]) / len(system_flags) if system_flags else 0

    def aggregate_metrics(log, flags):
        weighted_sum = 0
        adjustment_factor = 0.25
        for i, (tick, flag) in enumerate(zip(log, flags)):
            if i % 3 == 0:
                contribution = tick * 0.7
            elif flag & 0x01:
                contribution = tick * 0.4
            else:
                contribution = tick * 0.1

            # Complex decay pattern
            decay = 1 / (1 + i * adjustment_factor) if i > 0 else 1
            weighted_sum += contribution * decay

            # Red herring computation
            temp_diag = (weighted_sum * 123) % 47

        # Final computation
        raw_total = int(weighted_sum)
        flag_bonus = sum(1 for f in flags if f & 0x04) * 15
        penalty = sum(1 for f in flags if f & 0x02) * 7
        return raw_total + flag_bonus - penalty

    # Unused function (distractor)
    def compute_signal_envelope(data):
        envelope = 0
        for val in data:
            envelope += abs(val - 256) ** 0.5
        return envelope

    final_diagnostic = aggregate_metrics(timing_log, system_flags)
    Result: final_diagnostic