def analyze_system_integrity(raw_logs, thresholds):
    # Irrelevant pre-processing: log normalization (distractor)
    normalized = [x / max(raw_logs) for x in raw_logs if x > 0]
    filtered = [x for x in raw_logs if x > thresholds.get('noise_floor', 10)]

    # Key data structures
    event_set = set(raw_logs)
    critical_events = {x for x in event_set if x % 7 == 0 and x > 50}
    backup_indices = [i for i, x in enumerate(raw_logs) if x in critical_events]

    # Distractor: unused function
    def decrypt_segment(data):  # Never called
        return [d ^ 255 for d in data][::2]

    # Real processing begins
    window_size = 4
    rolling_averages = []
    for i in range(len(filtered) - window_size + 1):
        window = filtered[i:i + window_size]
        avg = sum(window) / window_size
        rolling_averages.append(round(avg, 2))

    # Bit manipulation layer (key)
    base_signature = 0
    for val in rolling_averages:
        if val > 200:
            base_signature ^= int(val) & 0xFF

    # Another distractor: dead code path
    temp_state = None
    if len(rolling_averages) > 100:
        temp_state = sum(rolling_averages) // len(rolling_averages)
        temp_state += 999  # unreachable under current data

    # Data transformation with zip and enumerate (required feature)
    indexed_filtered = list(enumerate(filtered))
    paired_shifts = []
    for idx, (i, val) in enumerate(zip(indexed_filtered, filtered)):
        if idx >= len(indexed_filtered) - 1:
            break
        shift = (val ^ filtered[idx + 1]) & 0xF
        paired_shifts.append(shift)

    # Control flow with nested conditions
    aggregate_score = 0
    anomaly_mask = 0
    active_nodes = []

    for i, log_val in enumerate(filtered):
        if log_val < thresholds.get('critical_low', 50):
            continue
        if any(log_val % prime == 0 for prime in [2, 3, 5, 7, 11]):
            anomaly_mask |= (1 << (log_val % 8))
            if log_val not in active_nodes:
                active_nodes.append(log_val)
        else:
            aggregate_score += log_val // 10

    # Distractor: irrelevant string processing
    status_msg = "System nominal"
    if len(active_nodes) > 10:
        status_msg = "Overload: " + "".join([chr(65 + (x % 26)) for x in active_nodes[:3]])

    # Decoy calculation
    phantom_risk = 0
    for x in paired_shifts:
        phantom_risk += x ** 2
        if phantom_risk > 1000:
            phantom_risk //= 3

    # Final key computation
    correction_factor = len(paired_shifts) and (base_signature or 13)
    final_diagnostic = aggregate_score + correction_factor * (len(active_nodes) ^ anomaly_mask)

    # Output requirement
    print(f"Result: {final_diagnostic}")

# Input data (fixed seed equivalent)
logs = [120, 85, 63, 44, 91, 77, 105, 58, 119, 98, 133, 70, 84, 99, 112]
config = {'noise_floor': 40, 'critical_low': 60}

analyze_system_integrity(logs, config)