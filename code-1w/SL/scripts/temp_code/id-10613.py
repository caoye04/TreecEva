def process_feedback(raw_entries):
    cleaned = [entry.strip().lower() for entry in raw_entries if entry.strip()]
    word_count = sum(len(e.split()) for e in cleaned)
    
    # Irrelevant transformation (distractor)
    reversed_entries = [e[::-1] for e in cleaned]
    palindrome_count = len([r for r in reversed_entries if r == r[::-1]])

    # Meaningless aggregation (dead path)
    total_chars = 0
    for entry in cleaned:
        for char in entry:
            if char.isalpha():
                total_chars += 1

    # Actual signal: count positive keywords
    positive_keywords = ['good', 'excellent', 'improved', 'satisfied', 'well']
    positive_hits = 0
    for entry in cleaned:
        words = entry.split()
        for word in words:
            if word in positive_keywords:
                positive_hits += 1

    return positive_hits, word_count


def calculate_baseline(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b  # Fibonacci-based baseline (red herring)


def normalize_score(x, min_val=0, max_val=100):
    if x < min_val:
        return min_val
    elif x > max_val:
        return max_val
    else:
        return x  # Clamping function (partially relevant)

# Decoy data structure
user_profile = {
    'id': 'USR98765',
    'access_level': 'admin',
    'last_login': '2023-08-15',
    'preferences': {
        'theme': 'dark',
        'notifications': True
    }
}

# Simulated logs with noise
feedback_logs = [
    "  Excellent work on the report! Very well detailed.  ",
    "The formatting could be improved.",
    "Good effort overall, satisfied with progress.",
    "",
    "IMPROVED significantly since last review. Well done!",
    "Not bad, but needs more examples.",
    "excellent choice of methodology"
]

calibration_factor = 3.5
offset_adjustment = -2  # Unused parameter (distractor)
dummy_flag = False

# Irrelevant preprocessing chain
processed_data = []
for log in feedback_logs:
    if log.strip():
        processed = log.replace('!', '.').replace('?', '.')
        sentences = processed.split('.')
        filtered = [s.strip() for s in sentences if s.strip()]
        processed_data.extend(filtered)

# Extract metrics
hit_count, total_words = process_feedback(feedback_logs)
baseline_ref = calculate_baseline(len(feedback_logs))

# Fake dependency
temp_score = hit_count * calibration_factor
adjusted_word_ratio = total_words / (hit_count + 1) if hit_count > 0 else 0

# Secondary irrelevant logic
categorized = {}
for word_len in [len(w) for w in ' '.join(feedback_logs).split()]:
    category = 'short' if word_len < 5 else 'long'
    categorized[category] = categorized.get(category, 0) + 1

# Core calculation disguised among distractions
raw_performance = temp_score + adjusted_word_ratio * 0.1
clamped_performance = normalize_score(raw_performance, 0, 50)

# Final aggregation using decoy variables
def aggregate_performance(logs, factor):
    count, _ = process_feedback(logs)
    fib_offset = calculate_baseline(len(logs)) % 4
    score = count * factor + fib_offset
    if score > 40:
        score -= 5  # Arbitrary threshold adjustment
    return int(round(score))

final_score = aggregate_performance(feedback_logs, calibration_factor)
print(f"Result: {final_score}")