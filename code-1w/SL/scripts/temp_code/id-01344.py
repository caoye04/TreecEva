def analyze_frequency(text):
    char_count = {}
    for char in text:
        if char.isalpha():
            char_count[char.lower()] = char_count.get(char.lower(), 0) + 1
    return char_count

raw_input = 'ProgrammingLanguagesAreFunToWorkWith'
distinct_chars = len(set(raw_input.lower()))

# Misleading frequency analysis with irrelevant transformations
freq_map = analyze_frequency(raw_input)
scaled_values = [v * 1.5 for v in freq_map.values()]
normalized_total = sum(scaled_values) / len(scaled_values) if scaled_values else 0

# Dummy transformation chain
offset = sum([i for i, c in enumerate(raw_input) if c in 'aeiou'])
dummy_weights = {c: idx + offset for idx, c in enumerate('abcdefghijklmnopqrstuvwxyz')}

# Real processing path begins
filtered_letters = [c.lower() for c in raw_input if c.isalpha()]
unique_pairs = [(filtered_letters[i], filtered_letters[i+1]) for i in range(len(filtered_letters)-1)]
pair_scores = {p: (ord(p[0]) + ord(p[1])) % 7 for p in set(unique_pairs)}

def process_sequence(seq, scores):
    total = 0
    for i in range(len(seq) - 1):
        pair = (seq[i], seq[i+1])
        if pair in scores:
            total += scores[pair]
            # Introduce red herring counter
            temp_debug = (total * 2) % 19  # unused later
    return total

processed_data = process_sequence(filtered_letters, pair_scores)

# Secondary distraction: unused clustering logic
cluster_groups = {}
for k, v in freq_map.items():
    group_key = v % 3
    cluster_groups.setdefault(group_key, []).append(k)

# Actual final computation
base_value = processed_data * 3
adjustment_factor = len(freq_map) - len(cluster_groups)
final_score = base_value + adjustment_factor

print(f"Result: {final_score}")