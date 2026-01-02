def evaluate_performance(feedback):
    total = 0
    bonus = 0
    penalty = 0
    temp_sum = 0
    adjustment_factor = 1.2

    # Irrelevant string processing (distractor)
    feedback_text = ''.join(feedback)
    char_count = len(feedback_text)
    vowel_count = sum(1 for c in feedback_text.lower() if c in 'aeiou')
    average_vowels_per_entry = vowel_count / len(feedback) if feedback else 0

    # Real logic begins: scoring based on keywords
    keyword_scores = {
        'excellent': 10,
        'good': 5,
        'average': 2,
        'poor': -3,
        'failing': -8
    }

    performance_tiers = []

    for entry in feedback:
        entry_lower = entry.lower()
        base_value = 0

        # Check for keyword matches
        for keyword, score in keyword_scores.items():
            if keyword in entry_lower:
                base_value += score

        # Apply length-based bonus (semi-relevant)
        if len(entry) > 50:
            base_value += 1  # Slight reward for detailed feedback

        total += base_value
        performance_tiers.append(base_value)

        # Distractor: tracking unrelated stats
        temp_sum += len(entry.split())
        if 'comment' in entry_lower:
            bonus += 2
        if 'urgent' in entry_lower:
            penalty += 5

    # Real computation path
    if total > 20:
        bonus += 10
    elif total < 5:
        penalty += 15

    # Final adjustment with distractor variables intentionally not used
    final_score = total * adjustment_factor

    # Dead code branch (distractor)
    if False:
        final_score += bonus - penalty  # Never executed

    return int(final_score)

# Main execution
feedback_list = [
    "The performance was excellent overall.",
    "Good effort, but needs improvement in communication.",
    "Average results in most areas.",
    "Poor attendance and failing attitude observed."
]

# Key statement
final_score = evaluate_performance(feedback_list)
print(f"Result: {final_score}")