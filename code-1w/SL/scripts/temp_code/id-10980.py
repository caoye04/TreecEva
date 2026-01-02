def analyze_trend(data, threshold):
    trend = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend += 1
    return trend > threshold

# Irrelevant helper function (decoy)
def calculate_entropy(seq):
    from math import log2
    freq = {}
    for item in seq:
        freq[item] = freq.get(item, 0) + 1
    total = len(seq)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 3)

# Unused sorting logic (dead code path)
def sort_by_priority(items):
    return sorted(items, key=lambda x: (x[1], -x[2]))

# Distractor variables
temp_log = [0.5, 1.2, 3.4, 2.1, 0.9]
dummy_mask = [1, 0, 1, 1, 0]
offset_correction = sum(temp_log[:3]) * 0.5

# Real computation begins
baseline = [85, 90, 78, 92, 88]
metrics = [89, 94, 80, 96, 91]

# Bit manipulation red herring
bit_flags = 0b1010 ^ 0b1100 & 0b1111
flag_check = (bit_flags << 2) | 0b10

# Slicing with misleading purpose
slice_preview = metrics[1:4:1]
summary_stats = [sum(baseline), sum(metrics), abs(sum(baseline) - sum(metrics))]

# Conditional branch with early exit decoy
if len(metrics) % 2 == 0:
    dummy_result = [x * 0.9 for x in metrics]
    if sum(dummy_result) < 300:
        final_output = -1  # dead end

# Real evaluation logic
status_flags = []
for a, b in zip(metrics, baseline):
    if a >= b + 3:
        status_flags.append(2)
    elif a <= b - 3:
        status_flags.append(-1)
    else:
        status_flags.append(1)

# Recursive helper for combinatorics distraction
def count_combinations(n, r):
    if r > n or r < 0:
        return 0
    if r == 0 or r == n:
        return 1
    return count_combinations(n-1, r-1) + count_combinations(n-1, r)

combination_key = count_combinations(5, 2)  # evaluates to 10, unused later

# Main scoring logic
raw_improvement = sum(m - b for m, b in zip(metrics, baseline))
bonus_factor = 0
if raw_improvement > 10:
    bonus_factor = 2
elif raw_improvement > 5:
    bonus_factor = 1

# Conditional expression with slicing side-path
adjustment = len(slice_preview[::1]) if raw_improvement > 0 else 0
penalty = 0
for flag in status_flags:
    if flag == -1:
        penalty += 3

# Key statement
final_score = evaluate_performance(metrics, baseline)

# Actual implementation of evaluate_performance
def evaluate_performance(mets, base):
    improvement_per_item = [m - b for m, b in zip(mets, base)]
    positive_changes = [val for val in improvement_per_item if val > 0]
    negative_changes = [val for val in improvement_per_item if val < 0]
    net_gain = sum(positive_changes) - sum(abs(x) for x in negative_changes)
    consistency_bonus = 3 if all(m >= b * 0.95 for m, b in zip(mets, base)) else 0
    stability_penalty = 0
    if len(positive_changes) > 0 and len(negative_changes) > 0:
        stability_penalty = 2
    
    # Final formula
    score = net_gain * 2 + consistency_bonus - stability_penalty
    return int(score)

# Print result
print(f"Result: {final_score}")