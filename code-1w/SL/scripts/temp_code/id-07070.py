def analyze_pattern(sequence):
    counts = {}
    for char in sequence:
        counts[char] = counts.get(char, 0) + 1
    return counts

def normalize_values(values):
    total = sum(values)
    return [v / total for v in values] if total != 0 else values

# Simulated sensor data stream
data = ['A', 'B', 'A', 'C', 'B', 'A', 'D', 'C', 'A']
thresholds = {'A': 0.3, 'B': 0.25, 'C': 0.2, 'D': 0.1}

# Irrelevant preprocessing: character frequency analysis (distractor)
freq_map = analyze_pattern(data)
sorted_freq = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)
ranked_chars = [item[0] for item in sorted_freq]

# Another distraction: normalization of threshold values (not directly used)
normalized_thresholds = normalize_values(list(thresholds.values()))
max_normalized = max(normalized_thresholds)

# Core logic: compute expected frequencies from data
expected_counts = {}
for idx, val in enumerate(data):
    expected_counts[val] = expected_counts.get(val, 0) + 1

# Convert to proportions
proportions = {k: v / len(data) for k, v in expected_counts.items()}

# Compute match score against thresholds
match_scores = {}
for key in thresholds:
    if key in proportions:
        diff = abs(proportions[key] - thresholds[key])
        match_scores[key] = 1 - diff  # Higher = better match
    else:
        match_scores[key] = 0.0

# Secondary scoring based on position weight using enumerate (relevant)
position_score = 0.0
for i, ch in enumerate(data):
    weight = (i + 1) / len(data)  # increasing weight over time
    position_score += weight * (ord(ch) % 3)

# Use zip to align ranked characters with threshold keys (idiomatic but partially distracting)
zip_pairs = list(zip(ranked_chars, thresholds.keys()))
bonus_points = 0
for rc, tk in zip_pairs:
    if rc == tk:
        bonus_points += 1

# Final computation: weighted combination of match quality
base_match = sum(match_scores.values())
adjusted_match = base_match * (1 + position_score / 20)

# Distractor: unused intermediate calculation
theoretical_max = len(thresholds) * 1.5
scaling_factor = theoretical_max / (len(data) or 1)

# Key statement
final_score = int(adjusted_match + bonus_points)
print(f"Result: {final_score}")