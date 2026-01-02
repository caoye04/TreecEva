def evaluate_performance(log, keywords):
    count_map = {}
    total_entries = len(log)
    valid_count = 0
    temp_sum = 0

    for entry in log:
        cleaned = entry.strip().lower()
        if not cleaned:
            continue
        words = cleaned.split()
        
        # Irrelevant aggregation (distractor)
        for word in words:
            if word in count_map:
                count_map[word] += 1
            else:
                count_map[word] = 1

        # Actual logic: check keyword presence
        found = False
        for word in words:
            if word in keywords:
                found = True
                break
        if found:
            valid_count += 1

    # Distractor computation
    if count_map:
        avg_frequency = sum(count_map.values()) / len(count_map)
        temp_sum += avg_frequency * 1.5

    # More distraction: sorting unused data
    sorted_keys = sorted(count_map.keys(), key=lambda x: count_map[x], reverse=True)
    top_five = sorted_keys[:5]

    # Actual score calculation
    completeness_ratio = valid_count / total_entries if total_entries > 0 else 0
    final_score = int(completeness_ratio * 100)

    # Dead code path (never reached due to logic)
    if final_score > 200:
        final_score = 100

    return final_score

# Input data
feedback_log = [
    "Great work on the presentation!",
    "Needs improvement in clarity.",
    "Excellent use of data.",
    "The analysis was thorough.",
    "",  # Empty entry
    "Clarity and precision need attention.",
    "Outstanding performance overall!"
]
target_words = {"clarity", "data", "analysis", "precision"}

# Execute
final_score = evaluate_performance(feedback_log, target_words)
print(f"Result: {final_score}")