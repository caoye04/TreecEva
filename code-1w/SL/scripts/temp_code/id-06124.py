def analyze_pattern(sequence):
    count_vowels = lambda s: sum(1 for c in s.lower() if c in 'aeiou')
    total_chars = len(sequence)
    vowel_count = count_vowels(sequence)
    consonant_count = total_chars - vowel_count

    # Distractor: irrelevant linguistic analysis
    syllable_estimate = max(1, vowel_count // 2)
    complexity_proxy = consonant_count * 1.5 + vowel_count * 0.8

    return vowel_count, consonant_count


def validate_thresholds(thresholds):
    if not all(0 <= t <= 100 for t in thresholds):
        return False
    mid_range = [t for t in thresholds if 30 < t < 70]
    return len(mid_range) >= 2


def calculate_final_score(data, thresholds):
    # Primary logic begins
    raw_sum = sum(ord(c) for c in data if c.isupper())
    offset = sum(thresholds) % 100

    # Intermediate transformations with some red herrings
    temp_results = []
    for i, char in enumerate(data):
        if char.isdigit():
            temp_results.append(int(char) ** 2)
        elif char in 'aeiou':
            temp_results.append(-1)

    # Real computation path
    bonus = 10 if 'X' in data else 0
    penalty = len([c for c in data if c in '!@#']) * 5

    # Distractor: unused phonetic scoring
    phonetic_weight = 0.0
    for c in data:
        if c.lower() in 'mnrl':
            phonetic_weight += 0.3
        elif c.lower() in 'bp':
            phonetic_weight += 0.2

    # Key branching logic
    if len(data) > 10 and validate_thresholds(thresholds):
        base_score = raw_sum + offset + bonus - penalty
        adjustment_factor = 1.2 if len(temp_results) > 3 else 0.9
    else:
        base_score = raw_sum - offset
        adjustment_factor = 1.0

    # Final calculation
    intermediate = int(base_score * adjustment_factor)
    final_score = intermediate + (thresholds[0] // 10) * 3

    # Irrelevant cleanup step (dead code path)
    if False:
        final_score = -999

    return final_score

# Setup inputs
user_input = "Ax9E2kPz!mX"
data = user_input.strip().upper()
thresholds = [45, 67, 23, 88, 12]

# Execute main logic
vowel_info, cons_info = analyze_pattern(data)
result_flag = validate_thresholds(thresholds)
score_snapshot = calculate_final_score(data, thresholds)

# Critical execution point
final_score = calculate_final_score(data, thresholds)

print(f"Result: {final_score}")