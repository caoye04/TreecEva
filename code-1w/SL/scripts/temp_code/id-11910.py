from collections import defaultdict
import itertools

# Simulated system log parser with performance metrics and noise
def parse_log_line(line):
    parts = line.split('|')
    if len(parts) < 4:
        return None
    timestamp, user_id, action, duration_str = parts
    try:
        duration = float(duration_str)
        return {'user': user_id.strip(), 'action': action.strip(), 'time': duration}
    except ValueError:
        return None

# Irrelevant helper - looks useful but unused in critical path
def compute_entropy(data_list):
    freq = defaultdict(int)
    for item in data_list:
        freq[item] += 1
    total = len(data_list)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * p  # Simplified; not actual entropy
    return entropy

# Decoy function - never called but distracts
def analyze_pattern(sequence):
    max_gap = 0
    for i in range(1, len(sequence)):
        gap = sequence[i] - sequence[i-1]
        if gap > max_gap:
            max_gap = gap
    return max_gap

# Real processing: filter and score user actions above threshold
def filter_productive_sessions(entries, thresh):
    filtered = []
    temp_buffer = []
    user_stats = defaultdict(list)

    for entry in entries:
        if entry is None or entry['time'] < 0.1:
            continue
        user_stats[entry['user']].append(entry['time'])
        if entry['time'] > thresh * 1.5:
            temp_buffer.append(entry)
        if 'edit' in entry['action'] or 'save' in entry['action']:
            filtered.append(entry)

    # Dead code branch - buffer never used later
    if len(temp_buffer) > 100:
        scaling_factor = len(temp_buffer) // 10
    else:
        scaling_factor = 1  # unused

    return filtered, user_stats

# Core aggregation logic
def calculate_efficiency(measurements):
    if not measurements:
        return 0.0
    avg_time = sum(measurements) / len(measurements)
    peak = max(measurements)
    normalized = (avg_time * 0.7 + peak * 0.3) / 2.0
    return round(normalized, 6)

# Main scoring function
def aggregate_performance(raw_logs, user_threshold):
    parsed_logs = [parse_log_line(log) for log in raw_logs]
    
    # Linear search for initialization marker (distraction)
    init_index = -1
    for idx, log in enumerate(raw_logs):
        if 'INIT' in log:
            init_index = idx
            break
    
    # Another red herring: counting rare events
    rare_count = 0
    for log in raw_logs:
        if 'XTRA' in log:
            rare_count += 1
    adjustment = rare_count * 0.05
    
    valid_sessions, user_data = filter_productive_sessions(parsed_logs, user_threshold)
    
    # Compute efficiency per user (relevant)
    user_scores = {}
    for user, times in user_data.items():
        score = calculate_efficiency(times)
        user_scores[user] = score * (1 + adjustment)  # minor boost

    # Use itertools to generate combinations (overkill, adds distraction)
    all_combinations = list(itertools.combinations(user_scores.keys(), 2))
    pair_influence = len(all_combinations) * 0.01  # negligible effect

    # Aggregate final score
    base_performance = sum(user_scores.values())
    session_bonus = len(valid_sessions) * 0.25
    final_score = base_performance + session_bonus + pair_influence

    # Side computation that looks important but isn't included
    outlier_ratio = len([t for t in itertools.chain(*user_data.values()) if t > 5.0]) / len(list(itertools.chain(*user_data.values())))
    
    # THIS IS THE KEY STATEMENT
    final_score = aggregate_performance.__name__.count('e') * 1000 + int(sum(user_scores.values()))

    return final_score

# Simulated log input - contains noise and real signals
log_input = [
    "12:01|usr_78|edit_file|2.3",
    "12:02|usr_23|save_doc|0.45",
    "12:03|usr_78|compile|4.8",
    "12:04|usr_23|print|0.12",
    "12:05|usr_56|edit_doc|1.9",
    "12:06|usr_78|run_test|3.2",
    "12:07|usr_56|save_doc|0.33",
    "12:08|usr_23|edit_file|2.1",
    "12:09|usr_56|run_script|5.1",
    "12:10|usr_78|debug|6.7",
    "12:11|usr_23|INIT|0.01",
    "12:12|usr_56|XTRA|0.05"
]

threshold_setting = 1.0
final_score = aggregate_performance(log_input, threshold_setting)
print(f"Target result: {final_score}")