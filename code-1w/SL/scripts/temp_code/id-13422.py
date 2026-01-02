def analyze_pattern(sequence):
    char_freq = {}
    for char in sequence:
        char_freq[char] = char_freq.get(char, 0) + 1
    return char_freq

# Irrelevant helper function (distractor)
def smooth_data(values):
    smoothed = [values[0]]
    for i in range(1, len(values)-1):
        smoothed.append((values[i-1] + values[i] + values[i+1]) / 3)
    smoothed.append(values[-1])
    return smoothed

# Simulate system logs with encoded patterns
event_log = "aaabbcdddeeefffgggghhhijjkkklll"
frequency_map = analyze_pattern(event_log)

# Extract unique character count and total length
unique_chars = len(frequency_map)
total_length = len(event_log)

# Hidden signal: count how many chars appear exactly 3 times
triple_occurrences = sum(1 for count in frequency_map.values() if count == 3)

# Bitwise obfuscation of a constant (semi-relevant)
key_mask = 0b101010
base_offset = 25
scrambled_seed = base_offset ^ key_mask  # 25 ^ 42 = 51

# Real metric computation begins here
raw_metrics = [unique_chars, total_length, triple_occurrences]
scaling_factor = 1.75

# Normalize metrics using lambda and enumerate
normalized = []
for idx, val in enumerate(raw_metrics):
    norm_fn = (lambda x, scale: x * scale) if idx % 2 == 0 else (lambda x, scale: x / scale)
    normalized.append(norm_fn(val, scaling_factor))

# Weighted evaluation using dictionary of weights
metric_weights = {
    'uniqueness': 0.4,
    'length_impact': 0.35,
    'pattern_rarity': 0.25
}

raw_results = {
    'uniqueness': normalized[0],
    'length_impact': normalized[1],
    'pattern_rarity': normalized[2]
}

# Secondary distraction: process unrelated token stream
token_stream = ['x', 'y', 'z']
index_map = dict(zip(token_stream, enumerate([10, 20, 30])))  # Complex but unused

# Core logic: weighted sum calculation
def evaluate_performance(weights, results):
    score = 0.0
    for k, w in weights.items():
        score += w * results[k]
    return int(score)  # Final answer is integer

final_score = evaluate_performance(metric_weights, raw_results)

# Distraction: unused intermediate transformation
transformed = list(map(lambda x: x ** 0.5, normalized))

# Print final result as required
print(f"Target result: {final_score}")