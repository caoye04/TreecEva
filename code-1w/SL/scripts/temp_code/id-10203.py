from itertools import groupby

def analyze_pattern(sequence):
    streaks = []
    current_streak = 0
    prev = None
    for item in sequence:
        if item == prev:
            current_streak += 1
        else:
            if prev is not None and current_streak > 0:
                streaks.append(current_streak)
            current_streak = 1
        prev = item
    if current_streak > 0:
        streaks.append(current_streak)
    return streaks

def compute_entropy(counts):
    total = sum(counts)
    entropy = 0
    for count in counts:
        p = count / total
        if p > 0:
            entropy -= p * __import__('math').log2(p)
    return round(entropy, 4)

def compute_final_score(raw_data):
    # Process raw data into grouped segments
    sorted_data = sorted(raw_data)
    grouped = {k: list(g) for k, g in groupby(sorted_data)}
    
    # Misleading intermediate computations (distractors)
    avg_length = sum(len(v) for v in grouped.values()) / len(grouped) if grouped else 0
    max_group_size = max(len(v) for v in grouped.values()) if grouped else 0
    temp_shadow = [len(v) * 2 for v in grouped.values() if len(v) % 2 == 0]
    shadow_sum = sum(temp_shadow)  # Unused later
    
    # Core logic: count character occurrences across all groups
    char_count = {}
    for key, items in grouped.items():
        for val in items:
            c = str(val)[0]  # First digit as character
            char_count[c] = char_count.get(c, 0) + 1
    
    # Compute frequency-based score
    frequencies = list(char_count.values())
    base_score = sum(f ** 2 for f in frequencies) // (len(frequencies) if frequencies else 1)
    
    # Additional irrelevant processing (dead path)
    if base_score > 10:
        adjustment = 0
        for i in range(3):
            adjustment += (base_score >> i) & 1
        base_score += adjustment  # Minor obfuscation

    # Final transformation using pattern analysis
    pattern_input = [len(v) for v in grouped.values()]
    patterns = analyze_pattern(pattern_input)
    entropy_component = compute_entropy(patterns)
    noise_offset = len([p for p in patterns if p >= 3]) * 0.25
    
    final_score = int(base_score + (entropy_component * 10) - noise_offset)
    
    return final_score

# Simulated dataset
raw_dataset = [23, 88, 88, 45, 45, 45, 91, 91, 91, 91, 7, 7, 7, 7, 7, 12, 12, 33]

# Key execution point
final_score = compute_final_score(raw_dataset)
print(f"Result: {final_score}")