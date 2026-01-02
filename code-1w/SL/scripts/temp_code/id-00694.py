from itertools import combinations

def analyze_patterns(sequence):
    count = 0
    trend = []
    for i in range(len(sequence) - 1):
        if sequence[i+1] > sequence[i]:
            trend.append(1)
        elif sequence[i+1] < sequence[i]:
            trend.append(-1)
        else:
            trend.append(0)
    
    # Irrelevant pattern analysis (distractor)
    oscillations = 0
    for i in range(len(trend) - 1):
        if trend[i] != 0 and trend[i+1] != 0 and trend[i] != trend[i+1]:
            oscillations += 1

    return trend

def calculate_entropy(values):
    # Dead function - not used in final computation
    from math import log2
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    total = len(values)
    entropy = 0
    for f in freq.values():
        p = f / total
        entropy -= p * log2(p)
    return round(entropy, 4)

raw_data = [23, 45, 12, 67, 34, 89, 33, 10]
offsets = {i: val % 10 for i, val in enumerate(raw_data)}

# Misleading transformation chain
shifted = [x - 5 for x in raw_data]
scaled = [x * 1.1 for x in shifted]
filtered = [x for x in scaled if x > 30]

# Core processing with relevant logic
base_weights = {i: val // 10 for i, val in enumerate(raw_data)}
processed_data = []
for idx, val in enumerate(raw_data):
    adjustment = 0
    if idx % 2 == 0:
        adjustment += offsets[idx]
    if base_weights[idx] > 3:
        adjustment -= 2
    processed_data.append(val + adjustment)

# Use of zip and enumerate together (required Python feature)
adjusted_pairs = []
for i, (a, b) in enumerate(zip(processed_data, reversed(processed_data))):
    if i % 3 == 0:
        adjusted_pairs.append(a - b + i)
    else:
        adjusted_pairs.append(a + b)

# Secondary distractor: unused combinatorial analysis
pair_sums = []
for pair in combinations(processed_data, 2):
    pair_sums.append(sum(pair))

# Key computation path
def calculate_final_score(data):
    score = 0
    for i, val in enumerate(data):
        if i % 4 == 0:
            score += val // 3
        elif i % 4 == 2:
            score -= val % 7
        else:
            score += (val % 4) - 1
    return score

# Final irrelevant calculation (dead code path)
max_pair_sum = max(pair_sums) if pair_sums else 0
total_oscillations = sum(1 for x in analyze_patterns(raw_data) if x != 0)

# Critical execution point
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")