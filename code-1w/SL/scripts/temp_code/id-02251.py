def analyze_pattern(sequence):
    if len(sequence) < 3:
        return False
    trend = [sequence[i] < sequence[i+1] for i in range(len(sequence)-1)]
    return trend.count(True) > trend.count(False)

# Irrelevant helper function (distractor)
def normalize_data(values):
    max_val = max(values)
    return [v / max_val for v in values]

# Another decoy function dealing with unrelated logic
def validate_checksum(data_tuple):
    xor_sum = 0
    for item in data_tuple:
        if isinstance(item, int):
            xor_sum ^= item
    return xor_sum % 7 == 0

# Unused transformation (dead code path)
def transform_coordinates(coord_list):
    return [(c[0] * 2 + 1, c[1] * 2 - 1) for c in coord_list]

# Core logic buried among distractions
def compute_weighted_rank(ranks):
    base = sum(ranks)
    bonus = len([r for r in ranks if r < 10]) * 1.5
    penalty = len([r for r in ranks if r > 80]) * 2.0
    return base + bonus - penalty

# Misleading aggregation function that looks important but isn't used in final result
def aggregate_metrics(records):
    total = 0
    for rec in records:
        if rec.get('active'):
            total += rec['value'] * 0.8
        else:
            total += rec['value'] * 0.2
    return round(total, 2)

# Key function using set operations and lambda
rank_filter = lambda rs: {x for x in rs if x % 4 != 0}

def process_history(log_entries):
    events = []
    for entry in log_entries:
        event_type = entry.split(':')[0]
        value = int(entry.split(':')[-1])
        events.append((event_type, value))
    
    # Extract timestamps (irrelevant part)
    timestamps = [e[1] for e in events if e[0] == 'TS']
    
    # Actual relevant computation hidden here
    scores = [e[1] for e in events if e[0] == 'SCORE']
    return scores

# Main evaluation logic
rank_set = {5, 12, 18, 25, 30, 35, 44, 48, 55, 61, 67, 70, 73, 82, 85, 90, 95}
dummy_coords = [(1, 2), (3, 4), (5, 6)]
history_log = [
    'ACTION:15', 'SCORE:8', 'EVENT:1', 'TS:1623', 'SCORE:12', 'TS:1625',
    'UPDATE:3', 'SCORE:18', 'CHECK:7', 'TS:1630', 'SCORE:7', 'RESET:0'
]

# Dead assignment - looks like it does something important
system_status = {'initialized': True, 'version': '2.1.5', 'mode': 'debug'}

# Unused list comprehension with complex filtering (red herring)
filtered_ranks = [r for r in rank_set if (r > 20 and r < 80) or (r % 5 == 0)]

# Decoy dictionary construction
profile = {
    'id': 'USR92837',
    'access_level': 3,
    'permissions': ['read', 'write'],
    'last_login': '2023-08-14'
}

# Real work happens here but obscured by context
relevance_scores = process_history(history_log)
sorted_ranks = sorted(list(rank_set))
trimmed_ranks = rank_filter(sorted_ranks)

# Complex conditional expression with nested logic
adjustment_factor = 1.2 if analyze_pattern(relevance_scores) else 0.8

# Multiple simultaneous assignments (tuple unpacking)
base_value, extra_bonus = len(trimmed_ranks), sum(relevance_scores) // 4

# Intermediate computation mixed with irrelevant ones
temp_result = (base_value * 7) + (extra_bonus * 3)
checksum_test = validate_checksum((9, 16, 25, 36))  # Computed but unused

# Final performance evaluation - the actual answer source
def evaluate_performance(ranks, log):
    filtered = rank_filter(ranks)
    score_list = process_history(log)
    weighted = compute_weighted_rank(list(filtered))
    avg_score = sum(score_list) / len(score_list) if score_list else 0
    trend_boost = 10 if analyze_pattern(score_list) else 0
    final_component = weighted * adjustment_factor + avg_score + trend_boost
    return int(round(final_component))

# Critical execution point
final_score = evaluate_performance(rank_set, history_log)

# Output the required result
print(f"Target result: {final_score}")