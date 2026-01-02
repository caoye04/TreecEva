def evaluate_performance(log, min_threshold):
    # Count total entries and valid attendances
    entry_count = len(log)
    present_days = [day for day in log if 'present' in day.lower()]
    absent_days = [day for day in log if 'absent' in day.lower()]

    # Misleading distraction: process timestamps (not used in final logic)
    total_seconds = 0
    for entry in log:
        if 'time:' in entry:
            time_part = entry.split('time:')[-1].strip()
            hours, minutes = map(int, time_part.split(':'))
            total_seconds += hours * 3600 + minutes * 60  # unused later

    # Character frequency analysis (semi-relevant red herring)
    char_freq = {}
    for entry in log:
        for c in entry:
            if c.isalpha():
                char_freq[c] = char_freq.get(c, 0) + 1
    rare_chars = [c for c, freq in char_freq.items() if freq < 2]
    obfuscation_factor = len(rare_chars) % 7  # only indirectly influences

    # Core logic: attendance ratio
    attendance_rate = len(present_days) / entry_count if entry_count else 0
    base_score = attendance_rate * 100

    # Apply adjustment based on threshold
    if attendance_rate >= min_threshold:
        bonus = 15
    else:
        bonus = -10

    # Distractor: nested loop counting substrings (not directly used)
    pattern_matches = 0
    statuses = ['present', 'absent', 'late']
    for status in statuses:
        for entry in log:
            if status in entry:
                pattern_matches += entry.count(status)
    noise_offset = pattern_matches % 11 - 5  # minor interference

    # Final computation
    raw_final = base_score + bonus + obfuscation_factor
    final_score = int(raw_final - noise_offset)  # deterministic result

    return final_score

# Simulated employee attendance log with embedded metadata
attendance_log = [
    'Day1: present, time: 09:14',
    'Day2: absent, time: 00:00',
    'Day3: present, time: 08:55',
    'Day4: late, time: 10:05',
    'Day5: present, time: 09:00',
    'Day6: absent, time: 00:00',
    'Day7: present, time: 09:20'
]
threshold = 0.6

# Key execution point
final_score = evaluate_performance(attendance_log, threshold)
print(f"Target result: {final_score}")