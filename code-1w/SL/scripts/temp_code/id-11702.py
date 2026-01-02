def evaluate_performance(entries, min_duration):
    # Track relevant metrics
    total_duration = 0
    valid_sessions = 0
    peak_moment = 0
    session_streak = 0
    max_streak = 0

    # Irrelevant tracking variables (distractors)
    avg_noise = 0
    calibration_offset = 1.23
    debug_flags = [False] * len(entries)
    temporal_weights = []

    for i, entry in enumerate(entries):
        duration = entry['end'] - entry['start']
        activity_type = entry['type']
        signal_q = entry.get('quality', 1.0)

        # Weighted contribution (only some affect result)
        weighted_duration = duration * signal_q
        temporal_weights.append(weighted_duration * 0.95)  # Not actually used later

        if duration > min_duration:
            total_duration += duration
            valid_sessions += 1
            session_streak += 1
            if duration > peak_moment:
                peak_moment = duration
        else:
            if session_streak > max_streak:
                max_streak = session_streak
            session_streak = 0

        # Misleading computation: looks important but unused
        if i > 0 and entries[i-1]['type'] == activity_type:
            avg_noise += calibration_offset / (i + 1)

    if session_streak > max_streak:
        max_streak = session_streak

    # Secondary filter using slicing to analyze dense activity bursts
    active_window = entries[1:-1]  # Exclude first and last
    burst_count = 0
    for win in active_window:
        if (win['end'] - win['start']) > min_duration * 0.8:
            burst_count += 1

    # Final score depends only on total_duration, valid_sessions, and burst_count
    reliability_factor = 1.0 if max_streak < 4 else 1.15
    base_score = total_duration * valid_sessions
    adjustment = burst_count * peak_moment * 0.1
    final_score = int((base_score + adjustment) * reliability_factor)

    # Dead code path (never reached in practice due to logic above)
    if False and len(debug_flags) > 100:
        final_score += sum(temporal_weights) // 10

    return final_score

# Simulated log data
log_data = [
    {'start': 10, 'end': 25, 'type': 'compute', 'quality': 0.9},
    {'start': 30, 'end': 42, 'type': 'io', 'quality': 1.0},
    {'start': 45, 'end': 65, 'type': 'compute', 'quality': 1.1},
    {'start': 70, 'end': 75, 'type': 'io', 'quality': 0.8},
    {'start': 80, 'end': 98, 'type': 'compute', 'quality': 1.0},
    {'start': 100, 'end': 105, 'type': 'network', 'quality': 0.7},
    {'start': 110, 'end': 130, 'type': 'compute', 'quality': 1.2}
]

threshold = 12

# Key execution point
final_score = evaluate_performance(log_data, threshold)
print(f"Result: {final_score}")