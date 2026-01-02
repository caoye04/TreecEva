from itertools import combinations

def analyze_pattern(sequence):
    count = 0
    trend = []
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            trend.append(1)
        elif sequence[i] < sequence[i-1]:
            trend.append(-1)
        else:
            trend.append(0)
    
    # Irrelevant computation: counts oscillations but unused later
    oscillations = 0
    for j in range(1, len(trend)):
        if trend[j] != trend[j-1] and trend[j-1] != 0:
            oscillations += 1

    return sum(sequence)

# Misleading helper function that looks important but isn't used in final logic
def compute_entropy(data):
    from math import log
    freq = {}
    for x in data:
        freq[x] = freq.get(x, 0) + 1
    total = len(data)
    entropy = 0
    for v in freq.values():
        p = v / total
        entropy -= p * log(p, 2)
    return entropy

# Core processing function
lambda_transform = lambda x: x ** 2 - 3 * x + 2

def evaluate_series(values):
    transformed = [lambda_transform(v) for v in values]
    filtered = [t for t in transformed if t > 0]
    return sum(filtered) // len(values) if values else 0

# Main logic
benchmark_data = [4, 7, 2, 9, 5, 8]

# Dead code path - simulates preprocessing
if len(benchmark_data) % 2 == 0:
    padded_data = benchmark_data + [0]
else:
    padded_data = benchmark_data[:]

# Set operation to identify high performers (distractor with partial relevance)
high_performers = {x for x in benchmark_data if x >= 7}
low_performers = {x for x in benchmark_data if x < 5}
overlap_check = high_performers & low_performers  # Always empty, irrelevant

# Generate pairs for some analysis (unused but plausible)
pairs = list(combinations(benchmark_data, 2))
pair_sums = [a + b for a, b in pairs if a != b]

# Real work begins here
base_metric = analyze_pattern(benchmark_data)
secondary_metric = evaluate_series(benchmark_data)

# Intermediate calculation with misleading naming
efficiency_ratio = base_metric / len(benchmark_data)  # Not actually used in final score

# Actual accumulation leading to answer
temp_offset = 0
for val in benchmark_data:
    if val % 2 == 0:
        temp_offset += val // 2
    else:
        temp_offset -= val % 3

# Final performance calculation
final_score = secondary_metric + temp_offset - 5
print(f"Result: {final_score}")