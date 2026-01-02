from collections import defaultdict, Counter

# Simulate user interaction logs with action types and timestamps
raw_logs = [
    ('click', 10), ('scroll', 15), ('click', 20), ('keypress', 25),
    ('scroll', 30), ('click', 35), ('click', 40), ('scroll', 45)
]

# Misleading preprocessing: irrelevant transformation
transformed_logs = [(action.upper(), ts * 2) for action, ts in raw_logs]
duplicate_counter = Counter([action for action, _ in transformed_logs])

# Actual processing pipeline
action_count = defaultdict(int)
time_segments = []

for action, timestamp in raw_logs:
    action_count[action] += 1
    if timestamp > 20:
        time_segments.append(timestamp // 10)

# Secondary analysis (partially relevant)
frequent_actions = {k: v for k, v in action_count.items() if v >= 2}
segment_distribution = Counter(time_segments)

# Red herring: unused function
def analyze_engagement(logs):
    total = len(logs)
    unique_actions = len(set(a for a, t in logs))
    return total * unique_actions

# Irrelevant aggregation
fake_summary = {
    'total_entries': len(transformed_logs),
    'unique_transformed': len(set(transformed_logs)),
    'max_time': max(ts for _, ts in transformed_logs)
}

# Core logic disguised among distractions
processed_data = []
for idx, (action, ts) in enumerate(raw_logs):
    if action == 'click':
        processed_data.append((idx + 1) * ts % 7)

# Another distraction: nested loop with no impact
buffer_cache = []
for i in range(2):
    temp_row = []
    for j in range(3):
        temp_row.append(i * j + 5)
    buffer_cache.append(temp_row)

# Critical computation hidden among side calculations
running_total = 0
for val in processed_data:
    running_total += val * 2
    if running_total > 20:
        running_total -= 10

scaling_factor = len(frequent_actions) + 1  # depends on data
base_modifier = segment_distribution[4]  # counts how many timestamps in 40-49

intermediate_score = running_total + scaling_factor * base_modifier

# Final nonlinear adjustment using case conversion distraction
noise_sequence = 'AbCDe'
adjustment = sum(ord(c.lower()) - ord('a') for c in noise_sequence) // 5

final_score = compute_final_score(intermediate_score) if 'compute_final_score' in globals() else intermediate_score + adjustment

# Dummy function definition placed after usage (will be caught by interpreter)
def compute_final_score(x):
    return x + 3 * (x % 4) - 1

print(f"Result: {final_score}")