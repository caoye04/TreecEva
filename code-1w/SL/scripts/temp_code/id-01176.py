from collections import defaultdict, Counter

def preprocess_logs(raw_logs):
    processed = []
    temp_store = defaultdict(int)
    invalid_count = 0

    for log in raw_logs:
        parts = log.strip().split('|')
        if len(parts) < 3:
            invalid_count += 1
            continue

        timestamp, level, message = parts[0], parts[1], parts[2]
        category = "general"
        if "ERROR" in message:
            category = "error"
        elif "WARN" in message:
            category = "warning"

        word_count = len(message.split())
        temp_store[category] += 1
        processed.append({
            'level': level,
            'words': word_count,
            'has_error_term': 'error' in message.lower(),
            'timestamp_len': len(timestamp)
        })

    # Irrelevant aggregation (distractor)
    summary_stats = dict(temp_store)
    total_entries = len(processed)
    avg_word_length = sum(len(word) for log in raw_logs for word in log.split()) / max(total_entries, 1)

    return processed, summary_stats, avg_word_length

def analyze_patterns(data_list):
    pattern_counter = Counter()
    total_high_word_entries = 0
    cumulative_shift = 0

    for item in data_list:
        key_pattern = f"{item['level']}_{item['words'] % 3}"
        pattern_counter[key_pattern] += 1

        if item['words'] > 5:
            total_high_word_entries += 1

        # Misleading bit manipulation (not used later)
        shifted = item['timestamp_len'] << 2
        cumulative_shift ^= shifted

    # Dead computation (distractor)
    entropy_approx = 0
    for count in pattern_counter.values():
        if count > 0:
            entropy_approx -= (count / len(data_list)) * (count / len(data_list))

    return pattern_counter, total_high_word_entries

def calculate_final_score(data):
    base_score = 0
    adjustment_factor = 1.0

    for entry in data:
        if entry['has_error_term']:
            base_score += entry['words'] * 2
        else:
            base_score += entry['words'] // 2

        if entry['level'] == 'CRITICAL':
            adjustment_factor *= 1.1

    final_score = int(base_score * adjustment_factor)
    return final_score

# Main execution
raw_system_logs = [
    "2023-08-01|INFO|System started successfully",
    "2023-08-01|WARNING|Disk usage at 85% capacity",
    "2023-08-01|ERROR|Failed to connect to database error_code=500",
    "2023-08-01|CRITICAL|Critical failure in main thread detected",
    "2023-08-01|DEBUG|Memory dump: 0xABCDEF123456",
    "2023-08-01|INFO|User login successful",
    "2023-08-01|ERROR|Permission denied for resource access"
]

# Step 1: Preprocess logs
processed_data, stats, average_word_length = preprocess_logs(raw_system_logs)

# Step 2: Analyze patterns (semi-relevant but not used in final score)
data_patterns, high_word_count_total = analyze_patterns(processed_data)

# Step 3: Calculate final score
temp_debug_value = sum(len(str(k)) for k in data_patterns.keys())  # Distractor
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")