def evaluate_performance(log_entries, threshold):
    # Track character frequency for anomaly detection (partially irrelevant)
    char_freq = {}
    total_chars = 0
    for entry in log_entries:
        for char in entry:
            char_freq[char] = char_freq.get(char, 0) + 1
            total_chars += 1

    # Normalize frequencies (distractor computation)
    norm_freq = {ch: cnt / total_chars for ch, cnt in char_freq.items() if cnt > 1}

    # Core logic: count entries meeting pattern criteria
    valid_count = 0
    warning_count = 0
    for entry in log_entries:
        stripped = entry.strip().lower()
        if 'error' in stripped and 'critical' not in stripped:
            warning_count += 1
        elif 'critical' in stripped:
            valid_count += 2  # Higher weight for critical issues
        elif 'info' in stripped and len(stripped) > 10:
            valid_count += 1

    # Secondary filter: only count if length diversity is sufficient
    lengths = set(len(entry) for entry in log_entries)
    diversity_bonus = len(lengths) if len(lengths) > threshold else 0

    # Red herring: unused complex calculation
    entropy = 0.0
    for p in norm_freq.values():
        if p > 0:
            entropy -= p * __import__('math').log2(p)

    # Final score with distraction variables
    base_score = valid_count * 17
    adjustment = warning_count * 3
    final_score = base_score - adjustment + diversity_bonus

    return final_score

# Input data
log_data = [
    "INFO: System started successfully.",
    "WARNING: High memory usage detected.",
    "ERROR: Failed to connect to database.",
    "CRITICAL: Authentication server down!",
    "info: user login attempt",
    "info: logging configuration updated"
]

total_lines = len(log_data)
threshold = 4
unused_snapshot = [len(x) for x in log_data if 'x' in x]  # Dead code path

final_score = evaluate_performance(log_data, threshold)
print(f"Result: {final_score}")