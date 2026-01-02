def analyze_sentiment(text_data):
    # Irrelevant helper function – distractor
    char_count = {char: text_data.count(char) for char in set(text_data)}
    upper_ratio = sum(1 for c in text_data if c.isupper()) / len(text_data)
    return upper_ratio > 0.3


def validate_sequence(seq):
    # Dead code path – never called in execution
    if len(seq) < 5:
        return False
    cumulative = 0
    for i, val in enumerate(seq):
        if i % 2 == 0:
            cumulative += val ** 2
        else:
            cumulative -= val
    return cumulative > 10

# Misleading data structures
raw_logs = ['ERROR: timeout', 'INFO: retrying', 'WARN: deprecated', 'INFO: success']
timestamp_weights = [1.1, 0.9, 1.3, 0.8]

# Actual relevant data
feedback_strings = ['very positive', 'negative', 'positive', 'neutral', 'very positive']
engagement_ranks = [5, 2, 4, 3, 5]
sentiment_multiplier = {'neutral': 1, 'positive': 2, 'very positive': 3, 'negative': -1}

# Distractor: complex but unused transformation
encoded_signals = []
for idx, entry in enumerate(feedback_strings):
    encoded = 0
    for ch in entry:
        if ch in 'aeiou':
            encoded ^= ord(ch) << (idx % 4)
    encoded_signals.append(encoded % 17)

# Relevant logic begins here
mapped_levels = []
for fb in feedback_strings:
    level = 1
    if 'very' in fb:
        level += 1
    if 'positive' in fb:
        level += 1
    if 'negative' in fb:
        level -= 2
    mapped_levels.append(level)

# Combine with engagement using zip – python idiom
combined_metrics = []
for rank, level in zip(engagement_ranks, mapped_levels):
    combined_metrics.append(rank * level)

# Secondary transformation with enumerate
adjusted_metrics = []
for i, val in enumerate(combined_metrics):
    adjustment = 1
    if i > 0 and combined_metrics[i] > combined_metrics[i-1]:
        adjustment += 0.5
    if len(str(val)) % 2 == 0:  # another minor red herring
        adjustment *= 1.1
    adjusted_metrics.append(val * adjustment)

# Decoy accumulation (never used)
total_weighted_log = 0
for log_entry, weight in zip(raw_logs, timestamp_weights):
    total_weighted_log += len(log_entry) * weight

# Core aggregation logic
baseline_offset = sum(1 for s in feedback_strings if 'very' in s) * 2
penalty = sum(1 for s in feedback_strings if 'negative' in s) * 3

# Real accumulation
aggregate = 0
for metric in adjusted_metrics:
    if metric > 0:
        aggregate += int(metric)
    else:
        aggregate -= int(abs(metric) / 2)

# Final performance calculation
def aggregate_performance(levels):
    base = sum(levels)
    bonus = 0
    for i, lvl in enumerate(levels):
        if lvl >= 2 and i % 2 == 0:
            bonus += 2
    return base + bonus + baseline_offset - penalty

# Critical execution point
final_score = aggregate_performance(mapped_levels)

# Print result as required
print(f"Target result: {final_score}")