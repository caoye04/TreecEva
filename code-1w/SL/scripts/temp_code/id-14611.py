def process_feedback(reviews, criteria):
    # Irrelevant helper: counts adjectives (distractor)
    def count_adjectives(text):
        words = text.lower().split()
        adj_suffixes = ['ful', 'ous', 'able', 'ible']
        return sum(1 for w in words if any(w.endswith(suf) for suf in adj_suffixes))

    # Semi-relevant normalization step
    normalized = []
    for review in reviews:
        clean = review.strip().lower()
        if len(clean) > 0 and clean[0] == '!':
            continue  # Skip admin notes
        normalized.append(clean.replace('!', '').replace('.', ''))

    # Core logic: sentiment keyword scoring
    positive = ['excellent', 'great', 'good', 'happy', 'pleased', 'satisfied']
    negative = ['bad', 'poor', 'terrible', 'awful', 'unhappy', 'disappointed']

    scores = []
    for entry in normalized:
        words = entry.split()
        score = 0
        adj_count = count_adjectives(entry)  # Computed but not used in final logic

        for word in words:
            if word in positive:
                score += 3
            elif word in negative:
                score -= 2

        # Apply length-based adjustment (semi-relevant)
        length_bonus = len(words) // 5
        score += length_bonus

        # Use slicing to ignore first and last word impact
        relevant_words = words[1:-1] if len(words) > 2 else words
        word_count_factor = len(relevant_words)

        # Final per-review score with arbitrary scaling
        final_entry_score = (score * 1.5) + (word_count_factor * 0.7)
        scores.append(final_entry_score)

    # Aggregate logic
    total = sum(scores)
    average = total / len(scores) if scores else 0

    # Threshold filtering based on criteria (unused branch as red herring)
    filtered = [s for s in scores if s >= criteria.get('min_threshold', 2.0)]
    ignored_count = len(scores) - len(filtered)  # Tracking unused metric

    # Main accumulation unaffected by filter
    base_accum = sum(round(s, 1) for s in scores)

    # Final transformation using modulo and string-based digit extraction
    checksum_str = ''.join([str(int(abs(s))) for s in scores])
    if checksum_str:
        # Extract every third digit using slicing
        selected_digits = checksum_str[::3]
        digit_sum = sum(int(d) for d in selected_digits)
    else:
        digit_sum = 0

    # Final score calculation
    final_score = int(base_accum + digit_sum - ignored_count)

    # Misleading dead code path
    if len(normalized) > 100:
        final_score *= 0.9  # Never reached due to input size

    return final_score

# Input data
feedback_reviews = [
    "Great service and excellent staff!",
    "I am unhappy with the bad experience.",
    "Poor support but good resolution.",
    "Absolutely wonderful and satisfying result.",
    "Terrible wait time and awful communication."
]

evaluation_criteria = {
    'min_threshold': 4.0,
    'weight': 1.0
}

# Execute
final_score = process_feedback(feedback_reviews, evaluation_criteria)
print(f"Target result: {final_score}")