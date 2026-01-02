def analyze_sentiment(pattern):
    # Distractor: unused function
    return sum(1 for c in pattern if c in 'aeiou')


def validate_sequence(seq):
    # Distractor: complex but unused validation
    if len(seq) < 5:
        return False
    balanced = sum(1 for s in seq if s % 2 == 0) == sum(1 for s in seq if s % 2 != 0)
    return balanced and max(seq) - min(seq) <= 10

# Irrelevant data structures
token_map = {'A': 1, 'B': 2, 'C': 3, 'X': -99, 'Y': -99}
lookup_grid = [[i * 3 + j for j in range(4)] for i in range(4)]

# Real input data
feedback_logs = [
    [8, 7, 9, 6],
    [5, 8, 7, 8],
    [9, 9, 6, 7],
    [7, 6, 8, 9]
]

weights = [0.4, 0.3, 0.2, 0.1]  # Weight decay across feedback rounds

# Dead code path variable (red herring)
optimized_path_triggered = False

# Unused transformation
normalized_logs = []
for log in feedback_logs:
    avg = sum(log) / len(log)
    normalized_logs.append([round((x - avg) * 1.5) for x in log])

# Distractor computation with set operations
unique_values = set()
for entry in feedback_logs:
    unique_values.update(entry)
duplicate_count = len(feedback_logs[0]) - len(set(feedback_logs[0]))  # Only checks first, misleading

# Simulated confidence levels (irrelevant)
confidence_levels = []
for i, entry in enumerate(feedback_logs):
    conf = (i + 1) * 0.2 + sum(entry) / 10
    confidence_levels.append(round(conf, 2))

# Key transformation using enumerate and zip (required python features)
adjusted_logs = []
for i, log in enumerate(feedback_logs):
    adjusted = []
    for j, (val, w) in enumerate(zip(log, weights)):
        # Apply positional decay and round using integer division logic
        adjustment = (val * w * 10) // (j + 1) if j > 0 else val * w * 10
        adjusted.append(int(adjustment))
    adjusted_logs.append(adjusted)

# Intermediate aggregation (some steps are distracting)
raw_aggregates = []
for adj_log in adjusted_logs:
    # Use of min/max/average - relevant
    center = len(adj_log) // 2
    focused_slice = adj_log[center-1:center+1] if len(adj_log) > 2 else adj_log
    raw_aggregates.append(
        (sum(focused_slice) + max(focused_slice)) // 2
    )

# Secondary weighting (only some matter)
effective_weights = []
for idx, raw in enumerate(raw_aggregates):
    factor = 1.0
    if idx % 2 == 0:
        factor *= 1.1
    if sum(feedback_logs[idx]) > 30:
        factor *= 1.05
    effective_weights.append(factor)

# Core answer computation
aggregate_performance = 0
for idx, raw_val in enumerate(raw_aggregates):
    contribution = raw_val * effective_weights[idx]
    aggregate_performance += contribution

# Final scaling with rounding to 2 decimal places
final_score = round(aggregate_performance, 2)

# Decoy output statements
# print(f'Debug - Unique values: {sorted(unique_values)}')
# print(f'Confidence summary: {sum(confidence_levels)/len(confidence_levels):.2f}')

# Critical output
print(f"Result: {final_score}")