def analyze_pattern(sequence):
    count_vowels = sum(1 for c in sequence if c.lower() in 'aeiou')
    char_freq = {c: sequence.count(c) for c in set(sequence)}
    max_freq = max(char_freq.values())
    normalized = [ord(c) - ord('a') for c in sequence if c.isalpha()]
    return count_vowels, max_freq, normalized


def validate_sequence(seq):
    if not seq.isalpha():
        return False
    if len(seq) < 3:
        return False
    consecutive = all(abs(ord(seq[i]) - ord(seq[i+1])) == 1 for i in range(len(seq)-1))
    return consecutive or len(set(seq)) == len(seq)


def calculate_final_score(data, thresholds):
    raw_total = 0
    penalty = 0
    bonus = 0
    intermediate_results = []

    for entry in data:
        text = entry['text']
        weight = entry['weight']

        # Irrelevant preprocessing (distractor)
        reversed_text = text[::-1]
        mirrored = text + reversed_text
        _ = [c.upper() for c in mirrored if c.islower()]  # dead computation

        if not validate_sequence(text):
            penalty += entry['penalty']
            continue

        vowel_count, peak_freq, numeric_seq = analyze_pattern(text)

        base_value = vowel_count * weight
        if peak_freq > thresholds['repetition_limit']:
            base_value -= peak_freq

        trend_score = sum(numeric_seq[i] < numeric_seq[i+1] for i in range(len(numeric_seq)-1))
        adjustment = trend_score * 0.5 if trend_score > 3 else -1.5

        # Conditional expression (required Python feature)
        scaled_bonus = 10 if len(text) % 5 == 0 else (5 if len(text) > 8 else 0)
        
        entry_score = base_value + adjustment + scaled_bonus
        intermediate_results.append(entry_score)

        # More distractors
        outlier_check = [x for x in numeric_seq if x > 20]
        _ = sum(outlier_check) / len(outlier_check) if outlier_check else 0  # unused

    # Final aggregation logic
    raw_total = sum(intermediate_results)
    final_score = int(raw_total - penalty + bonus)

    # Extra misleading calculation
    avg_intermediate = sum(intermediate_results) / len(intermediate_results) if intermediate_results else 0
    _ = avg_intermediate * 1.5  # not used

    return final_score

# Main execution
config = {
    'repetition_limit': 2,
    'enable_enhancement': False
}

data_set = [
    {'text': 'abcdefgh', 'weight': 3, 'penalty': 7},
    {'text': 'programming', 'weight': 2, 'penalty': 5},
    {'text': 'xyz', 'weight': 4, 'penalty': 6},
    {'text': 'efghi', 'weight': 5, 'penalty': 4}
]

thresholds = {'repetition_limit': 2}
final_score = calculate_final_score(data_set, thresholds)
print(f"Result: {final_score}")