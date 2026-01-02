def evaluate_performance(log_entries, threshold):
    total_chars = 0
    valid_entries = []
    temp_buffer = []
    char_frequency = {}

    for entry in log_entries:
        stripped_entry = entry.strip()
        if not stripped_entry.startswith('DEBUG'):
            total_chars += len(stripped_entry)
            if len(stripped_entry) > threshold:
                valid_entries.append(stripped_entry)
            else:
                temp_buffer.append(stripped_entry[::-1])  # reverse unused

        # Irrelevant computation: counting letter 'a'
        for char in stripped_entry:
            if char == 'a':
                char_frequency[char] = char_frequency.get(char, 0) + 1

    # Distractor: complex but unused structure
    summary_stats = {
        'count': len(valid_entries),
        'total_length': total_chars,
        'avg_length': total_chars / len(valid_entries) if valid_entries else 0
    }

    # Real logic: score based on valid entries containing 'ERROR' and length > 20
    critical_count = 0
    for ve in valid_entries:
        if 'ERROR' in ve and len(ve) > 20:
            critical_count += 1

    # Secondary distraction: unused checksum
    checksum = 0
    for i, c in enumerate(temp_buffer):
        checksum += len(c) * (i + 1)

    base_score = len(valid_entries) * 10
    penalty = critical_count * 3
    final_score = base_score - penalty

    return final_score

# Input data
log_data = [
    "DEBUG: system ok",
    "INFO: startup sequence initiated",
    "WARNING: low memory",
    "ERROR: failed to connect to database server - retrying",
    "DEBUG: retry mechanism active",
    "ERROR: timeout exceeded on primary node",
    "STATUS: fallback enabled"
]
threshold = 15

result = evaluate_performance(log_data, threshold)
print(f"Target result: {result}")