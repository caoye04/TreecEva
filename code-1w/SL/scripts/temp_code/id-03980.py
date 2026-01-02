def analyze_system_integrity(log_entries):
    # Irrelevant preprocessing: reverse and pad logs (distractor)
    padded_logs = [entry.rjust(20, '#') for entry in log_entries]
    reversed_logs = [entry[::-1] for entry in padded_logs]

    # Key data structures
    critical_flags = set()
    temp_values = []
    shadow_buffer = []

    # Decoy analysis pass: computes but doesn't use this (dead path)
    for log in log_entries:
        if 'ERR' in log and 'CRITICAL' not in log:
            shadow_buffer.append(hash(log) % 100)

    # Real processing begins: extract diagnostic codes
    for idx, entry in enumerate(log_entries):
        if 'CRITICAL' in entry:
            code = int(entry.split('[')[1].split(']')[0])
            temp_values.append(code)
            if code % 4 == 0:
                critical_flags.add(f'FATAL_{code}')

    # Simulate complex state transitions (mixed relevance)
    state_vector = [0] * 5
    for val in temp_values:
        state_vector[val % 5] ^= val
        state_vector[(val + 1) % 5] += (val // 10)

    # Destructuring decoy: unpacking with unused variables
    x, y, z, w, v = state_vector
    adjustment_factor = x ^ z  # Only one used later

    # Compute derived thresholds (some are red herrings)
    base_threshold = sum(temp_values) // len(temp_values) if temp_values else 0
    secondary_cap = max(temp_values) * 0.75 if temp_values else 100
    rolling_limit = (base_threshold + secondary_cap) / 2

    # Real logic: filter alerts above dynamic threshold
    filtered_diagnostics = [v for v in temp_values if v > rolling_limit]

    # Another distraction: set difference with irrelevant entries
    all_possible = {i for i in range(10, max(temp_values) + 10)}
    known_ignored = {i for i in range(10, max(temp_values) + 10) if i % 7 == 0}
    remaining_alerts = list(all_possible - known_ignored - {999, 888})  # Overcomplicated

    # Core calculation (obscured by context)
    aggregate_score = 0
    for d in filtered_diagnostics:
        if d % 2 == 1:
            aggregate_score += d * 3
        else:
            aggregate_score -= d // 2

    # Final computation point — this is where answer is determined
    final_diagnostic = aggregate_score + len(remaining_alerts)

    # Print required result
    print(f"Result: {final_diagnostic}")

    return final_diagnostic

# Input data
logs = [
    "[12] STATUS OK",
    "[24] ERR TIMEOUT", 
    "[36] CRITICAL FLOOD_DETECTED",
    "[41] CRITICAL POWER_SPIKE", 
    "[55] CRITICAL OVERLOAD",
    "[60] WARNING TEMP_HIGH"
]

# Execute
result = analyze_system_integrity(logs)