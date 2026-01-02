def analyze_text_segment(segment, reference_set):
    char_frequency = {}
    for char in segment:
        if char.isalpha():
            lower_char = char.lower()
            char_frequency[lower_char] = char_frequency.get(lower_char, 0) + 1

    unique_chars = set(char_frequency.keys())
    overlap_count = len(unique_chars.intersection(reference_set))

    # Distractor: irrelevant statistical computation
    total_chars = sum(char_frequency.values())
    avg_frequency = total_chars / len(char_frequency) if char_frequency else 0
    entropy_proxy = 0
    for freq in char_frequency.values():
        if freq > 0 and total_chars > 0:
            prob = freq / total_chars
            entropy_proxy -= prob * __import__('math').log(prob) if prob > 0 else 0

    score = overlap_count * 10 + (5 if 'e' in char_frequency else 0)
    return score, total_chars, entropy_proxy


def filter_segments_by_pattern(segments):
    filtered = []
    pattern_flags = []
    for s in segments:
        has_repeated = any(s[i] == s[i+1] for i in range(len(s)-1))
        starts_with_vowel = s[0].lower() in 'aeiou' if s else False
        meets_criteria = has_repeated and not starts_with_vowel
        pattern_flags.append(meets_criteria)
        if meets_criteria:
            filtered.append(s)
    # Dead code path — never used
    debug_summary = {"filtered": len(filtered), "total": len(segments)}
    return filtered

segments = [
    "Hello World", "apple pie", "Success!!", "Looping code", "Quick brown fox",
    "Commit changes", "Programming", "Data analysis", "eelementary", "Tricky situation"
]

reference_letters = set('python')
raw_scores = []
processing_log = []  # Collected but unused

for seg in segments:
    score, length, entropy = analyze_text_segment(seg, reference_letters)
    adjustment = 0
    if length > 10:
        adjustment += 2
    if 'x' in seg.lower():
        adjustment -= 1
    adjusted_score = score + adjustment
    raw_scores.append(adjusted_score)
    processing_log.append(f'Scored {seg}: base={score}, adj={adjustment}')

# Simulate data transformation phase
processed_data = []
baseline_offset = sum(raw_scores) / len(raw_scores)
for idx, s in enumerate(raw_scores):
    normalized = s - baseline_offset
    # Irrelevant transformation
    padded_value = normalized + 100
    processed_data.append(padded_value)

# Secondary distractor: string-based validation (unused)
dummy_validation = [s.upper().replace(' ', '_') for s in segments if len(s) % 2 == 0]
validation_hash = sum(ord(c) for c in ''.join(dummy_validation)[:10]) % 97

extra_noise = []
for i in range(3):
    temp_val = (validation_hash * i) % 50
    extra_noise.append(temp_val)

# Core logic hidden among distractions
def calculate_final_score(data_list):
    trimmed = [x for x in data_list if x > 0]  # Filter non-positive
    if not trimmed:
        return 0
    mean_val = sum(trimmed) / len(trimmed)
    variance_proxy = sum((x - mean_val) ** 2 for x in trimmed) / len(trimmed)
    # Final scoring uses only mean and fixed offset
    result = int(mean_val + 0.8 * variance_proxy)
    return result

final_score = calculate_final_score(processed_data)
print(f"Target result: {final_score}")