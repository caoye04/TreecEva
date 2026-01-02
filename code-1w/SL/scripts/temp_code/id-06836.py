from collections import defaultdict, Counter

def analyze_pattern(seq):
    freq = Counter(seq)
    most = freq.most_common(1)[0][1]
    least = freq.most_common()[-1][1]
    return most - least

# Irrelevant helper (dead function - distractor)
def unused_util(data):
    return sum(x ** 2 for x in data if x % 3 == 0)

# Misleading transformation chain
temp_buffer = [i ^ 5 for i in range(15)]
shifted = [x >> 1 for x in temp_buffer]
decoy_sum = sum(shifted) * 2  # Red herring

# Core data
raw_input = [3, 7, 1, 4, 7, 3, 9, 7, 2]

# Distractor: complex but unused structure
lookup_table = defaultdict(int)
for idx, val in enumerate(raw_input):
    lookup_table[f"item_{idx}"] = val * 3 + (idx & 1)

# Real processing begins
filtered = [x for x in raw_input if x > 2]
sorted_pairs = sorted(zip(filtered, [x % 4 for x in filtered]), key=lambda p: p[1])

# Extract transformed values using slicing and enumerate
transformed = []
for i, (val, mod) in enumerate(sorted_pairs):
    if i % 2 == 0:
        transformed.append(val * 2 + mod)
    else:
        transformed.append(val - mod)

# Decoy intermediate
aggregate_temp = sum(transformed) / len(transformed) if transformed else 0
buffer_copy = transformed[::-1]  # Reversed slice - not used directly

# Key distraction: fake convergence check
converged = False
for _ in range(3):
    aggregate_temp = int(aggregate_temp) + (aggregate_temp - int(aggregate_temp)) * 1.5
    if abs(aggregate_temp - 12.5) < 0.1:
        converged = True
        break

# Real computation path
pattern_metric = analyze_pattern([x & 3 for x in raw_input])  # Bitwise frequency diff

# Weighted combination with irrelevant components
weight_a = len([x for x in raw_input if x % 2 == 1])  # Odd count
weight_b = min(raw_input) + (max(raw_input) // 2)

# Actual answer derivation
base_score = sum(transformed[:len(transformed)//2])  # First half only
penalty = pattern_metric * 2
bonus = weight_a if len(set(raw_input)) > 5 else 0

# Final aggregation with misleading additions
final_score = base_score - penalty + bonus
final_score += (decoy_sum % 7)  # Tiny irrelevant offset
final_score -= (sum(temp_buffer[:3]) % 5)  # Another negligible but distracting tweak

# Output the target result
print(f"Result: {final_score}")