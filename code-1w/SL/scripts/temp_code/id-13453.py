import math

# Irrelevant helper function (dead code path)
def analyze_sensor_data(data):
    return sum(x ** 2 for x in data if x > 0) // len(data) if data else 0

# Misleading metric computation (unused)
baseline_offset = 17
temp_weights = [0.1, 0.2, 0.3, 0.4]
raw_aggregate = 0
for i in range(4):
    raw_aggregate += temp_weights[i] * (i + 1) ** 2

# Real input data
event_logs = [1, 1, 0, 1, 0, 1]
user_flags = {True, False}

# Core metrics
def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        p = v / total if total != 0 else 0
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 6)

# Auxiliary transformation
transformed_ranks = []
counter = 0
for log in event_logs:
    if log:
        counter += 1
        transformed_ranks.append(counter * 2)
    else:
        transformed_ranks.append(-1)

# Simulate ranking with noise
rankings = []
for i, val in enumerate(transformed_ranks):
    if val != -1:
        rankings.append(val + (i % 3))
    else:
        rankings.append(None)

# Filter out invalid entries
filtered_ranks = [r for r in rankings if r is not None]

# Additional distraction: unused bitwise analysis
bit_analysis = 0
for r in filtered_ranks:
    bit_analysis ^= r & 7

# Base performance metrics
base_metrics = {
    'count': len(filtered_ranks),
    'sum': sum(filtered_ranks),
    'max': max(filtered_ranks),
    'entropy': compute_entropy(filtered_ranks)
}

# Fake fusion logic (decoy)
def fuse_signals(a, b, c=1.0):
    return (a * 0.5 + b * 0.3) / (c + 1e-6)

intermediate_fuse = fuse_signals(base_metrics['sum'], base_metrics['max'])

# Real evaluation logic
def evaluate_performance(ranks, metrics):
    # Step 1: Normalize ranks using modular scaling
    normalized = [r % 7 for r in ranks]

    # Step 2: Count occurrences above threshold
    high_perf = sum(1 for r in normalized if r > 4)

    # Step 3: Apply combinatorial weight based on set uniqueness
    unique_set = set(normalized)
    combo_bonus = len(unique_set) * (len(unique_set) - 1) // 2

    # Step 4: Conditional adjustment based on entropy parity
    entropy_val = metrics['entropy']
    adjust_factor = 2 if abs(entropy_val - round(entropy_val)) < 0.01 else 1

    # Step 5: Accumulate score
    score = 0
    for x in normalized:
        score += x * adjust_factor

    # Step 6: Add combinatorics bonus only if certain conditions met
    if metrics['count'] >= 4 and len(unique_set) >= 5:
        score += combo_bonus * 3
    else:
        score += combo_bonus

    # Step 7: Final adjustment using modular arithmetic
    score = (score + base_metrics['sum']) % 97

    # Step 8: Inject deterministic offset (based on static condition)
    flags_list = list(user_flags)
    if len(flags_list) == 2:
        score += 5

    return score

# Execute main logic
final_score = evaluate_performance(filtered_ranks, base_metrics)

# Print result as required
print(f"Result: {final_score}")