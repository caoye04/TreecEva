def analyze_log_pattern(log):
    char_count = {}
    for char in log:
        if char.isalpha():
            char_count[char.lower()] = char_count.get(char.lower(), 0) + 1
    sorted_chars = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))
    return [item[0] for item in sorted_chars[:3]]

log_entries = [
    "Error: DB_CONN_FAILED | ID=0x1A",
    "Warning: HIGH_CPU_USAGE | ID=0x2C",
    "Info: USER_LOGIN_SUCCESS | ID=0x0F",
    "Error: AUTH_TIMEOUT | ID=0x1A",
    "Debug: CACHE_HIT | ID=0x3D"
]

# Irrelevant helper function (distractor)
def get_system_load(entry):
    if "ERROR" in entry.upper():
        return 90 + len(entry) % 10
    elif "WARNING" in entry.upper():
        return 75 + len(entry) % 5
    else:
        return 40 + len(entry) % 15

# Misleading intermediate variables
total_logs = len(log_entries)
duplicate_ids = {}
for entry in log_entries:
    id_part = entry.split('|')[1].strip()
    if id_part in duplicate_ids:
        duplicate_ids[id_part] += 1
    else:
        duplicate_ids[id_part] = 1

# Simulate buffer with character frequency analysis
buffer_analysis = []
for entry in log_entries:
    pattern = analyze_log_pattern(entry)
    buffer_analysis.extend(pattern)

# Secondary distractor: sorting unrelated metrics
freq_summary = {}
for char in buffer_analysis:
    freq_summary[char] = freq_summary.get(char, 0) + 1

sorted_summary = sorted(freq_summary.items(), key=lambda x: x[1], reverse=True)

def calculate_remaining_capacity(entries, limit):
    base_capacity = 1000
    usage_per_error = 75
    usage_per_warning = 30
    overhead_factor = 0.1

    error_count = 0
    warning_count = 0
    temp_debug_value = 0

    for entry in entries:
        upper_entry = entry.upper()
        if "ERROR" in upper_entry:
            error_count += 1
        if "WARNING" in upper_entry:
            warning_count += 1
        # Dead code path (distractor)
        if "DEBUG" in upper_entry and "CACHE" in upper_entry:
            temp_debug_value += len(entry) // 10

    raw_usage = (error_count * usage_per_error) + (warning_count * usage_per_warning)
    adjusted_usage = raw_usage * (1 + overhead_factor)

    # Complex conditional expression
    safety_margin = 50 if error_count > 1 else 25

    # Additional irrelevant computation
    avg_length = sum(len(e) for e in entries) / len(entries) if entries else 0
    length_penalty = int(avg_length // 10) * 5 if avg_length > 20 else 0

    # Final capacity calculation (key logic)
    final_capacity = base_capacity - adjusted_usage - safety_margin - length_penalty

    return int(final_capacity)

threshold = 3
final_capacity = calculate_remaining_capacity(log_entries, threshold)

print(f"Result: {final_capacity}")