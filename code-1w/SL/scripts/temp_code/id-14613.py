from collections import defaultdict
import math

def analyze_user_activity(raw_data, filter_char, penalty_rate):
    # Irrelevant preprocessing: counting character frequencies
    char_count = defaultdict(int)
    for entry in raw_data:
        for c in entry['action_log']:
            char_count[c] += 1

    filtered_logs = []
    total_duration = 0
    idle_count = 0

    # Semi-relevant transformation: extract and clean logs
    for record in raw_data:
        log = record['action_log'].strip().lower()
        duration = record['duration_sec']
        if filter_char in log:
            tokens = log.split(' ')
            cleaned_tokens = [t for t in tokens if len(t) > 1]
            processed_log = ' '.join(cleaned_tokens)
            filtered_logs.append({
                'log': processed_log,
                'len': len(processed_log),
                'duration': duration
            })
            total_duration += duration
        else:
            idle_count += 1  # distractor: not used later

    # Dead code path (never executed due to data, but looks relevant)
    if len(filtered_logs) > 100:
        scaling_factor = math.log(len(filtered_logs))
    else:
        scaling_factor = 1.0  # unused in logic

    return filtered_logs, total_duration


def compute_efficiency(metrics_list, base_factor):
    efficiency_scores = []
    temp_accumulator = 0

    for m in metrics_list:
        raw_score = m['len'] * base_factor / (m['duration'] + 1)
        normalized = math.sqrt(raw_score ** 2)  # redundant but looks complex
        efficiency_scores.append(normalized)
        temp_accumulator += normalized  # red herring accumulator

    # Additional distraction: sort but don't use sorted list
    sorted_scores = sorted(efficiency_scores, reverse=True)
    avg_efficiency = sum(efficiency_scores) / len(efficiency_scores) if efficiency_scores else 0

    return avg_efficiency


def aggregate_performance(log_entries, user_threshold):
    performance_bins = defaultdict(list)
    outlier_flags = []

    for idx, entry in enumerate(log_entries):
        key_length = entry['len']
        perf_class = 'high' if key_length >= user_threshold else 'low'
        performance_bins[perf_class].append(entry)

        # Distractor flagging logic (not used in output)
        if idx % 7 == 0 and key_length < 50:
            outlier_flags.append(idx)

    high_performers = performance_bins['high']
    low_performers = performance_bins['low']

    # Core calculation
    total_weight = 0
    cumulative_adjustment = 0

    for hp in high_performers:
        weight = hp['len'] * 0.3
        adjustment = hp['duration'] * 0.05
        total_weight += weight
        cumulative_adjustment += adjustment

    for lp in low_performers:
        weight = lp['len'] * 0.1
        total_weight += weight

    final_score = int((total_weight - cumulative_adjustment) * 1.25)

    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Simulated input data
raw_session_data = [
    {'action_log': 'click navigation menu quickly', 'duration_sec': 12},
    {'action_log': 'open settings panel and adjust brightness', 'duration_sec': 23},
    {'action_log': 'scroll through long article content', 'duration_sec': 18},
    {'action_log': 'submit form with multiple fields', 'duration_sec': 31},
    {'action_log': 'view image gallery full screen', 'duration_sec': 45},
    {'action_log': 'search for documentation keywords', 'duration_sec': 27},
    {'action_log': 'download large file using wifi', 'duration_sec': 67},
    {'action_log': 'update profile information securely', 'duration_sec': 29}
]

# Begin processing
processed_logs, total_time = analyze_user_activity(raw_session_data, 'a', penalty_rate=0.05)
efficiency_metric = compute_efficiency(processed_logs, base_factor=1.7)
final_score = aggregate_performance(processed_logs, user_threshold=35)