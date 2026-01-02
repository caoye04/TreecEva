def analyze_performance(log_entries, baseline):
    # Irrelevant statistics (distractors)
    total_chars = sum(len(entry) for entry in log_entries)
    avg_length = total_chars / len(log_entries) if log_entries else 0
    upper_count = 0
    normalized_data = []

    for entry in log_entries:
        clean_entry = entry.strip().lower()
        if clean_entry.startswith('err'):
            continue  # Ignore error logs
        processed = ''.join(ch for ch in clean_entry if ch.isalnum())
        normalized_data.append(processed)

    # Decoy transformation: case conversion and slicing (partially irrelevant)
    sliced_segments = [item[1:-1] for item in normalized_data if len(item) > 2]
    reversed_parts = [seg[::-1] for seg in sliced_segments]

    # Core logic embedded within noise
    valid_records = []
    for item in normalized_data:
        if item.isdigit():
            num = int(item)
            if num > baseline * 0.85:  # Threshold filter
                valid_records.append(num)

    # Secondary distractor: string pattern analysis (unused)
    pattern_match_count = 0
    for part in reversed_parts:
        if len(part) >= 3 and part[0] == part[-1]:
            pattern_match_count += 1

    # Real computation path
    adjustment_factor = len(sliced_segments) - pattern_match_count or 1
    raw_sum = sum(valid_records)

    # Misleading early return (dead code path)
    if avg_length < 5 and upper_count == 0:
        return -999  # Never reached due to data

    # Actual score calculation
    if raw_sum == 0:
        final_score = baseline
    else:
        final_score = (raw_sum // len(valid_records)) if valid_records else 0
        final_score = (final_score + baseline) // adjustment_factor

    # Additional red herring: unused bitwise manipulation
    bit_noise = (baseline << 2) ^ raw_sum
    bit_noise %= 17

    return final_score

# Simulated input data
log_entries = [
    '  Transaction successful: 4567  ',
    'INFO: user login',
    'ERR_CRITICAL: timeout',
    '  8888  ',
    'data_sync_complete',
    '  12345  ',
    'status_ok',
    '  7777  ',
    'maintenance_window'
]
baseline = 5000

# Key execution point
final_score = analyze_performance(log_entries, baseline)
print(f"Target result: {final_score}")